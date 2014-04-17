# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.4
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


"""
BERGCloud API. 
Copyright (c) BERG Cloud Limited 2013.
"""


from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_BERGCloud', [dirname(__file__)])
        except ImportError:
            import _BERGCloud
            return _BERGCloud
        if fp is not None:
            try:
                _mod = imp.load_module('_BERGCloud', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _BERGCloud = swig_import_helper()
    del swig_import_helper
else:
    import _BERGCloud
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


BC_EUI64_SIZE_BYTES = _BERGCloud.BC_EUI64_SIZE_BYTES
BC_ADDRESS_SIZE_BYTES = _BERGCloud.BC_ADDRESS_SIZE_BYTES
BC_CLAIMCODE_SIZE_BYTES = _BERGCloud.BC_CLAIMCODE_SIZE_BYTES
BC_KEY_SIZE_BYTES = _BERGCloud.BC_KEY_SIZE_BYTES
BC_PRINT_MAX_CHARS = _BERGCloud.BC_PRINT_MAX_CHARS
BC_EVENT_ANNOUNCE = _BERGCloud.BC_EVENT_ANNOUNCE
BC_COMMAND_SET_ADDRESS = _BERGCloud.BC_COMMAND_SET_ADDRESS
BC_COMMAND_START_RAW = _BERGCloud.BC_COMMAND_START_RAW
BC_COMMAND_START_PACKED = _BERGCloud.BC_COMMAND_START_PACKED
BC_COMMAND_NAMED_PACKED = _BERGCloud.BC_COMMAND_NAMED_PACKED
BC_COMMAND_ID_MASK = _BERGCloud.BC_COMMAND_ID_MASK
BC_COMMAND_FORMAT_MASK = _BERGCloud.BC_COMMAND_FORMAT_MASK
BC_COMMAND_DISPLAY_IMAGE = _BERGCloud.BC_COMMAND_DISPLAY_IMAGE
BC_COMMAND_DISPLAY_TEXT = _BERGCloud.BC_COMMAND_DISPLAY_TEXT
BC_EVENT_START_RAW = _BERGCloud.BC_EVENT_START_RAW
BC_EVENT_START_PACKED = _BERGCloud.BC_EVENT_START_PACKED
BC_EVENT_NAMED_PACKED = _BERGCloud.BC_EVENT_NAMED_PACKED
BC_EVENT_ID_MASK = _BERGCloud.BC_EVENT_ID_MASK
BC_EVENT_FORMAT_MASK = _BERGCloud.BC_EVENT_FORMAT_MASK
BC_COMMAND_FIRMWARE_ARDUINO = _BERGCloud.BC_COMMAND_FIRMWARE_ARDUINO
BC_COMMAND_FIRMWARE_MBED = _BERGCloud.BC_COMMAND_FIRMWARE_MBED
SPI_CMD_GET_CONNECT_STATE = _BERGCloud.SPI_CMD_GET_CONNECT_STATE
SPI_CMD_GET_CLAIMCODE = _BERGCloud.SPI_CMD_GET_CLAIMCODE
SPI_CMD_GET_CLAIM_STATE = _BERGCloud.SPI_CMD_GET_CLAIM_STATE
SPI_CMD_GET_SIGNAL_QUALITY = _BERGCloud.SPI_CMD_GET_SIGNAL_QUALITY
SPI_CMD_GET_EUI64 = _BERGCloud.SPI_CMD_GET_EUI64
SPI_CMD_SEND_ANNOUNCE = _BERGCloud.SPI_CMD_SEND_ANNOUNCE
SPI_CMD_GET_ADDRESS = _BERGCloud.SPI_CMD_GET_ADDRESS
SPI_CMD_POLL_FOR_COMMAND = _BERGCloud.SPI_CMD_POLL_FOR_COMMAND
SPI_CMD_SET_DISPLAY_STYLE = _BERGCloud.SPI_CMD_SET_DISPLAY_STYLE
SPI_CMD_DISPLAY_PRINT = _BERGCloud.SPI_CMD_DISPLAY_PRINT
SPI_CMD_SEND_EVENT_RAW = _BERGCloud.SPI_CMD_SEND_EVENT_RAW
SPI_CMD_SEND_EVENT_PACKED = _BERGCloud.SPI_CMD_SEND_EVENT_PACKED
SPI_PROTOCOL_PAD = _BERGCloud.SPI_PROTOCOL_PAD
SPI_PROTOCOL_PENDING = _BERGCloud.SPI_PROTOCOL_PENDING
SPI_PROTOCOL_RESET = _BERGCloud.SPI_PROTOCOL_RESET
BC_CONNECT_STATE_CONNECTED = _BERGCloud.BC_CONNECT_STATE_CONNECTED
BC_CONNECT_STATE_CONNECTING = _BERGCloud.BC_CONNECT_STATE_CONNECTING
BC_CONNECT_STATE_DISCONNECTED = _BERGCloud.BC_CONNECT_STATE_DISCONNECTED
BC_EUI64_NODE = _BERGCloud.BC_EUI64_NODE
BC_EUI64_PARENT = _BERGCloud.BC_EUI64_PARENT
BC_EUI64_COORDINATOR = _BERGCloud.BC_EUI64_COORDINATOR
BC_HOST_UNKNOWN = _BERGCloud.BC_HOST_UNKNOWN
BC_HOST_ARDUINO = _BERGCloud.BC_HOST_ARDUINO
BC_HOST_MBED = _BERGCloud.BC_HOST_MBED
BC_HOST_LINUX = _BERGCloud.BC_HOST_LINUX
BC_CLAIM_STATE_CLAIMED = _BERGCloud.BC_CLAIM_STATE_CLAIMED
BC_CLAIM_STATE_NOT_CLAIMED = _BERGCloud.BC_CLAIM_STATE_NOT_CLAIMED
BC_DISPLAY_NONE = _BERGCloud.BC_DISPLAY_NONE
BC_DISPLAY_STYLE_ONE_LINE = _BERGCloud.BC_DISPLAY_STYLE_ONE_LINE
BC_DISPLAY_STYLE_TWO_LINES = _BERGCloud.BC_DISPLAY_STYLE_TWO_LINES
BC_DISPLAY_STYLE_FOUR_LINES = _BERGCloud.BC_DISPLAY_STYLE_FOUR_LINES
BC_DISPLAY_CLEAR = _BERGCloud.BC_DISPLAY_CLEAR
SPI_EVENT_HEADER_SIZE_BYTES = _BERGCloud.SPI_EVENT_HEADER_SIZE_BYTES
SPI_MAX_PACKET_SIZE_BYTES = _BERGCloud.SPI_MAX_PACKET_SIZE_BYTES
SPI_HEADER_SIZE_BYTES = _BERGCloud.SPI_HEADER_SIZE_BYTES
SPI_FOOTER_SIZE_BYTES = _BERGCloud.SPI_FOOTER_SIZE_BYTES
SPI_MAX_PAYLOAD_SIZE_BYTES = _BERGCloud.SPI_MAX_PAYLOAD_SIZE_BYTES
SPI_RSP_SUCCESS = _BERGCloud.SPI_RSP_SUCCESS
SPI_RSP_INVALID_COMMAND = _BERGCloud.SPI_RSP_INVALID_COMMAND
SPI_RSP_BUSY = _BERGCloud.SPI_RSP_BUSY
SPI_RSP_NO_DATA = _BERGCloud.SPI_RSP_NO_DATA
SPI_RSP_SEND_FAILED = _BERGCloud.SPI_RSP_SEND_FAILED
SPI_RSP_NO_FREE_BUFFERS = _BERGCloud.SPI_RSP_NO_FREE_BUFFERS
class BERGCloudException(Exception):
    BERGCloudStatusDict = { 
    SPI_RSP_INVALID_COMMAND : "Invalid command",
    SPI_RSP_BUSY : "Busy",
    SPI_RSP_NO_DATA : "No data",
    SPI_RSP_SEND_FAILED : "Send failed",
    SPI_RSP_NO_FREE_BUFFERS : "No free buffers"
    }

    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return "0x%02x" % self.value
    def __str__(self):
        if self.value in self.BERGCloudStatusDict:
            return self.BERGCloudStatusDict[self.value]
        else:
            return "Undefined (0x%02x)" % self.value

class BERGCloudLinux(_object):
    """Proxy of C++ BERGCloudLinux class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, BERGCloudLinux, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, BERGCloudLinux, name)
    __repr__ = _swig_repr
    def begin(self, *args):
        """begin(self, char SPIpath)"""
        return _BERGCloud.BERGCloudLinux_begin(self, *args)

    def end(self):
        """end(self)"""
        return _BERGCloud.BERGCloudLinux_end(self)

    def pollForCommand_id(self):
        """
        pollForCommand_id(self) -> bool

        Check for a command.
        """
        return _BERGCloud.BERGCloudLinux_pollForCommand_id(self)

    def pollForCommand(self):
        """
        pollForCommand(self) -> bool

        Check for a command.
        """
        return _BERGCloud.BERGCloudLinux_pollForCommand(self)

    def sendEvent_id(self, *args):
        """
        sendEvent_id(self, uint8_t eventCode, uint8_t eventBuffer, bool packed = True) -> bool

        Send an event.
        """
        return _BERGCloud.BERGCloudLinux_sendEvent_id(self, *args)

    def sendEvent(self, *args):
        """
        sendEvent(self, char eventName, uint8_t eventBuffer, bool packed = True) -> bool

        Send an event.
        """
        return _BERGCloud.BERGCloudLinux_sendEvent(self, *args)

    def getConnectionState(self):
        """
        getConnectionState(self) -> bool

        Get the connection state.
        """
        return _BERGCloud.BERGCloudLinux_getConnectionState(self)

    def getSignalQuality(self):
        """
        getSignalQuality(self) -> bool

        Get the last-hop signal quality.
        """
        return _BERGCloud.BERGCloudLinux_getSignalQuality(self)

    def getClaimingState(self):
        """
        getClaimingState(self) -> bool

        Check if the device has been claimed.
        """
        return _BERGCloud.BERGCloudLinux_getClaimingState(self)

    def connect(self, *args):
        """
        connect(self, char key, uint16_t version, bool waitForConnected) -> bool

        Connect.
        """
        return _BERGCloud.BERGCloudLinux_connect(self, *args)

    def getClaimcode(self):
        """
        getClaimcode(self) -> bool

        Get the current claimcode.
        """
        return _BERGCloud.BERGCloudLinux_getClaimcode(self)

    def getEUI64(self, *args):
        """
        getEUI64(self, uint8_t type) -> bool

        Get the EUI64 identifier for this node, its parent or the network coordinator.
        """
        return _BERGCloud.BERGCloudLinux_getEUI64(self, *args)

    def getDeviceAddress(self):
        """
        getDeviceAddress(self) -> bool

        Get the Device Address.
        """
        return _BERGCloud.BERGCloudLinux_getDeviceAddress(self)

    def setDisplayStyle(self, *args):
        """
        setDisplayStyle(self, uint8_t style) -> bool

        Set the display style for the OLED display.
        """
        return _BERGCloud.BERGCloudLinux_setDisplayStyle(self, *args)

    def clearDisplay(self):
        """
        clearDisplay(self) -> bool

        Clear the OLED display.
        """
        return _BERGCloud.BERGCloudLinux_clearDisplay(self)

    def display(self, *args):
        """
        display(self, char text) -> bool

        Display a line of text on the OLED display.
        """
        return _BERGCloud.BERGCloudLinux_display(self, *args)

    __swig_setmethods__["lastResponse"] = _BERGCloud.BERGCloudLinux_lastResponse_set
    __swig_getmethods__["lastResponse"] = _BERGCloud.BERGCloudLinux_lastResponse_get
    if _newclass:lastResponse = _swig_property(_BERGCloud.BERGCloudLinux_lastResponse_get, _BERGCloud.BERGCloudLinux_lastResponse_set)
    def __init__(self): 
        """__init__(self) -> BERGCloudLinux"""
        this = _BERGCloud.new_BERGCloudLinux()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _BERGCloud.delete_BERGCloudLinux
    __del__ = lambda self : None;
BERGCloudLinux_swigregister = _BERGCloud.BERGCloudLinux_swigregister
BERGCloudLinux_swigregister(BERGCloudLinux)

# This file is compatible with both classic and new-style classes.


