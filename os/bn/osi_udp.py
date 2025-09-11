from scapy.all import sniff, Ether, IP, TCP, UDP, Raw
import psutil
import threading
import webbrowser
import time

def get_active_interface():
    for iface_name, addrs in psutil.net_if_addrs().items():
        stats = psutil.net_if_stats().get(iface_name)
        if stats is not None and stats.isup:
            if "Ethernet" in iface_name or "Wi-Fi" in iface_name:
                return iface_name
    return None

def show_packet_layers(packet):
    print("\n--- Paket ---")
    if packet.haslayer(Ether):
        eth = packet[Ether]
        print(f"[L2] Ethernet: src={eth.src}, dst={eth.dst}, type={eth.type}")
    if packet.haslayer(IP):
        ip = packet[IP]
        print(f"[L3] IP: src={ip.src}, dst={ip.dst}, proto={ip.proto}")
    if packet.haslayer(TCP):
        tcp = packet[TCP]
        print(f"[L4] TCP: sport={tcp.sport}, dport={tcp.dport}, flags={tcp.flags}, len={len(tcp)}")
    elif packet.haslayer(UDP):
        udp = packet[UDP]
        print(f"[L4] UDP: sport={udp.sport}, dport={udp.dport}, len={len(udp)}")
    if packet.haslayer(Raw):
        raw = packet[Raw]
        print(f"[L5-7] Raw data length: {len(raw.load)} bytes")
    else:
        print("[L5-7] Raw data: yok")

def capture_packets(count=10):
    iface = get_active_interface()
    if not iface:
        print("Aktif interface bulunamadı!")
        return
    print(f"Paketler {iface} üzerinden yakalanıyor...")
    packets = sniff(iface=iface, filter="tcp port 443 or udp", count=count)
    for pkt in packets:
        show_packet_layers(pkt)

def open_website(url):
    webbrowser.open(url)

if __name__ == "__main__":
    threading.Thread(target=open_website, args=("https://www.google.de",), daemon=True).start()
    time.sleep(2)
    threading.Thread(target=open_website, args=("https://www.youtube.com/watch?v=dQw4w9WgXcQ",), daemon=True).start()
    capture_packets(count=20)
