BERG Cloud for Raspberry Pi
===========================

This is the repository for the BERG Cloud python bindings for Raspberry Pi. It allows
easy integration with the Devshield, and we include sample code in the examples/
directory.

Installation
------------

The easiest way to install the library is with pip. To install it and the other
required libraries on your Raspbian distribution, type:

```
sudo apt-get install python-dev python-pip msgpack-python
```

Once these are installed, you can use pip to install the `bergcloud` library:

```
sudo pip install bergcloud
```

Depending on the version of Raspbian you're running you may find you get the following error when running the example code ```TypeError: __init__() got an unexpected keyword argument 'autoreset'```. In which case you can fix this by upgrading msgpack-python with the following command.

```
sudo pip install --upgrade msgpack-python
```

Adding the SPI driver
---------------------

In order to communicate with the Devshield you'll need to modify the system so that
it loads the ```spidev``` device driver. This can be done with the following steps:

```sudo nano /etc/modprobe.d/raspi-blacklist.conf```

Add a '#' to the start of the line saying ```spi-bcm2708``` and save the file. This
will ensure that the ```spidev``` driver is loaded when the system boots, so now
restart the system with:

```sudo reboot```

When the system comes back up, you should be able to see the spidev driver by
typing:

```ls -l /dev/spidev0.0```

Depending on how old your installation of the raspbian Linux operating system is,
you may need to add yourself to the `spi` group. You can check if you are already
a member by checking the output of the `groups` command.

If you see `spi` in the list, you are good to go. If you do not, then run the
following command:

```sudo adduser <your username> spi```

If you don't know your username, you can type `whoami` and it will tell you.


Example code
------------

To run the example code, simply go into the examples/ folder and run little_counter.py.
Don't forget to attach your BERG Cloud Devshield to your Raspberry Pi!

```
  cd examples/
  python little_counter.py
```

Documentation
-------------

See http://remote.bergcloud.com/developers/platform/reference/software/client-library for a description of the methods and examples.

Contact
-------

For more information see http://bergcloud.com/
