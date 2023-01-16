import json
import threading
from ..core import Interface
from ..core import Interface, Attribute, EnsureError, RoField, RwField

class ModbusClient(Interface):
    """Interface to manage power supplies
    """

    def __init__(self, alias=None, addr=None, port=None, topic=None, client=None):
        """Constructor
        """
        super().__init__(alias, addr, port, topic, client)


    def _post_initialization(self):
        """Declare attributes here
        """
        # === HOLDING REGISTERS ===
        self.add_attribute(
            Attribute(
                name = "holding_regs"
            )
        ).add_field(
            RwField(
                name = "values"
            )
        )

        # === WATCHLIST ===
        self.add_attribute(
            Attribute(
                name = "watchlist"
            )
        ).add_field(
            RwField(
                name = "configs"
            )
        )



    def watch_holding_regs(self, addr, size, unit, polling_time_s = 2):
        """
        """
        # should append the new config here, not override it
        self.watchlist.configs.set([{
            "type": "holding_regs",
            "address": addr, "size": size, "unit": unit,"polling_time_s": polling_time_s
        }])

