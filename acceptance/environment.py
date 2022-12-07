import os
import logging
from behave import *

from steps.xdocz_helpers import AttachTextLog

from fixtures.client import client
from fixtures.interface import interface_io
from fixtures.interface import interface_psu
from fixtures.interface import interface_file

from fixtures.broker_mosquitto import fixture_broker, fixture_mqtt_listener

###############################################################################
###############################################################################

FIX_NAME_BROKER="fixture.broker."

def before_tag(ctx, tag):
    """Execute before each tag
    """

    
    #
    # Process fixture tags
    #
    if tag.startswith("fixture.interface.io"):
        name = tag.replace("fixture.interface.io.", "")
        use_fixture(interface_io, ctx, name=name)
    elif tag.startswith("fixture.interface.psu"):
        name = tag.replace("fixture.interface.psu.", "")
        use_fixture(interface_psu, ctx, name=name)
    elif tag.startswith("fixture.interface.file"):
        name = tag.replace("fixture.interface.file.", "")
        use_fixture(interface_file, ctx, name=name)
    elif tag.startswith("fixture.client"):
        name = tag.replace("fixture.client.", "")
        use_fixture(client, ctx, name=name)
    
    elif tag.startswith("fixture.broker."):
        config_file = tag.replace("fixture.broker.", "")
        use_fixture(fixture_broker, ctx, config_file=config_file)
    elif tag.startswith("fixture.mqtt-listener"):
        use_fixture(fixture_mqtt_listener, ctx)


    


###############################################################################
###############################################################################

def before_all(ctx):
    """Function executed before anything else
    """
    # Make sure that the directory of the acceptance report exists
    os.makedirs('acceptance/report', exist_ok=True)

    # Enable logging
    # logging.basicConfig(level=logging.DEBUG)

    ctx.TEST_BROKER_ADDR="localhost"
    ctx.TEST_BROKER_PORT=1883

###############################################################################
###############################################################################

# def after_all(context):
#     """After all tests
#     """
#     pass
    
    
        