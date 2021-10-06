import netifaces    #for get_mac_and_broadcast_by_interface
import os           #for get_inerface_by_ip()


def get_mac_and_broadcast_by_interface(iface: str):
    '''
    Find mac and broadcast using netifaces
    :param iface: The interface to search with
    :return: mac and broadcast if found, None if not found
    '''
    for ifaces in netifaces.interfaces():
        if ifaces == iface:
            iface_details = netifaces.ifaddresses(iface)
            for key_iface in iface_details:
                if key_iface == netifaces.AF_LINK:  # AF_LINK means the link layer interface, e.g. Ethernet
                    return iface_details[netifaces.AF_LINK]
            else:
                print('AF_LINK not found')
    else:
        print('interface not found')
    return None


def get_inerface_by_ip(ip: str):
    '''
    Find the interface using os library
    :param ip: The IP address to search with
    :return: The interface name if found, None if not found
    '''
    res = os.popen('ip route get ' + ip).read().split()

    counter = -1
    for i in res:
        counter += 1
        if i == 'dev':  #dev indicates the output device name
            return res[counter + 1]


if __name__ == "__main__":
    ip = '216.58.215.110'

    interface = get_inerface_by_ip(ip)
    res = get_mac_and_broadcast_by_interface(interface)

    print(res)


