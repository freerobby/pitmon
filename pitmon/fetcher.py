import threading
import time
import json
import os.path
from cyberqinterface.cyberqinterface import CyberQInterface


# TODO: param url and json file
class Fetcher(threading.Thread):

    def run(self):

        cyberq = CyberQInterface("127.0.0.1:8000/static")

        # If file exists, try to load it. If it doesn't or
        # load fails, start a new file
        if (os.path.isfile('/tmp/pitmon.json')):
            statefile = open('/tmp/pitmon.json')
            try:
                readings = json.load(statefile)
            except:
                readings = []
            statefile.close()
        else:
            readings = []

        banner = 0
        while True:
            if banner == 0:
                print "Time     , Output , Cook           , Food1          , Food2          , Food3"
            banner += 2
            if banner == 20:
                banner = 0

            result = cyberq.getAll()

            probes = ['COOK', 'FOOD1', 'FOOD2', 'FOOD3']
            temps = ['TEMP', 'SET']

            reading = dict()
            for probe in probes:
                for temp in temps:
                    key = '%s_%s' % (probe, temp)
                    reading[key] = float(result[probe][key])/10
                key = '%s_STATUS' % probe
                reading[key] = cyberq.statusLookup(result[probe][key])
            reading['OUTPUT_PERCENT'] = int(result['OUTPUT_PERCENT'])
            epoch = time.time()
            reading['TIMESTAMP'] = int(epoch)
            reading['DATE'] = time.strftime("%Y-%m-%d", time.localtime())
            reading['TIME'] = time.strftime("%H:%M:%S", time.localtime())
            readings.append(reading)

            statefile = open('/tmp/pitmon.json', 'w')
            json.dump(readings, statefile)
            statefile.close()

            print "%s , %6d , %5.1f %8s , %5.1f %8s , %5.1f %8s , %5d %8s" % (
                  reading['TIME'], reading['OUTPUT_PERCENT'],
                  reading['COOK_TEMP'], reading['COOK_STATUS'],
                  reading['FOOD1_TEMP'], reading['FOOD1_STATUS'],
                  reading['FOOD2_TEMP'], reading['FOOD2_STATUS'],
                  reading['FOOD3_TEMP'], reading['FOOD3_STATUS'])

            time.sleep(3.0)
