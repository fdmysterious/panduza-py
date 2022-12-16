import os
import json
import logging
import threading

from abc import ABC, abstractmethod
from typing      import Optional, Callable, Set
from dataclasses import dataclass, field

from .client import Client


from .attribute import Attribute


# -----------------------------------------------------------------------------

@dataclass
class Field:
    
    name: str
    attribute: Attribute = None

    def __post_init__(self):
        """Initialize topics and logging
        """
        self.value = "off"

    def set_attribute(self, attribute):
        """
        """
        self.attribute = attribute

    def set(self, val):
        """
        """
        self.attribute.set(**{self.name: val})



    
 

