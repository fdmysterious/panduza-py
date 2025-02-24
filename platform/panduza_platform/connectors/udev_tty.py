import pyudev
from loguru import logger

def TTYPortFromUsbInfo(vendor_id:str , product_id:str , serial=None, base_devname="/dev/ttyACM"):
    """Find tty port from usb information
    """
    # Explore usb device with tty subsystem
    udev_context = pyudev.Context()
    # for device in udev_context.list_devices(ID_BUS='usb', SUBSYSTEM='tty'):
    for device in udev_context.list_devices(SUBSYSTEM='tty'):
        properties = dict(device.properties)
        
        # For debugging purpose
        # logger.debug(f"{properties}")

        # Need to find the one with the DEVNAME corresponding to the /dev serial port
        if 'DEVNAME' not in properties or not properties['DEVNAME'].startswith(base_devname):
            continue

        # Check vendor/product/serial
        if vendor_id == properties["ID_VENDOR_ID"] and product_id == properties["ID_MODEL_ID"]:
            if serial:
                if serial == properties["ID_SERIAL_SHORT"]:
                    return properties["DEVNAME"]
            else:
                return properties["DEVNAME"]

    raise Exception(f"ERROR: device tty for [{vendor_id}:{product_id}:{serial}:{base_devname}] not found !")





def SerialPortFromUsbSetting(**kwargs):
    """Find serial port from usb settings

    :param base_devname:
        base for the name of the serial port (sometimes usefull to match the correct interface)
    :param \**kwargs:
        See below

    :Keyword Arguments:
        * *vendor* (``str``) --
            ID_VENDOR_ID
        * *model* (``str``) --
            ID_MODEL_ID
        * *serial_short* (``str``) --
            ID_SERIAL_SHORT
        * *base_devname* (``str``) --
            /dev/ttyACM or USB

    """
    # Get parameters
    vendor          = None if "vendor" not in kwargs else kwargs["vendor"]
    model           = None if "model" not in kwargs else kwargs["model"]
    serial_short    = None if "serial_short" not in kwargs else kwargs["serial_short"]
    base_devname    = "/dev/ttyACM" if "base_devname" not in kwargs else kwargs["base_devname"]

    # Explore usb device with tty subsystem
    udev_context = pyudev.Context()
    for device in udev_context.list_devices(SUBSYSTEM='tty'):
        properties = dict(device.properties)
        
        # For debugging purpose
        # logger.debug(f"{properties}")

        # Need to find the one with the DEVNAME corresponding to the /dev serial port
        if 'DEVNAME' not in properties or not properties['DEVNAME'].startswith(base_devname):
            continue

        # Checks
        if vendor and (vendor != properties["ID_VENDOR_ID"]):
            continue
        if model and (model != properties["ID_MODEL_ID"]):
            continue
        if serial_short and (serial_short != properties["ID_SERIAL_SHORT"]):
            continue

        return properties["DEVNAME"]


    raise Exception(f"ERROR: device tty for [{vendor}:{model}:{serial_short}:{base_devname}] not found !")




def HuntUsbDevs(vendor, model=None, subsystem=None):
    """Return a list with devices fond with those criterias
    """
    results = []

    # Explore usb device with tty subsystem
    udev_context = pyudev.Context()

    # Convert properties
    # I don't understand how th pyudev filters works
    for device in udev_context.list_devices():
        properties = dict(device.properties)

        if not ( vendor and ("ID_VENDOR_ID" in properties) and (properties["ID_VENDOR_ID"]==vendor) ):
            continue
        if not ( model and ("ID_MODEL_ID" in properties) and (properties["ID_MODEL_ID"]==model) ):
            continue
        if not ( subsystem and ("SUBSYSTEM" in properties) and (properties["SUBSYSTEM"]==subsystem) ):
            continue

        results.append(properties)
        # For debugging purpose
        # logger.debug(f"{properties}")

    return results

