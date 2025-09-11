from scapy.all import sniff, Ether, IP, TCP, UDP, Raw
import psutil

def get_active_ethernet_interface():
    """Aktif Ethernet adaptörünü bul"""
    for iface_name, addrs in psutil.net_if_addrs().items():
        stats = psutil.net_if_stats().get(iface_name)
        if stats is not None and stats.isup and "Ethernet" in iface_name:
            return iface_name
    return None

def show_packet_layers(packet):
    """Paketin OSI katmanlarını göster"""
    print("\n--- Paket ---")
    if packet.haslayer(Ether):
        eth = packet[Ether]
        print(f"[L2] Ether: src={eth.src}, dst={eth.dst}, type={eth.type}")
    if packet.haslayer(IP):
        ip = packet[IP]
        print(f"[L3] IP: src={ip.src}, dst={ip.dst}, proto={ip.proto}")
    if packet.haslayer(TCP):
        tcp = packet[TCP]
        print(f"[L4] TCP: sport={tcp.sport}, dport={tcp.dport}, flags={tcp.flags}")
    elif packet.haslayer(UDP):
        udp = packet[UDP]
        print(f"[L4] UDP: sport={udp.sport}, dport={udp.dport}")
    if packet.haslayer(Raw):
        raw = packet[Raw].load
        print(f"[L7] Raw Data (truncated): {raw[:50]}...")  # Sadece ilk 50 byte göster

def capture_packets(count=100):
    iface = get_active_ethernet_interface()
    if not iface:
        print("Aktif Ethernet adaptörü bulunamadı!")
        return

    print(f"Paket yakalanıyor: {iface}")
    # TCP ve UDP paketlerini yakala (port sınırı yok)
    packets = sniff(iface=iface, filter="tcp or udp", count=count)
    for pkt in packets:
        show_packet_layers(pkt)

if __name__ == "__main__":
    print("Önce internet sitesini aç veya YouTube başlat...")
    input("Hazır olduğunda Enter tuşuna bas...")
    capture_packets()
