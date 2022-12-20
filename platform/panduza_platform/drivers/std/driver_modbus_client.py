import time
from ...meta_driver import MetaDriver
from ...connectors.modbus_client_serial import ConnectorModbusClientSerial

class DriverModbusClient(MetaDriver):
    """
    """

    ###########################################################################
    ###########################################################################

    def _PZADRV_config(self):
        return {
            "info": {
                "type": "modbus.client",
                "version": "0.0"
            },
            "compatible": [
                "modbus.client",
                "py.modbus.client"
            ]
        }

    ###########################################################################
    ###########################################################################

    def _PZADRV_loop_ini(self, tree):

        # self.log.debug(f"{tree}")

        settings = tree["settings"]

        # Get the gate
        self.modbus = ConnectorModbusClientSerial.Get(
            port=settings["serial"]["port"],
            baudrate=settings["serial"]["baudrate"]
        )


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
