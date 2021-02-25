#!/usr/bin/env python3

#Example:
#    sudo ./my_ping.py --address google.com

import click
import scapy.route
from scapy.layers.inet import sr1,IP,ICMP
from scapy.config import conf
from scapy.supersocket import L3RawSocket

@click.command()
@click.option('-a', '--address', help='host to ping')
def icmp_ping(address):
    try:
        conf.L3socket=L3RawSocket
        packet = IP(dst=address)/ICMP()
        reply = sr1(packet, timeout=5, verbose=0)
        print ("it's alive" if reply else "host is down")
    except:
        print ("host is down")

if __name__ == '__main__':
    icmp_ping()

