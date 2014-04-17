#    LittleCounter - A simple demonstration of how you use the BERG Cloud Linux
#                    client libraries to fetch and send data to BERG Cloud. For
#                    more info see http://bergcloud.com/
#
#    This example code is in the public domain.
#
#    https://github.com/bergcloud/devshield-raspberrypi

from bergcloud import *
import time
import msgpack

# The Project Key ties this code into a Project on developer.bergcloud.com
PROJECT_KEY = "8B05F72510540AE47C35EEE726DCD5A8"

# The version of your code
VERSION = 0x0001

# Define your commands and events here, according to the schema from bergcloud.com
COMMAND_SET_COUNTER     = 0x01
COMMAND_GREET           = 0x02
EVENT_COUNTER_CHANGED   = 0x01

# Initialise our counter
counter = 0

def littleCounter():
    global counter

    commandList = ["setCounter", "greet"]

    # Create an instance of BERGCloudLinux
    b = BERGCloud.BERGCloudLinux()
    b.begin("/dev/spidev0.0")

    print "--- LittleCounter start ---"

    # Attempt to connect with our project key and build version
    b.connect(PROJECT_KEY, VERSION, False)

    # Run continuously
    while True:

        #
        # Fetching commands
        #

        print "Poll for command... ",

        try:
            commandName, commandData = b.pollForCommand()
            print "got command with name: %s" % commandName

            if commandName in commandList:
                # Unpack the data using MessagePack
                unpacker = msgpack.Unpacker(encoding = 'utf-8')
                unpacker.feed(commandData)

                # Create a list of unpacked items
                itemList = []
                for item in unpacker:
                    itemList.append(item)

                # Call handler for this command
                if commandName == "setCounter":
                    handleSetCounter(b, itemList)
                elif commandName == "greet":
                    handleGreet(b, itemList)

            else:
                print "WARNING: Unknown command"
        except BERGCloud.BERGCloudException as e:
            if e.value == BERGCloud.SPI_RSP_NO_DATA:
                print "None"
            else:
                raise

        #
        # Sending events
        #

        print "Sending an event... ",

        # In this Little Counter example we send up a string and a counter.
        # There is currently a 64 byte limit on the size of events, so be
        # careful with how much data you're sending up!

        # Encode data using MessagePack
        packer = msgpack.Packer(encoding = 'utf-8', autoreset = False)
        packer.reset()
        packer.pack("BERG")
        packer.pack(counter)

        # Send the event object
        try:
            b.sendEvent("counterChanged", packer.bytes(), True) # 'True' flags the event as containing messagePack data
            print "ok"
        except BERGCloud.BERGCloudException:
            print "failed/busy"

        # Increment our counter each time we loop around
        counter += 1

        # A simple delay to rate limit what we send up to the cloud
        time.sleep(5)

def handleSetCounter(b, itemList):
    # We're expecting an integer value for the counter
    global counter

    if len(itemList) == 1:
        newCounterVal = itemList[0]
        if type(newCounterVal) is int:
            print "Decoded newCounterVal as: %i" % newCounterVal

            # Set the global to our new value
            counter = newCounterVal;

            # Show the string on the OLED screen with display()
            b.clearDisplay()

            # Print in reverse order
            b.display("%i" % counter)
            b.display("Counter set to")

        else:
            print "WARNING: Unexpected type when decoding the counter value"
    else:
        print "WARNING: unpacking the new counter value failed"

def handleGreet(b, itemList):
    # We're expecting a string and a number for display-text

    if len(itemList) == 1 or len(itemList) == 2:
        name = itemList[0]
        if type(name) is str or type(name) is unicode:
            # Convert from unicode
            text = name.encode('ascii', 'ignore')
            # Show the string on the OLED screen with display()
            b.clearDisplay()
            b.display("Hello, " + text)
        else:
            print "WARNING: Unexpected type when decoding the text"
    else:
        print "WARNING: unpacking text failed"

    # For this command, we can optionally be passed an integer
    # and we log this out on the serial console.
    #
    # This is to demonstrate serializing multiple values within
    # one command.

    if len(itemList) == 2:
        number = itemList[1]
        if type(number) is int:
            # Print the number
            print "Decoded number: %i" % number
        else:
            print "WARNING: Unexpected type when decoding the number"
    else:
        print "No additional number given"

if __name__ == "__main__":
    littleCounter()
