import json
from loguru import logger
from ..meta_driver import MetaDriver

class MetaDriverPsu(MetaDriver):
    """ Abstract Driver with helper class to manage power supply interface
    """
    
    ###########################################################################
    ###########################################################################
    #
    # MATA DRIVER OVERRIDE
    #
    ###########################################################################
    ###########################################################################

    def _PZADRV_config(self):
        return {
            "info": {
                "type": "psu",
                "version": "1.0"
            },
        }

    def _PZADRV_loop_ini(self, tree):

        self.__cmd_handlers = {
            "state": self.__handle_cmds_set_state,
            "volts": self.__handle_cmds_set_volts,
            "amps" : self.__handle_cmds_set_amps
        }

        self._update_attribute("state", "value", self._PZADRV_PSU_read_state_value())
        self._update_attribute("volts", "value", self._PZADRV_PSU_read_volts_value())
        self._pzadrv_ini_success()

    def _PZADRV_loop_run(self):
        pass

    def _PZADRV_cmds_set(self, payload):
        """From MetaDriver
        """
        cmds = self.payload_to_dict(payload)
        # self.log.debug(f"cmds as json : {cmds}")
        for att in self.__cmd_handlers:
            if att in cmds:
                self.__cmd_handlers[att](cmds[att])

    ###########################################################################
    ###########################################################################
    #
    # FOR SUBCLASS USE ONLY
    #
    ###########################################################################
    ###########################################################################

    def _pzadrv_psu_update_volts_min_max(self, min, max):
        self._update_attribute("volts", "min", min, False)
        self._update_attribute("volts", "max", max)

    def _pzadrv_psu_update_amps_min_max(self, min, max):
        self._update_attribute("amps", "min", min, False)
        self._update_attribute("amps", "max", max)

    def _pzadrv_psu_update_misc(self, field, value):
        self._update_attribute("misc", field, value)
    
    ###########################################################################
    ###########################################################################
    #
    # TO OVERRIDE IN DRIVER
    #
    ###########################################################################
    ###########################################################################

    def _PZADRV_PSU_read_state_value(self):
        """Must get the state value on the PSU and return it
        """
        raise NotImplementedError("Must be implemented !")

    def _PZADRV_PSU_write_state_value(self, v):
        """Must set *v* as the new state value on the PSU
        """
        raise NotImplementedError("Must be implemented !")
    
    def _PZADRV_PSU_read_volts_value(self):
        """Must get the volts value on the PSU and return it
        """
        raise NotImplementedError("Must be implemented !")
    
    def _PZADRV_PSU_write_volts_value(self, v):
        """Must set *v* as the new volts value on the PSU
        """
        raise NotImplementedError("Must be implemented !")

    def _PZADRV_PSU_read_amps_value(self):
        """Must get the volts value on the PSU and return it
        """
        raise NotImplementedError("Must be implemented !")
    
    def _PZADRV_PSU_write_amps_value(self, v):
        """Must set *v* as the new volts value on the PSU
        """
        raise NotImplementedError("Must be implemented !")

    ###########################################################################
    ###########################################################################
    #
    # PRIVATE
    #
    ###########################################################################
    ###########################################################################

    def __handle_cmds_set_state(self, cmd_att):
        """
        """
        if "value" in cmd_att:
            v = cmd_att["value"]
            # if not isinstance(v, int) or not isinstance(v, float):
            #     raise Exception(f"Invalid type for volts.value {type(v)}")
            try:
                self._PZADRV_PSU_write_state_value(v)
                self._update_attribute("state", "value", v)
            except Exception as e:
                self.log.error(f"{e}")

    def __handle_cmds_set_volts(self, cmd_att):
        """
        """
        if "value" in cmd_att:
            v = cmd_att["value"]
            if not isinstance(v, int) and not isinstance(v, float):
                raise Exception(f"Invalid type for volts.value {type(v)}")
            try:
                self._PZADRV_PSU_write_volts_value(v)
                self._update_attribute("volts", "value", self._PZADRV_PSU_read_volts_value())
            except Exception as e:
                self.log.error(f"{e}")

    def __handle_cmds_set_amps(self, cmd_att):
        """
        """
        if "value" in cmd_att:
            v = cmd_att["value"]
            if not isinstance(v, int) and not isinstance(v, float):
                raise Exception(f"Invalid type for volts.value {type(v)}")
            try:
                self._PZADRV_PSU_write_amps_value(v)
                self._update_attribute("amps", "value", v)
            except Exception as e:
                self.log.error(f"{e}")

