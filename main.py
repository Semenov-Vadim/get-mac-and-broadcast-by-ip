import netifaces


def get_mac_and_broadcast():
    res = []
    for iface in netifaces.interfaces():
        if iface == 'lo':  # excluding loopback
            continue
            
        iface_details = netifaces.ifaddresses(iface)
        for key in iface_details:
            if key == netifaces.AF_LINK:    #AF_LINK means the link layer interface, e.g. Ethernet
                res.append(iface_details[netifaces.AF_LINK])
    return res


if __name__ == "__main__":
    print(get_mac_and_broadcast())

