import threading
import time
from cyberqinterface.cyberqinterface import CyberQInterface


class Fetcher(threading.Thread):

    def run(self):
        while True:
            result = CyberQInterface("127.0.0.1:8000/static").getAll()
            print "Output percent:", result.OUTPUT_PERCENT
            print "Cook temp:", float(result.COOK.COOK_TEMP)/10
            print "Food1 temp:", float(result.FOOD1.FOOD1_TEMP)/10
            time.sleep(3.0)
