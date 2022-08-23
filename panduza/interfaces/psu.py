import json
import threading
from ..core import Interface
from ..core import Attribute_JSON
from ..core import Interface, Attribute, EnsureError

# -----------------------------------------------------------------------------

class PsuNumericAttribute(Attribute):
    """! @brief This attribute manage volts and amps attributes because they are very similar
    """

    def __init__(self, b_topic, pza_client, name):
        """! @brief Constructor
        """
        super().__init__(client=pza_client, base_topic=b_topic, name=name)
        self.__trigger = threading.Event()


        """ @brief Current value of the attribute, it can set and get
        """
        self.__value = None
        self.__min: any = None
        self.__max: any = None
        self.__scale: any = None



    def __post_init__(self):
        """
        """
        super().__post_init__()

        # Subscribe to topic
        self.client.subscribe(self._topic_atts_get, callback=self.__update)

    def __update(self, topic, payload):
        """! @brief Callback triggered on reception of an mqtt messsage for this attribute
        """
        self._log.debug("Received new content")

        if payload is None:
            self.__value = None
            self.__min = None
            self.__max = None
            self.__scale = None
        else:
            data = json.loads(payload.decode("utf-8"))
            self.__value = data[self.name]
            self._log.debug(f"value : {self.__value}")
            self.__min = data["min"]
            self._log.debug(f"min : {self.__min}")
            self.__max = data["max"]
            self._log.debug(f"max : {self.__max}")
            self.__scale = data["scale"]
            self._log.debug(f"scale : {self.__scale}")
            self.__trigger.set()


    def get(self):
        return self.__value


    def set(self, v, ensure=False):

        retry=3
        if ensure:
            self.trigger_arm()

        self.client.publish(self._topic_cmds_set, self.payload_factory(v))

        if ensure:
            # It is possible that you catch some initialization message with the previous dir value
            # To manage this case, just wait for the correct value
            while self.__value != v or not retry:
                self.trigger_wait(timeout=3)
                if self.__value != v:
                    self.trigger_arm()
                    retry-=1

            if self.__value != v:
                raise RuntimeError(f"Attribute {self.name} for {self.base_topic}: cannot set to '{v}', got '{self.__value}'")




class Psu(Interface):
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

        self.state = Attribute_JSON(
            client          = self.client,
            base_topic      = self.base_topic,
            name            = "state",

            payload_factory = lambda v: json.dumps({"state": bool(v)}).encode("utf-8"),
            payload_parser  = lambda v: bool(json.loads(v.decode("utf-8"))["state"])
        )

        self.volts = Attribute_JSON(
            client          = self.client,
            base_topic      = self.base_topic,
            name            = "volts",

            payload_factory = lambda v: json.dumps({"volts": float(v)}).encode("utf-8"),
            payload_parser  = lambda v: bool(json.loads(v.decode("utf-8"))["volts"])
        )

        self.amps = PsuNumericAttribute(
            pza_client      = self.client,
            b_topic         = self.base_topic,
            name            = "amps",

            # payload_factory = lambda v: json.dumps({"amps": float(v)}).encode("utf-8"),
            # payload_parser  = lambda v: json.loads(v.decode("utf-8"))["amps"]
        )
