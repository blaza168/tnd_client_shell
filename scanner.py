from scapy.all import ARP, Ether, srp

# ip => scapy format of ip scan. Example: 192.168.1.1/24
def scan(ip):
    arp = ARP(pdst=ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")

    packet = ether/arp # Insert ARP to Ethernet

    result = srp(packet, timeout=3, verbose=0)[0] # srp function sends and receives packets at L2

    clients = []

    for sent, received in result:
        clients.append({'ip': received.psrc, 'mac': received.hwsrc})

    return clients