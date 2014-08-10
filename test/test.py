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

cyberq = CyberQInterface('192.168.142.155')

print "== status.xml =="
result = cyberq.getStatus()
print "Output percent:", result.OUTPUT_PERCENT
print "Cook temp:", float(result.COOK_TEMP)/10
print "Food1 temp:", float(result.FOOD1_TEMP)/10

print "\n== all.xml =="
result = cyberq.getAll()
print "Output percent:", result.OUTPUT_PERCENT
print "Cook temp:", float(result.COOK.COOK_TEMP)/10
print "Food1 temp:", float(result.FOOD1.FOOD1_TEMP)/10
print "Food1 status:", cyberq.statusLookup(result.FOOD1.FOOD1_STATUS)
