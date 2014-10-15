import persist
import poller


pollthread = poller.Poller()
persistthread = persist.Persist()


def start(url):
    pollthread.setUrl(url)
    persistthread.setPoller(pollthread)

    # Start the poller thread, which communicates with the CyberQ
    pollthread.setDaemon(True)
    pollthread.start()

    # Start the persist thread, which saves graph points
    persistthread.setDaemon(True)
    persistthread.start()


def getlast():
    return pollthread.getlast()
