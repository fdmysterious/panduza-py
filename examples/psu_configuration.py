"""Example script to configure a power supply through an API_PSU

This example is compatible with the tree **acceptance/features/rsc/psu_tree.json**

"""

# Simple Standalone Test
import sys
import argparse
from panduza import Core
from panduza import Psu

# Load Aliases
# **acceptance/features/rsc/psu_alias.json**
Core.LoadAliases({
    "local_test": {
        "url": "localhost",
        "port": 1883,
        "interfaces": {
            "Pikachu": "pza/test/psu_fake/Pikachu"
        }
    }
})

# Create interface
psu = Psu(alias="Pikachu")

# Set voltage
psu.volts.set(5)

