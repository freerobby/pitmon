import threading
import time
import json
import os.path
import config


class Persist(threading.Thread):

    # Reference to poller so we can fetch the last reading
    poller = None

    def run(self):

        while True:
            # If file exists, try to load it. If it doesn't or
            # load fails, start a new file
            if (os.path.isfile(config.output)):
                statefile = open(config.output)
                try:
                    readings = json.load(statefile)
                except:
                    readings = []
                statefile.close()
            else:
                readings = []

            reading = self.poller.getlast()
            if (reading is None):
                print "Warning, no valid reading from poller"
            else:
                readings.append(reading)

            statefile = open(config.output, 'w')
            json.dump(readings, statefile, indent=4)
            statefile.close()

            time.sleep(config.persist)

    def setpoller(self, poller):
        self.poller = poller
