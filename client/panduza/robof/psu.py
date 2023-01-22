from robotlibcore import keyword
from robot.libraries.BuiltIn import BuiltIn



class KeywordsPsu(object):

    @keyword
    def turn_on_power_supply(self, name):
        """Turn on the psu
        """
        pza = BuiltIn().get_variable_value("${__pza__}")
        pza[name].state.value.set("on")

    @keyword
    def turn_off_power_supply(self, name):
        """Turn on the psu
        """
        pza = BuiltIn().get_variable_value("${__pza__}")
        pza[name].state.value.set("off")




