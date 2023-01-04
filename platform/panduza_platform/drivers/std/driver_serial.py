import io
from collections import ChainMap
from panduza_platform.meta_drivers.serial import MetaDriverSerial
from panduza_platform.connectors.serial_tty import ConnectorSerialTty

from panduza_platform.connectors.udev_tty import HuntUsbDevs




class DriverSerial(MetaDriverSerial):
    """
    """
    
    ###########################################################################
    ###########################################################################

    def _PZADRV_config(self):
        # Extend the common psu config
        return ChainMap(super()._PZADRV_config(), {
            "name": "Py_Serial",
            "description": "Generic Serial Interface",
            "compatible": [
                "serial",
                "py.serial"
            ]
        })

    # def __tgen(serial_short, name_suffix):
    #     return {
    #         "name": "QL355P:" + name_suffix,
    #         "driver": "py.psu.aimtty.ql355p",
    #         "settings": {
    #             "serial_short": serial_short
    #         }
    #     }

    # def _PZADRV_tree_template(self):
    #     return DriverQL355P.__tgen("USB: Short Serial ID", "template")

    # def _PZADRV_hunt_instances(self):
    #     instances = []
    #     usb_pieces = HuntUsbDevs(vendor=QL355P_USBID_VENDOR, model=QL355P_USBID_MODEL, subsystem="tty")
    #     for p in usb_pieces:
    #         iss = p["ID_SERIAL_SHORT"]
    #         instances.append(DriverQL355P.__tgen(iss, iss))
    #     return instances

    ###########################################################################
    ###########################################################################

    def _PZADRV_loop_ini(self, tree):

        # Get settings from tree and append constant settings for this device
        settings = dict() if "settings" not in tree else tree["settings"]
        settings["base_devname"] = "/dev/ttyUSB"
        
        # Get the connector
        self.serp = ConnectorSerialTty.Get(**settings)
 


        # Call meta class PSU ini
        super()._PZADRV_loop_ini(tree)



    def _PZADRV_loop_run(self):
        """
        """
        # Check if there is data waiting to be read
        if self.serp.get_internal_driver().in_waiting > 0:
            # Read the data
            data = self.serp.get_internal_driver().read(self.serp.get_internal_driver().in_waiting)
            self._PZADRV_SERIAL_data_received(data)

    ###########################################################################
    ###########################################################################

    def _PZADRV_SERIAL_write_data(self, v):
        """
        """
        self.serp.get_internal_driver().write(v)
        

