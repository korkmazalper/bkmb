from scapy.all import sniff, Ether, IP, TCP, UDP, Raw
import psutil

def get_active_ethernet_interface():
    """Aktif Ethernet interface bulur"""
    for iface_name, addrs in psutil.net_if_addrs().items():
        stats = psutil.net_if_stats().get(iface_name)
        if stats and stats.isup and "Ethernet" in iface_name:
            return iface_name
    return None

def show_packet_layers(packet):
    """Paketin tüm katmanlarını ve boyutlarını gösterir"""
    print("\n--- Paket Başlangıcı ---")
    
    # Layer 2 - Ethernet
    if packet.haslayer(Ether):
        eth = packet[Ether]
        print(f"[L2] Ether: src={eth.src}, dst={eth.dst}, type={eth.type}, length={len(eth)} bytes")
    
    # Layer 3 - IP
    if packet.haslayer(IP):
        ip = packet[IP]
        print(f"[L3] IP: src={ip.src}, dst={ip.dst}, proto={ip.proto}, length={len(ip)} bytes")
    
    # Layer 4 - TCP/UDP
    if packet.haslayer(TCP):
        tcp = packet[TCP]
        print(f"[L4] TCP: sport={tcp.sport}, dport={tcp.dport}, flags={tcp.flags}, length={len(tcp)} bytes")
    elif packet.haslayer(UDP):
        udp = packet[UDP]
        print(f"[L4] UDP: sport={udp.sport}, dport={udp.dport}, length={len(udp)} bytes")
    
    # Layer 5-7 - Raw / Uygulama verisi
    if packet.haslayer(Raw):
        raw = packet[Raw].load
        print(f"[L5-7] Raw Data: {len(raw)} bytes")
        print(f"Raw Bytes (ilk 64 byte): {raw[:64]}")  # İlk 64 byte’ı gösteriyoruz

def capture_packets(count=10):
    iface = get_active_ethernet_interface()
    if not iface:
        print("Aktif Ethernet interface bulunamadı!")
        return

    print(f"Yakalanıyor: {iface}")
    packets = sniff(iface=iface, count=count)
    for pkt in packets:
        show_packet_layers(pkt)

if __name__ == "__main__":
    capture_packets()
