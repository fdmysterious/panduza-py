import time
from ...meta_driver import MetaDriver
from ...connectors.modbus_client_serial import ConnectorModbusClientSerial

from panduza_platform.connectors.udev_tty import HuntUsbDevs


class DriverModbusClient(MetaDriver):
    """Driver for modbus client
    """

    ###########################################################################
    ###########################################################################

    def _PZADRV_config(self):
        return {
            "name": "ModbusClient",
            "description": "Generic Modbus Client",
            "info": {
                "type": "modbus.client",
                "version": "0.0"
            },
            "compatible": [
                "modbus.client",
                "py.modbus.client"
            ]
        }



    def _PZADRV_tree_template(self,
        name="template",
        vendor="USB: Vendor ID",
        model="USB: Model ID",
        serial_short= "USB: Short Serial ID",
        port_name = "/dev/ttyUSBxxx or COM"
    ):
        template = {
            "name": "modbus_client:" + name,
            "driver": "py.modbus.client",
            "settings": {
                "mode": "rtu",
                "vendor": vendor,
                "model": model,
                "serial_short": serial_short,
                "port_name": port_name,
                "baudrate": "int => 9600 | 115200 ..."
            }
        }

        if port_name is None:
            del template["settings"]["port_name"]

        return template

    def _PZADRV_hunt_instances(self):
        instances = []

        # 16de:0003 Telemecanique USB - RS485 SL cable
        TELEMEC_VENDOR="16de"
        TELEMEC_MODEL="0003"
        usb_pieces = HuntUsbDevs(vendor=TELEMEC_VENDOR, model=TELEMEC_MODEL, subsystem="tty")
        for p in usb_pieces:
            iss = p["ID_SERIAL_SHORT"]
            instances.append(self._PZADRV_tree_template(
                name=iss,
                vendor=TELEMEC_VENDOR,
                model=TELEMEC_MODEL,
                serial_short=iss,
                port_name=None))

        return instances

    ###########################################################################
    ###########################################################################

    def _PZADRV_loop_ini(self, tree):

        # self.log.debug(f"{tree}")

        
        settings = dict() if "settings" not in tree else tree["settings"]
        settings["base_devname"] = "/dev/ttyUSB"

        # Get the gate
        self.modbus = ConnectorModbusClientSerial.GetV2(**settings)


        self.__cmd_handlers = {
            "holding_regs": self.__handle_cmds_set_holding_regs,
        }

        self._pzadrv_ini_success()


    ###########################################################################
    ###########################################################################

    def _PZADRV_loop_run(self):
        """
        """
        pass

    ###########################################################################
    ###########################################################################

    def _PZADRV_loop_err(self):
        """
        """
        pass

    ###########################################################################
    ###########################################################################

    def _PZADRV_cmds_set(self, payload):
        """From MetaDriver
        """
        cmds = self.payload_to_dict(payload)
        self.log.debug(f"cmds as json : {cmds}")
        for att in self.__cmd_handlers:
            if att in cmds:
                self.__cmd_handlers[att](cmds[att])

    ###########################################################################
    ###########################################################################

    def __handle_cmds_set_holding_regs(self, cmd_att):
        """
        """
        if "values" in cmd_att:
            values = cmd_att["values"]
            try:
                for u in values:
                    for addr in values[u]:
                        self.log.debug(f"on unit {u} write register {addr} with {values[u][addr]}")
                        self.modbus.write_register(int(addr), int(values[u][addr]), int(u) )

                # self._update_attribute("state", "value", v)
            except Exception as e:
                self.log.error(f"{e}")
