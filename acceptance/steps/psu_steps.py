import os
import time
from behave import *
from hamcrest import assert_that, equal_to
from xdocz_helpers import AttachTextLog, PathToRsc
from panduza import Core, Client

###############################################################################
###############################################################################

# Required to parse arguments in steps, for example "{thing}"
use_step_matcher("parse")

###############################################################################
###############################################################################

@Step('the psu interface "{interface_name}" initialized on test broker with topic "{interface_topic}"')
def step(ctx, interface_name, interface_topic):
    ctx.interfaces["psu"][interface_name].init(addr=ctx.TEST_BROKER_ADDR, port=ctx.TEST_BROKER_PORT, topic=interface_topic)

###############################################################################
###############################################################################

@Step('the psu interface "{interface_name}" method *XXX.state.value.set* is called with value "{value}"')
def step(ctx, interface_name, value):
    ctx.interfaces["psu"][interface_name].state.value.set(value)
    # let some time to the message to be registred by the listener
    time.sleep(0.5)

###############################################################################
###############################################################################

@Step("the broker must recieve '{payload}' on topic '{topic}'")
def step(ctx, payload, topic):
    assert_that(len(ctx.mqttMessages), equal_to(1))
    msg = ctx.mqttMessages[0]
    assert_that(msg.topic, equal_to(topic))
    assert_that(msg.payload.decode("utf-8"), equal_to(payload))
    ctx.mqttMessages = []



# ###############################################################################
# ###############################################################################

# @Step('psu interface "{interface_name}" initialized with alias "{interface_alias}"')
# def step(context, interface_name, interface_alias):
#     context.interfaces["psu"][interface_name].init(alias=interface_alias)

# ###############################################################################
# ###############################################################################

# @Step('psu interface "{interface_name}" change power supply state to "{state_value}"')
# def step(context, interface_name, state_value):
#     psu = context.interfaces["psu"][interface_name]
#     state_bool = False
#     if state_value == "on":
#         state_bool = True
#     psu.state.set(state_bool, ensure=True)

# ###############################################################################
# ###############################################################################

# @Step('psu interface "{interface_name}" state is "{state_value}"')
# def step(context, interface_name, state_value):
#     psu = context.interfaces["psu"][interface_name]
#     state_bool = False
#     if state_value == "on":
#         state_bool = True
#     assert_that(psu.state.get(), equal_to(state_bool))


