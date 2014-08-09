import threading
import time
import json
import os.path
from cyberqinterface.cyberqinterface import CyberQInterface


class Fetcher(threading.Thread):

    def run(self):
        if (os.path.isfile('/tmp/pitmon.json')):
            statefile = open('/tmp/pitmon.json')
            try:
                readings = json.load(statefile)
            except:
                readings = []
            statefile.close()
        else:
            readings = []
        while True:
            result = CyberQInterface("127.0.0.1:8000/static").getAll()
            print "Output percent:", result.OUTPUT_PERCENT
            print "Cook temp:", float(result.COOK.COOK_TEMP)/10
            print "Food1 temp:", float(result.FOOD1.FOOD1_TEMP)/10

            reading = dict()
            reading['COOK_TEMP'] = float(result.COOK.COOK_TEMP)/10
            readings.append(reading)

            statefile = open('/tmp/pitmon.json', 'w')
            json.dump(readings, statefile)
            statefile.close()

            time.sleep(3.0)
