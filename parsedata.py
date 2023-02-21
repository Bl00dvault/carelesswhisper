# @brief: This file is meant to handle incoming received data from layer2_v# 
# @warning: While threads are used on the listendata script, using thread locks here will be necessary
#   in order to track message throughout lifecycle of execution

def recv_data(recv_data,sender_address,server_address):
    print('Received',recv_data)
    print('From',sender_address)
    print('Hosted Port',server_address)

def parse_data():
    print()

