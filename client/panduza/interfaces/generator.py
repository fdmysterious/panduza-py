
import time
from ..core.core import Core
from ..core.interface import Interface

from .psu import Psu

def GenerateAllInterfacesFromAliases(connections):
    """
    """

    type_gen = {
        "psu": Psu
    }


    Core.LoadAliases(connections=connections)

    interfaces = {}
    for alias in Core.Aliases:
        itf = Interface(alias=alias)
        itf.info.ping()
        interfaces[alias] = itf

    time.sleep(1)

    # Generate interfaces in the correct type
    typed_interfaces = {}
    for name in interfaces:
        itf = interfaces[name]
        t = itf.info.get_type()
        assert t != "unknown", f"Error > {name} interface does not respond"
        # typed_interfaces[name] = type_gen[t](interface=itf)
        typed_interfaces[name] = Psu(interface=itf)
        
        
    return typed_interfaces



