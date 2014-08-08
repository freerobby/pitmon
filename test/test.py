#!/usr/bin/env python2.7

# Verify CyberQInterface is installed correctly and can talk
# the CyberQ protocol
#
# This requires the pitmon server to be running and uses the
# sample files from the /static directory. This allows development
# without needing a live CyberQ device.
#
# From git project root run:
#
# $ PYTHONPATH=. python test/test.py

from cyberqinterface.cyberqinterface import CyberQInterface

print "== status.xml =="
result = CyberQInterface("127.0.0.1:8000/static/").getStatus()
print "Output percent:", result.OUTPUT_PERCENT
print "Cook temp:", result.COOK_TEMP
print "Food1 temp:", result.FOOD1_TEMP

print "\n== all.xml =="
result = CyberQInterface("127.0.0.1:8000/static/").getAll()
print "Output percent:", result.OUTPUT_PERCENT
print "Cook temp:", result.COOK.COOK_TEMP
print "Food1 temp:", result.FOOD1.FOOD1_TEMP
