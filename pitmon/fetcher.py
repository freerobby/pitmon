import threading
import time
import json
import os.path
from cyberqinterface.cyberqinterface import CyberQInterface


class Fetcher(threading.Thread):

    def run(self):

        probes = ['COOK', 'FOOD1', 'FOOD2', 'FOOD3']
        temps = ['TEMP', 'SET']
        statuses = ['COOK_STATUS', 'FOOD1_STATUS',
                    'FOOD2_STATUS', 'FOOD3_STATUS']
        generals = ['OUTPUT_PERCENT']

        cyberq = CyberQInterface("127.0.0.1:8000/static")

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
            result = cyberq.getAll()
            print "Output percent:", result.OUTPUT_PERCENT
            print "Output percent:", result['OUTPUT_PERCENT']
            print "Cook temp:", float(result.COOK.COOK_TEMP)/10
            print "Food1 temp:", float(result.FOOD1.FOOD1_TEMP)/10

            reading = dict()
            for probe in probes:
                for temp in temps:
                    key = '%s_%s' % (probe, temp)
                    reading[key] = float(result[probe][key])/10
                key = '%s_STATUS' % probe
                reading[key] = cyberq.statusLookup(result[probe][key])
            for general in generals:
                reading[general] = int(result[general])
            readings.append(reading)

            statefile = open('/tmp/pitmon.json', 'w')
            json.dump(readings, statefile)
            statefile.close()

            time.sleep(3.0)
