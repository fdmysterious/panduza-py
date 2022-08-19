import json
from ..core import Interface
from ..core import Attribute_JSON

class Lace(Interface):
    """
    """

    ###########################################################################
    ###########################################################################
    
    def __init__(self, alias=None, url=None, port=None, b_topic=None, pza_client=None):
        """Constructor
        """
        super().__init__(alias, url, port, b_topic, pza_client)
