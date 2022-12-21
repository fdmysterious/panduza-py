import io
from collections import ChainMap
from panduza_platform.meta_drivers.psu import MetaDriverPsu
from panduza_platform.connectors.serial_tty import ConnectorSerialTty


QL355P_USBID_VENDOR="103e"
QL355P_USBID_MODEL="03e8"
QL355P_TTY_BASE="/dev/ttyUSB"

STATE_VALUE_ENUM = { "on": True, "off": False }
VOLTS_BOUNDS     = { "min": 0, "max": 30 }
AMPS_BOUNDS      = { "min": 0, "max":  5 }


class DriverQL355P(MetaDriverPsu):
    """
    """
    
    ###########################################################################
    ###########################################################################

    def _PZADRV_config(self):
        # Extend the common psu config
        return ChainMap(super()._PZADRV_config(), {
            "compatible": [
                "ql355p",
                "aimtty.ql355p",
                "psu.aimtty.ql355p",
                "py.psu.aimtty.ql355p"
            ]
        })

    ###########################################################################
    ###########################################################################

    def _PZADRV_loop_ini(self, tree):

        # Get settings from tree and append constant settings for this device
        settings = dict() if "settings" not in tree else tree["settings"]
        settings["vendor"] = QL355P_USBID_VENDOR
        settings["model"] = QL355P_USBID_MODEL
        settings["base_devname"] = QL355P_TTY_BASE
        
        # Get the connector
        self.serp = ConnectorSerialTty.Get(**settings)

        # TODO : Bad pratice "get_internal_driver" but used to speed up
        # https://stackoverflow.com/questions/10222788/line-buffered-serial-input
        self.io  = io.TextIOWrapper(
            self.serp.get_internal_driver(),
            encoding       = "ascii",
            newline        = None,
            line_buffering = False
        )
        self.io._CHUNK_SIZE= 1
        

        # TODO :Bad pratice with loopback variable instead of reading the value back
        self.state = "off"
        self.volts = 0
        self.amps = 0

        # Constants Fields settings
        self._pzadrv_psu_update_volts_min_max(VOLTS_BOUNDS["min"], VOLTS_BOUNDS["max"])
        self._pzadrv_psu_update_amps_min_max(AMPS_BOUNDS["min"], AMPS_BOUNDS["max"])

        # Misc
        self._pzadrv_psu_update_misc("model", "QL355P (AIM-TTI)")

        # Call meta class PSU ini
        super()._PZADRV_loop_ini(tree)


    ###########################################################################
    ###########################################################################

    def __write(self, *cmds):
        # Append new line terminator to all commands
        txt = "".join( map(lambda x: f"{x}\r\n", cmds) )

        self.log.debug(f"TX: {txt!r}")
        self.io.write(txt)
        self.io.flush()

    ###########################################################################
    ###########################################################################

    def _PZADRV_PSU_read_state_value(self):
        return self.state

    ###########################################################################
    ###########################################################################

    def _PZADRV_PSU_write_state_value(self, v):
        self.state = v
        cmd = STATE_VALUE_ENUM[v]
        self.__write(f"OP1 {int(cmd)}")

    ###########################################################################
    ###########################################################################

    def _PZADRV_PSU_read_volts_value(self):
        return self.volts

    ###########################################################################
    ###########################################################################

    def _PZADRV_PSU_write_volts_value(self, v):
        self.volts = v
        self.__write(f"V1 {v:.3f}")

    ###########################################################################
    ###########################################################################

    def _PZADRV_PSU_read_amps_value(self):
        return self.amps
    
    ###########################################################################
    ###########################################################################

    def _PZADRV_PSU_write_amps_value(self, v):
        self.amps = v
        self.__write(f"I1 {v:.3f}")


