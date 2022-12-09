import json
import threading
from ..core import Interface
from ..core import Interface, Attribute, EnsureError, Field


class Psu(Interface):
    """Interface to manage power supplies
    """

    def __init__(self, alias=None, addr=None, port=None, topic=None, client=None):
        """! Constructor
        """
        super().__init__(alias, addr, port, topic, client)


    def _post_initialization(self):
        """! Declare attributes here
        """
        # === STATE ===
        self.add_attribute(
            Attribute(
                name = "state"
            )
        ).add_field(
            Field(
                name = "value"
            )
        )
        # === VOLTS ===
        self.add_attribute(
            Attribute(
                name = "volts"
            )
        ).add_field(
            Field(
                name = "value"
            )
        )
        # === VOLTS ===
        self.add_attribute(
            Attribute(
                name = "amps"
            )
        ).add_field(
            Field(
                name = "value"
            )
        )

