from getmac import getmac
import ipaddr

ip = '192.168.0.103'
short_mask = '/24'

mac_address = getmac.get_mac_address(ip = ip, network_request = True)
mask = ipaddr.IPv4Network(ip + short_mask)

# print(mask.netmask)
print('mac address: ', mac_address)
print('broadcast: ', mask.broadcast)
