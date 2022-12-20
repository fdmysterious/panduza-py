import time
import json
import paho.mqtt.client as mqtt

from .core import Core
from .client import Client


class Interface:
    """Access point to a Panduza interface
    """

    ###########################################################################
    ###########################################################################
    
    def __init__(self, alias=None, addr=None, port=None, topic=None, client=None):
        """Constructor
        """
        self._initialized = False
        self.init(alias, addr, port, topic, client)

    ###########################################################################
    ###########################################################################

    def _post_initialization(self):
        pass

    ###########################################################################
    ###########################################################################

    def init(self, alias=None, addr=None, port=None, topic=None, client=None):
        """Initialization of the interface
        """
        # Wait for later initialization
        if alias==None and addr==None and port==None and topic==None and client==None:
            return

        #
        if client != None:
            self.client = client
            self.topic = topic

        # Build a new client
        else:
            if alias:
                self.client = Client(interface_alias=alias)
                self.topic  = Core.BaseTopicFromAlias(alias)
            else:
                self.topic  = topic
                self.client = Client(url=addr, port=port)

        # 
        if not self.client.is_connected:
            self.client.connect()

        
        # #
        # self.heart_beat_monitoring = HeartBeatMonitoring(self.client, self.topic)
        

        # Initialization ok
        self._initialized = True

        #
        self._post_initialization()


    ###########################################################################
    ###########################################################################

    def add_attribute(self, attribute):
        # Append fields as attributes
        attribute.set_interface(self)
        setattr(self, attribute.name, attribute)
        return attribute

    ###########################################################################
    ###########################################################################

    def payload_to_dict(self, payload):
        """ To parse json payload
        """
        return json.loads(payload.decode("utf-8"))

    ###########################################################################
    ###########################################################################

    def payload_to_int(self, payload):
        """
        """
        return int(payload.decode("utf-8"))

    ###########################################################################
    ###########################################################################

    def payload_to_str(self, payload):
        """
        """
        return payload.decode("utf-8")

    # ###########################################################################
    # ###########################################################################

    # def isAlive(self):
    #     """
    #     """
    #     if not self.heart_beat_monitoring.enabled:
    #         raise Exception("watchdog not enabled on the interface")
        
    #     t0 = time.time()
    #     while (time.time() - t0 < 3) and not self.heart_beat_monitoring.alive:
    #         pass

    #     return self.heart_beat_monitoring.alive

    ###########################################################################
    ###########################################################################

    def _on_mqtt_message(self, client, userdata, msg):
        # print("!!!", msg.topic)

        if msg.topic.endswith('/info'):
            self.heart_beat_monitoring.update()

