######################################################################
#
# Filename: NodeBrowser.py
# Author: Johannes4Linux
# Date: 04.04.2020
#
# A simple command line tool to browse through all the nodes 
# in an OPC UA Server
#
######################################################################

from node import *
from opcua import Client
import sys
from sys import argv


hostname = str(sys.argv[1])
port = str(sys.argv[2])  

#if hostname == "":
#    hostname = "localhost"

#if port == "":
#    port = 4840
#else:
#    try:
#        port = int(port);
#    except:
#        print("Invalid Port Number!")
#        sys.exit(-1)

#start = input("Select start point: 1: Objects Node, 2: Root Node [default: 1]: ")
#if start == "":
#    start = 1
#else:
#    try:
#        start = int(start)
#        if start not in [1,2]:
#            raise ValueError
#    except:
#        print("Invalid Option!")
#        sys.exit(-1)
        
#try:
#    client = Client("opc.tcp://"+hostname+":"+str(port))
#    client.connect()
#except:
#    print("Client couldn't connect to Server at " + "opc.tcp://"+hostname+":"+str(port))
#    sys.exit(-1)

domain = "opc.tcp://"
ddd = ":"
final_address = (domain+hostname+ddd+port)
try:
   client=Client(final_address)
   client.connect()
except:
   print("Client couldn't connect to Server at " + "opc.tcp://"+hostname+":"+str(port))
   sys.exit(-1)

client.get_root_node()
client.get_objects_node()

Server_Nodes = ServerNodes()
Server_Nodes.build_list(Node(client.get_objects_node(), None))
Server_Nodes.show_hierarchie()
client.close_session()
