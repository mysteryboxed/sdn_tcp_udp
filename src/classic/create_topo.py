#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet


class MyTopo(Topo):
    def __init__(self):
        Topo.__init__(self)

        # Add hosts
        u1 = self.addHost('u1', ip="172.18.0.1/24")
        u2 = self.addHost('u2', ip="172.18.1.1/24")
        u3 = self.addHost('u3', ip="172.18.2.1/24")
        u4 = self.addHost('u4', ip="172.18.3.1/24")
        u5 = self.addHost('u5', ip="172.18.4.1/24")
        u6 = self.addHost('u6', ip="172.18.2.3/24")
        u7 = self.addHost('u7', ip="172.18.2.4/24")
        u8 = self.addHost('u8', ip="172.18.2.5/24")

        # Add switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')
        s6 = self.addSwitch('s6')

        # Add links
        self.addLink(s1, u1)
        self.addLink(s2, u2)
        self.addLink(s3, u3)
        self.addLink(s3, u6)
        self.addLink(s3, u7)
        self.addLink(s3, u8)
        self.addLink(s4, u4)
        self.addLink(s5, u5)

        self.addLink(s1, s2, bw=50, delay='15ms', loss=0.5)
        self.addLink(s1, s6, bw=75, delay='10ms', loss=0.5)
        self.addLink(s1, s5, bw=50, delay='15ms', loss=0.5)
        self.addLink(s2, s3, bw=75, delay='10ms', loss=0.5)
        self.addLink(s2, s4, bw=50, delay='15ms', loss=0.5)
        self.addLink(s2, s6, bw=75, delay='10ms', loss=0.5)
        self.addLink(s3, s4, bw=75, delay='10ms', loss=0.5)
        self.addLink(s4, s6, bw=75, delay='10ms', loss=0.5)
        self.addLink(s4, s5, bw=50, delay='15ms', loss=0.5)
        self.addLink(s5, s6, bw=75, delay='10ms', loss=0.5)


topos = {'mytopo':MyTopo}
