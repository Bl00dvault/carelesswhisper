import socket
import layer4_v1
import threading
import parsedata

class Thread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print('Starting',self.name)
        msgHost, sendPort = openUDP[self.threadID].split(':')
        #print('Waiting for connection on',msgHost,'at',sendPort,'\n')
        message_fwd_listen(sendPort,msgHost)
        #print('Exiting',self.name,'\n')

def message_fwd_listen(sendPort,msgHost):
    # @note: Create UDP socket
    # @warning: added timeout for debugging
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    timeout = 30
    sock.settimeout(timeout)
    # @note: Location of incoming data
    server_address = (msgHost,int(sendPort))
    # @note: Receive data
    # @warning: Requires root/admin access to accomplish
    try:
        sock.bind(server_address)
        #print('\nWaiting for connection on',msgHost,'at',sendPort,'\n')
    except Exception as e:
        # @note: Prints errors, normally handles [WinError 10048] Only one usage of each socket address 
        #   (protocol/network address/port) is normally permitted
        # print(e)
        next

    # @note: Packet size set "randomly"
    pkt_size = 240
    try:
        connection = sock.recvfrom(pkt_size)
        try: 
            recv_data, sender_address = connection
            #print('received:\n    ', recv_data,'from:\n  ',sender_address)
            parsedata.recv_data(recv_data,sender_address,server_address)
            # message_fwd_send(sendPort,msgHost)
        except Exception as e:
            # @note: Normally handles no data being received
            #print(e)
            next
    except:
        #print('Connection timeout after ',timeout,'seconds')
        next

# @note: Main function for now
def listen_threads():
    global threadLock
    global openUDP
    openUDP = layer4_v1.find_udp_port()
    threadLock = threading.Lock()
    for n in range(0,len(openUDP),1):
        threadN = 'thread'+str(n)
        threadN = Thread(n, 'Thread '+str(n), n)
        threadN.start()

listen_threads()
