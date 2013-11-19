BERG Cloud for Raspberry Pi
===========================

This is the repository for the BERG Cloud python bindings for Raspberry Pi. It allows
easy integration with the Devshield, and we include sample code in the examples/
directory.

Installation
------------

The easiest way to install the library is with pip. To install pip on your Raspbian
distribution, type:

```
sudo apt-get install python-dev python-pip
```

Once pip is installed, you can use it to install the `bergcloud` library:

```
sudo pip install bergcloud
```

Example code
------------

To run the example code, simply go into the examples/ folder and run little_counter.py.
Don't forget to attach your BERG Cloud Devshield to your Raspberry Pi!

```
  cd examples/
  python little_counter.py
```

