import rpyc
import
import clr
clr.AddReference("System.Collections")
from
clr.AddReference()
from rpyc.utils.server import ThreadedServer


class MonitorService(rpyc.Service):

    def on_connect(self, conn):
        print("connected")

    def on_disconnect(self, conn):
        print("disconnect")
 

if __name__ == '__main__':
    t = ThreadedServer(MonitorService, port=8031)
    t.start()
