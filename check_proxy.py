#!/usr/bin/env python3
'''
Simple script to show your ip after connect to proxy
Usage: script_name [proxy_host:proxy_port]
default proxy is localhost:3001
'''
import socket
import logging
import socks
import sys

proxy = "localhost:3001".split(":") if len(sys.argv) < 2 else sys.argv[1].split(":")
host  = "ifconfig.me/ip"
port = 80
request = "GET /{1} HTTP/1.1\r\nHost: {0}\r\nUser-Agent: curl/7.58.0\r\n\r\n".format(*host.split("/"))

def resolv(address):
    logging.debug("Resolved %s (%s)" % (address,socket.gethostbyname(address)))
    return socket.gethostbyname(address)

logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s', level=logging.ERROR)
#Without proxy
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((resolv(host.split("/")[0]), port))
    logging.info("Successfully connected to host %s" % host)
    logging.debug("Request:\n%s" % request)
    s.send(request.encode())
    response = s.recv(4096).decode()
    logging.debug("Response:\n%s" % response)
    print ("My IP: %s" % response.split()[-1])
except Exception as err:
    logging.info("Unable to connected to host %s:%s" % (host,port))
    logging.info("Error: %s" % err)
    sys.exit(1)
finally:
    s.close()

#Behind proxy
try:
    s = socks.socksocket()
    s.setproxy(socks.PROXY_TYPE_SOCKS5, proxy[0], int(proxy[1]))
    s.connect((host.split("/")[0],port))
    logging.info("Successfully connected to proxy: {}:{}".format(*proxy))
    s.send(request.encode())
    logging.debug("Request:\n%s" % request)
    response = s.recv(4096).decode()
    logging.debug("Response:\n%s" % response)
    print ("Behind proxy my IP is: %s" % response.split()[-1])
except Exception as err:
    logging.info("Unable to connected to proxy {}:{}".format(*proxy))
    logging.info("Error: %s" % err)
finally:
    s.close()
