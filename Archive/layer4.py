# @note: Downloaded Import
import psutil
# @note: Default Import
import socket
import re

# @brief: Find network interfaces in order to pass into arguments later
# @see: May also want to implement the NIC queries with netifaces library, see below
# import netifaces
# if_list = netifaces.interfaces()
def find_interface():
    addrs = psutil.net_if_addrs()
    for nic in addrs.keys():
        if nic == 'Ethernet':
            # @note: The keys in addrs[nic] are variable not set, thus need to create iterator and I'm bad at map()
            n = 0
            for subint in addrs[nic]:
                # @note: Need to handle validation of IP address (avoid MAC address), this is just an 
                # overcomplicated regex match using socket.inet_aton
                try:
                    nicAddrs = str(addrs[nic][n].address)
                    socket.inet_aton(nicAddrs)
                    print('Use this address: ', nicAddrs)
                    return nicAddrs
                except OSError:
                    n += 1
                    continue    

# @brief: Find UDP connection info                 
def find_udp_port():
    udpPortList = []
    connections = psutil.net_connections()
    # @note: Iterate through all open connections
    for port in connections:
        connectType = str(port[2])
        # @note: Filter out TCP connections
        if connectType == 'SocketKind.SOCK_DGRAM':
            # @note: Filter out IPv6
            if re.match(r'.*\:.*', str(port.laddr.ip)) is None:
                connectinfo = str(port.laddr.ip),':',str(port[6])
                connectinfo = ''.join(connectinfo)
                udpPortList.append(connectinfo)
    return udpPortList
        # print('IP', port.laddr.ip)
        # print('Port', port.laddr.port)
        # print('TCP/UDP', port[2])
        # print('PID', port[6])
        # print('\n')
    #print(connections)
