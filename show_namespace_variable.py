#script.py (ip_server) (port) (index_namespace)
import time
from multiprocessing import Process
import signal
from node import *
from opcua import Client
import sys

def do_actions():
    """
    Function that should timeout after 5 seconds. It simply prints a number and waits 1 second.
    :return:
    """
    hostname = str(sys.argv[1])
    port = str(sys.argv[2])
    index = int(sys.argv[3])

    print (index)
    domain = "opc.tcp://"
    ddd = ":"
    final_address = (domain+hostname+ddd+port)



    try:
       client=Client(final_address)
       client.connect()
    except:
       print("Client couldn't connect to Server at " + "opc.tcp://"+hostname+":"+str(port))
       sys.exit(-1)


    #from node import *
    Server_Nodes = ServerNodes()
    Server_Nodes.build_list(Node(client.get_objects_node(), None))
    Server_Nodes.show_hierarchie()
    print ("-------------------------------")
    Server_Nodes.node_list[index].get_node_value()

    print ("--")

if __name__ == '__main__':
    # We create a Process
    action_process = Process(target=do_actions)

    # We start the process and we block for 5 seconds.
    action_process.start()
    action_process.join(timeout=10)

    # We terminate the process.
    action_process.terminate()
    index = int(sys.argv[3])
    print("This is the variable in position "+str(index)+" inside the Namespace" )

