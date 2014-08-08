#!/usr/bin/env python2.7

# Verify CyberQInterface is installed correctly and can talk
# to the CyberQ device
#
# From git project root run:
#
# $ PYTHONPATH=. python test/test.py

from cyberqinterface.cyberqinterface import CyberQInterface

all = CyberQInterface("127.0.0.1").getAll()
print all
