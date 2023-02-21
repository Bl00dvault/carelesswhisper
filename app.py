#################################################################################
# @note: Classification: Unclassified
# @author: bloodvault - Original Implemenation
# @brief: CARELESSWHISPER is designed to listen, read, and send UDP messages
#################################################################################
# Imports
# @note: Default Imports
import socket
import datetime
# @note: Installed Imports
import psutil
# @note: Developed Imports
import menu
#################################################################################

# @brief: This function queries the system datetime to use as a trigger
# @note: Don't remember the python getsystemtime() function, but something close to that would work here
# @warning: While loop in main() using this method has not been tested
def trigger_start():
    try:
        triggerTime = '12:59:59'
        now = datetime.now()
        currenttime = now.strftime('%H:%M:%S')
        if currenttime == triggerTime:
            main()
    except:
        return True
        # return False

# @brief: Identify UDP ports open (for send or receive) in order to ID where message traffic is
# @params: mission from main() since this is the first function called after the trigger, will pass down mission params as necessary
# @warning: Using this method will almost certainly miss messages since the list that is created in the for loop is not being simultaneously
#   iterated through. Using threading, or a different technique will be necessary for best results
def udp_port_search(mission):

    # @note: First need to find the correct interface to connect to 
    # @note: See layer2.py for outputs

    if mission == '5':
        # @note: Psuedo Code
        """```bash/python
        msghost = ip a | grep
        iptables FORWARD table entry all UDP to listenPort
        """
        # @note: Test Values
        msghost = '127.0.0.1'
        listenPort = 10000
        message_fwd_listen(listenPort, msghost)
    else:
        exit

# @brief: Listen for UDP message
# @param: send_port from messageFwd() is the proxied port which will send all traffic to this listener
# @param: msghost from messageFwd() is the IP address of the host that is sending/receiving messages
# @note: May also want to set a connection.timeout() for troubleshooting, or just for best results
def message_fwd_listen(send_port,msghost):
    # @note: Create UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # @note: Location of incoming data
    server_address = (msghost,send_port)
    # @note: Receive data
    sock.bind(server_address)
    print('Waiting for connection')

    ## Pick one of the following message sizes
    # @note: added timeout for debugging
    pkt_size = 240
    sock.settimeout(20)
    connection = sock.recvfrom(pkt_size)

    # Alternatively set the connection size to very large with a timeout buffer
    # pkt_size = 100000000
    # sock.settimeout(60)
    # connection = sock.recvfrom(pkt_size)

    try: 
        recv_data, sender_address = connection
        # print('received:\n    ', recv_data,'from:\n  ',sender_address)
        message_fwd_send(send_port,msghost)
    finally:
        exit

# @brief: Send UDP messages
# @params: send_port from message_fwd_listen(), and increment by 1 to avoid port conflict (send/receive on forwarding port)
# @params: msghost from message_fwd_listen() is host currently forwarding on
# @params: values currently corresponds to a properly formed message with erroneous data, the specification can be defined in <XXX> function
def message_fwd_send(send_port,msghost):
    # @note: Establish stream
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # @note: Location of hosted stream
    server_address = (msghost, send_port + 1)
    # @note: Connect to local socket
    sock.connect(server_address)
    # @note: Data stream variables
    values = draft_message(Message.header, 'header') + draft_message(Message.message, 'message')
    value = ''.join(values)
    byte_values = bytes(value,'utf-8')
    # values = b'100011100101001010010010010001010100010010100101010110110100'
    # @note: Send data
    try:
        print('sending "%s"' % byte_values)
        sock.sendto(byte_values,server_address)
    finally:
        print('closing socket')


# @brief: Read through list of created inputs for messages
# @note: Uncomment print statements and extra variables for verbose output
# @param: input - the padded message bits received from read_field_bits()
# @param: type - if specified include which part of the message the data is received from (header/data)
def draft_message(input, type):
    bits_output = []
    for field in input:
        bits_output.append(str(read_field_bits(field[0],field[2])))
    return bits_output


# @brief: Class defining the structure of data messages
class Message:
    def __init__(self):
        self.header = [

        ]
        self.message = [

        ]

# @brief: Function to read int() input data, and output as bits with appropriate field length
# @param: byte - Receive the bits data from UDP stream
# @param: bytesz - Specify the total size of the field , in order to pad the appropriate bytes
# @warning: When initially creating this I used global variables "padded_bits"
def read_field_bits(byte,bytesz):
    # @note: Set if statement to handle int(0) not playing nice
    if byte == 0:
        clean_bits = bin(0).lstrip('0b')
        padded_bits = clean_bits.rjust(bytesz,'0')
    else:
        bits = bin(int(byte))
        clean_bits = bits.lstrip('0b')
        padded_bits = clean_bits.rjust(bytesz,'0')
    return padded_bits

#################################################################################
# NEW HOTNESS
#################################################################################

def sendUDP():
    UDP_IP = '127.0.0.1'
    UDP_PORT = 5005
    #MESSAGE = b'This is a test'
    message = craftMessage(b'test')
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print('Sending... ', message)
    sock.sendto(message, (UDP_IP, UDP_PORT))

def listenUDP(timeout):
    timeout = int(timeout)
    UDP_IP = '127.0.0.1'
    UDP_PORT = 5005
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(timeout)
    sock.bind((UDP_IP, UDP_PORT))
    while True:
        print('Listening for UDP messages from ', UDP_IP, 'on', UDP_PORT)
        try:
            data, addr = sock.recvfrom(1024)
            print('Received message: ', data, '\nFrom IP: ', addr[0], '\nFrom Port: ', addr[1])
            break
        except ValueError:
            print('Did not receive any data after ', timeout, 'seconds')
            break

def craftMessage(message):
    try:
        message
        if isinstance(message) == str:
            return message
        elif isinstance(message) == bytes:
            return message
        elif isinstance(message) == int:
            return message
        else:
            print('Unknown message type')
    except:
        print(type(message))
        print('Unknown message format')


def main():
    args = menu.menu()
    try:
        args.app
    except:
        print('Unknown exception')
    finally:
        if args.app == 'lUDP':
            try:
                print('Timeout set for ' ,args.t , 'seconds')
                listenUDP(args.t)
            except:
                print('Timeout not set, setting socket timeout for 10 seconds')
                listenUDP(10)
        elif args.app == 'sUDP':
            sendUDP()
        elif args.app is None:
            print('Please supply arguments')
        else:
            print(f'Invalid module "%s"' % args.app)
            


if __name__ == '__main__':
    print('Starting Careless Whisper')
    print('\n')
    main()
