import time
import signal
import logging
from subprocess import Popen, PIPE, STDOUT
from behave import fixture
from steps.xdocz_helpers import PathToRsc
import psutil
import paho.mqtt.client as mqtt

COLOR_LOG='\033[93m'
COLOR_ERR='\033[31m'
COLOR_END='\033[0m'
# TIMEOUT=(60 * 2)
TIMEOUT=5
RETRY_DELAY=0.2

###############################################################################
###############################################################################

def local_info(msg):
    print("\n", COLOR_LOG, msg, COLOR_END,"\n")

###############################################################################
###############################################################################

def local_err(msg):
    print("\n", COLOR_ERR, msg, COLOR_END,"\n")

###############################################################################
###############################################################################

def is_mosquitto_up():
    # Iterate over all running process
    for proc in psutil.process_iter():
        try:
            processName = proc.name()
            if "mosquitto" in processName:
                # print(proc)
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return False

###############################################################################
###############################################################################

def start_mosquitto():
    # 
    local_info("BROKER STARTING...")

    # Start the process
    Popen(["mosquitto", "-d"])

    # Wait for mosquitto up or timeout TIMEOUT seconds
    timeout = time.time() + TIMEOUT
    while (not is_mosquitto_up()) and (time.time() < timeout):
        time.sleep(RETRY_DELAY)

    # Check
    if is_mosquitto_up():
        local_info("BROKER STARTED")
    else:
        local_err("BROKER FAIL TO START")

    # Wait for the broker to be up
    time.sleep(0.5)

    # 
    return is_mosquitto_up()

###############################################################################
###############################################################################

def stop_mosquitto():
    if is_mosquitto_up():
        local_info("BROKER STOPPING...")
        # Kill the process
        Popen(["pkill", "--signal", "SIGKILL", "-eci", "mosquitto"])

        # Wait for mosquitto down or timeout TIMEOUT seconds
        timeout = time.time() + TIMEOUT
        while (is_mosquitto_up()) and (time.time() < timeout):
            time.sleep(RETRY_DELAY)
        
        # Check
        if not is_mosquitto_up():
            local_info("BROKER STOPPED")
        else:
            local_err("BROKER FAIL TO STOP")

    # Return true if success
    return not is_mosquitto_up()

###############################################################################
###############################################################################

@fixture
def fixture_broker(context, config_file):
    """Manage the mosquitto broker fixture
    """
    # -- SETUP-FIXTURE PART:
    #
    started_flag=True

    # Restart
    stop_mosquitto()
    start_mosquitto()

    # -- READY FOR THE STEP --
    yield started_flag
    # -- CLEANUP-FIXTURE PART:

    # Stop
    stop_mosquitto()


###############################################################################
###############################################################################

@fixture
def fixture_mqtt_listener(ctx):
    
    ctx.mqttMessages=[]

    def on_message(client, userdata, message):
        userdata.append(message)

    ctx.mqttListener = mqtt.Client(userdata=ctx.mqttMessages)
    ctx.mqttListener.on_message = on_message
    ctx.mqttListener.connect(ctx.TEST_BROKER_ADDR, ctx.TEST_BROKER_PORT)
    ctx.mqttListener.subscribe("pza/#")
    ctx.mqttListener.loop_start()

    yield ctx.mqttListener

    ctx.mqttListener.disconnect()
    ctx.mqttListener.loop_stop()

