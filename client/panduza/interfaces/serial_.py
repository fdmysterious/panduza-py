import json
import base64
import threading
from dataclasses import dataclass, field
from ..core import Interface
from ..core import Interface, Attribute, EnsureError, RoField, RwField



@dataclass
class AttributeData(Attribute):
    _rx_buffer: bytes = None


    def _on_att_message(self, topic, payload):
        self._log.debug("overload !!!")




class Serial(Interface):
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
            AttributeData(
                name = "data"
            )
        ).add_field(
            RwField(
                name = "tx"
            )
        ).add_field(
            RwField(
                name = "rx"
            )
        )


    def send(self, tx_data: bytes):
        tx_encoded = base64.b64encode(tx_data)
        base64_message = tx_encoded.decode('ascii')
        self.data.tx.set(base64_message)




