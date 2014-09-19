import threading
import time
import copy
from cyberqinterface.cyberqinterface import CyberQInterface
import config


# TODO: param url and json file
class Poller(threading.Thread):

    last = dict()

    def run(self):

        cyberq = CyberQInterface(config.url)

        banner = 0
        while True:
            #if banner == 0:
                #print "Time     , Output , Cook           , Food1          , Food2          , Food3"
            #banner += 2
            #if banner == 20:
            #    banner = 0

            result = cyberq.getAll()

            probes = ['COOK', 'FOOD1', 'FOOD2', 'FOOD3']
            temps = ['TEMP', 'SET']

            reading = dict()
            for probe in probes:
                for temp in temps:
                    key = '%s_%s' % (probe, temp)
                    if result[probe][key] == 'OPEN':
                        reading[key] = 0.0
                        reading['%s_STATUS' % probe] = 'NO PROBE'
                    else:
                        reading[key] = int(result[probe][key])/10
                key = '%s_STATUS' % probe
                if key not in reading:
                    reading[key] = cyberq.statusLookup(result[probe][key])
                key = '%s_NAME' % probe
                reading[key] = result[probe][key].text
            reading['OUTPUT_PERCENT'] = int(result['OUTPUT_PERCENT'])
            epoch = time.time()
            reading['TIMESTAMP'] = int(epoch)
            reading['DATE'] = time.strftime("%Y-%m-%d", time.localtime())
            reading['TIME'] = time.strftime("%H:%M:%S", time.localtime())

            #print "%s , %6d , %5.1f %8s , %5.1f %8s , %5.1f %8s , %5.1f %8s" % (
            #      reading['TIME'], reading['OUTPUT_PERCENT'],
            #      reading['COOK_TEMP'], reading['COOK_STATUS'],
            #      reading['FOOD1_TEMP'], reading['FOOD1_STATUS'],
            #      reading['FOOD2_TEMP'], reading['FOOD2_STATUS'],
            #      reading['FOOD3_TEMP'], reading['FOOD3_STATUS'])

            self.last = reading
            time.sleep(config.poll)

    def getlast(self):
        return copy.deepcopy(self.last)
