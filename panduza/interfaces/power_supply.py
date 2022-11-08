import json
from ..core import Interface
from ..core import Attribute_JSON

class PowerSupply(Interface):
    """Interface to manage power supplies
    """

    ###########################################################################
    ###########################################################################
    
    def __init__(self, alias=None, url=None, port=None, b_topic=None, pza_client=None):
        """Constructor
        """
        super().__init__(alias, url, port, b_topic, pza_client)

    ###########################################################################
    ###########################################################################

    def _post_initialization(self):
        """Declare attributes here
        """

        state_values = {
            "off": False,
            "on": True
        }

        self.state = Attribute_JSON(
            client          = self.client,
            base_topic      = self.base_topic,
            name            = "state",

            payload_factory = lambda v: json.dumps({"state": "on" if v else "off"}).encode("utf-8"),
            payload_parser  = lambda v: state_values[json.loads(v.decode("utf-8"))["state"]]
        )

        self.volts = Attribute_JSON(
            client          = self.client,
            base_topic      = self.base_topic,
            name            = "volts",

            payload_factory = lambda v: json.dumps({"volts": float(v)}).encode("utf-8"),
            payload_parser  = lambda v: json.loads(v.decode("utf-8"))["volts"]["value"]
        )

        self.amps = Attribute_JSON(
            client          = self.client,
            base_topic      = self.base_topic,
            name            = "amps",

            payload_factory = lambda v: json.dumps({"amps": float(v)}).encode("utf-8"),
            payload_parser  = lambda v: json.loads(v.decode("utf-8"))["amps"]["value"]
        )
