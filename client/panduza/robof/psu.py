from robotlibcore import keyword
from robot.libraries.BuiltIn import BuiltIn



class KeywordsPsu(object):

    @keyword
    def set_power_supply_voltage(self, name, voltage):
        """
        """
        pza = BuiltIn().get_variable_value("${__pza__}")
        pza[name].volts.value.set(float(voltage))

    @keyword
    def turn_on_power_supply(self, name):
        """Turn on the psu
        """
        pza = BuiltIn().get_variable_value("${__pza__}")
        pza[name].state.value.set("on")

    @keyword
    def turn_off_power_supply(self, name, teardown=False):
        """Turn on the psu
        """
        pza = BuiltIn().get_variable_value("${__pza__}")

        if pza == None:
            # It is ok if panduza is not initialized, only if in the teardown process
            assert not teardown
        else:
            pza[name].state.value.set("off")


