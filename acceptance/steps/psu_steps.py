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

@Step('psu interface "{interface_name}" initialized with alias "{interface_alias}"')
def step(context, interface_name, interface_alias):
    context.interfaces["psu"][interface_name].init(alias=interface_alias)

###############################################################################
###############################################################################

@Step('psu interface "{interface_name}" change power supply state to "{state_value}"')
def step(context, interface_name, state_value):
    psu = context.interfaces["psu"][interface_name]
    state_bool = False
    if state_value == "on":
        state_bool = True
    psu.state.set(state_bool, ensure=True)

###############################################################################
###############################################################################

@Step('psu interface "{interface_name}" state is "{state_value}"')
def step(context, interface_name, state_value):
    psu = context.interfaces["psu"][interface_name]
    state_bool = False
    if state_value == "on":
        state_bool = True
    assert_that(psu.state.get(), equal_to(state_bool))


