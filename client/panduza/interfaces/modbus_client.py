import json
import threading
from ..core import Interface
from ..core import Interface, Attribute, EnsureError, Field


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
            Field(
                name = "values"
            )
        )

        # === WATCHLIST ===
        self.add_attribute(
            Attribute(
                name = "watchlist"
            )
        ).add_field(
            Field(
                name = "configs"
            )
        )


