# @note: Downloaded Import
import psutil
# @note: Default Import
import re

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
