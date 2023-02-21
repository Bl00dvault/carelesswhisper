import socket

from app import message_fwd_listen

def message_fwd_send(send_port,msghost):
    # @note: Establish stream
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # @note: Location of hosted stream
    server_address = (msghost, send_port)
    # @note: Connect to local socket
    sock.connect(server_address)
    # @note: Data stream variables
    # values = draft_message(Message.header, 'header') + draft_message(Message.message, 'message')
    # value = ''.join(values)
    # byte_values = bytes(value,'utf-8')
    values = b'100011100101001010010010010001010100010010100101010110110100'
    # @note: Send data
    try:
        # print('sending "%s"' % byte_values)
        # sock.sendto(byte_values,server_address)
        print('sending "%s"' % values)
        sock.sendto(values, server_address)
    finally:
        print('closing socket')

send_port = 4924
msghost = '192.168.24.1'
message_fwd_send(send_port, msghost)