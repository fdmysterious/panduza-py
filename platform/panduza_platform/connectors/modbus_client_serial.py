import time
import serial
# import minimalmodbus
from loguru import logger

from pymodbus.client import ModbusSerialClient 

from .udev_tty import TTYPortFromUsbInfo

from .modbus_client_base import ConnectorModbusClientBase

class ConnectorModbusClientSerial(ConnectorModbusClientBase):
    """The serial modbus client connector centralize access to a given port as a modbus client
    """

    # Contains instances
    __instances = {}

    ###########################################################################
    ###########################################################################

    @staticmethod
    def Get(usb_vendor_id: str = None, usb_product_id: str = None, usb_serial_id: str = None, usb_base_dev_tty: str ="/dev/ttyACM",
        port: str = None, baudrate: int = 19200, bytesize: int = 8, parity: chr = 'N', stopbits: int = 1,
        validator=None):
        """Singleton main getter
        """

        # Get the serial port key
        key = None
        if port != None:
            key = port
        elif usb_vendor_id != None and usb_product_id != None:
            key = TTYPortFromUsbInfo(usb_vendor_id, usb_product_id, usb_serial_id, usb_base_dev_tty)
        else:
            raise Exception("no way to identify the modbus serial port")

        # Create the new connector
        if not (key in ConnectorModbusClientSerial.__instances):
            ConnectorModbusClientSerial.__instances[key] = None
            try:
                new_instance = ConnectorModbusClientSerial(key, baudrate, bytesize, parity, stopbits, validator)
                ConnectorModbusClientSerial.__instances[key] = new_instance
            except Exception as e:
                ConnectorModbusClientSerial.__instances.pop(key)
                raise Exception('Error during initialization').with_traceback(e.__traceback__)

        # Return the previously created
        return ConnectorModbusClientSerial.__instances[key]

    ###########################################################################
    ###########################################################################

    def __init__(self, key: str = None, baudrate: int = 19200, bytesize: int = 8, parity: chr = 'N', stopbits: int = 1, validator=None):
        """Constructor
        """
        if not (key in ConnectorModbusClientSerial.__instances):
            raise Exception("You need to pass through Get method to create an instance")
        else:
            self.log = logger.bind(driver_name=key)
            self.log.info(f"attached to the Modbus Serial Client Connector")

            # create client object
            self.client = ModbusSerialClient(port=key, baudrate=baudrate, bytesize=bytesize, parity=parity, stopbits=stopbits)
            # connect to device
            self.client.connect()

            # In case multiple bus match previous conditions
            # TODO need to be improve 
            if validator:
                validator(self)
  

            # print( self.client.read_device_information() )
            # self.client.write_register(48, 50, unit=1)
            # self.client.write_register(1, 1, unit=1)



            # # disconnect device
            # client.close()



    ###########################################################################
    ###########################################################################

    def write_register(self, address: int, value, unit: int = 1):
        """
        """
        response = self.client.write_register(address, value, unit=unit)
        if response.isError():
            raise Exception(f'Error message: {response}')

    ###########################################################################
    ###########################################################################

    def read_input_registers(self, address: int, size: int = 1, unit: int = 1):
        """
        """
        response = self.client.read_input_registers(address, size, unit=unit)
        if not response.isError():
            return response.registers
        else:
            raise Exception(f'Error message: {response}')

    ###########################################################################
    ###########################################################################

    def read_holding_registers(self, address: int, size: int = 1, unit: int = 1):
        """
        """
        response = self.client.read_holding_registers(address, size, unit=unit)
        if not response.isError():
            return response.registers
        else:
            raise Exception(f'Error message: {response}')


