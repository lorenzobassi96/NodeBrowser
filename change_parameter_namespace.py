#script.py (ip_server) (porta) (indice) (nuovo_parametro)
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
    param = str(sys.argv[4])

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
#signal.alarm(2)
    Server_Nodes = ServerNodes()
    Server_Nodes.build_list(Node(client.get_objects_node(), None))

    if param == 'False':
      Server_Nodes.node_list[2].node.set_value(False)

    if param == 'True':
      Server_Nodes.node_list[2].node.set_value(True)


    # Server_Nodes.node_list[2].get_node_value()


if __name__ == '__main__':
    # We create a Process
    action_process = Process(target=do_actions)

    # We start the process and we block for 5 seconds.
    action_process.start()
    action_process.join(timeout=5)

    # We terminate the process.
    action_process.terminate()
    print("Change of the variable applied !!!!")

