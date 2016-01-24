from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.util import custom

# Topology to be instantiated in Mininet
class ComplexTopo(Topo):
    "Mininet Complex Topology"

    def __init__(self, cpu=.1, max_queue_size=None, **params):

        # Initialize topo
        Topo.__init__(self, **params)

        #TODO: Create your Mininet Topology here!
        # Host and link configuration
        hostConfig = {'cpu': cpu}
        linkConfig_ethernet = {'bw': 20, 'delay': '1ms', 'loss': 0,
                   'max_queue_size': max_queue_size }
        linkConfig_wifi = {'bw': 10, 'delay': '3ms', 'loss': 3,
                   'max_queue_size': max_queue_size }
        linkConfig_3g = {'bw': 2, 'delay': '10ms', 'loss': 10,
                   'max_queue_size': max_queue_size }

        # Hosts and switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        h1 = self.addHost('h1', **hostConfig)
        h2 = self.addHost('h2', **hostConfig)
        h3 = self.addHost('h3', **hostConfig)

        # Connect to host1
        self.addLink(h1, s1, **linkConfig_ethernet)

        # Connecting switches
        self.addLink(s1, s2, **linkConfig_ethernet)
        self.addLink(s2, s3, **linkConfig_ethernet)
        self.addLink(s2, s4, **linkConfig_ethernet)

        # Connect to host2
        self.addLink(h2, s3, **linkConfig_wifi)
        # Connect to host3
        self.addLink(h3, s4, **linkConfig_3g)
