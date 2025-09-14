from scapy.all import sniff, Ether, IP, TCP, UDP, Raw
import psutil
import requests
import threading
import time

def get_active_ethernet_interface():
    """Findet aktiv Interface"""
    for iface_name, addrs in psutil.net_if_addrs().items():
        stats = psutil.net_if_stats().get(iface_name)
        if stats is not None and stats.isup and "Ethernet" in iface_name:
            return iface_name
    return None

def show_packet_layers(packet):
    """Zeigt Paketinhalt OSI L2-L7"""
    print("\n--- Packet ---")

    # Layer 2
    if packet.haslayer(Ether):
        eth = packet[Ether]
        print(f"[L2] Ethernet: src={eth.src}, dst={eth.dst}, type={eth.type}")

    # Layer 3
    if packet.haslayer(IP):
        ip = packet[IP]
        print(f"[L3] IP: src={ip.src}, dst={ip.dst}, proto={ip.proto}")

    # Layer 4
    if packet.haslayer(TCP):
        tcp = packet[TCP]
        print(f"[L4] TCP: sport={tcp.sport}, dport={tcp.dport}, flags={tcp.flags}")
    elif packet.haslayer(UDP):
        udp = packet[UDP]
        print(f"[L4] UDP: sport={udp.sport}, dport={udp.dport}")

    # Layer 5-7
    if packet.haslayer(Raw):
        data = packet[Raw].load
        # L5 Session info
        print(f"[L5] Session: Port info erkannt")
        
        # L6 Darstellung
        try:
            text = data.decode('utf-8')
            print(f"[L6] Presentation: UTF-8 Text: {text[:50]} ...")
        except:
            print(f"[L6] Presentation: Raw bytes, Länge={len(data)}")
        
        # L7 Anwendung (HTTP, DNS etc.)
        if b"HTTP" in data or b"GET" in data or b"POST" in data:
            print(f"[L7] Application: HTTP Daten (erkannt)")
        elif b"DNS" in data:
            print(f"[L7] Application: DNS Daten (erkannt)")
        else:
            print(f"[L7] Application: Andere oder verschlüsselt")

def capture_packets(count=10, iface=None):
    print(f"Starte Packet Capture auf {iface}")
    packets = sniff(iface=iface, count=count, timeout=10)
    for pkt in packets:
        show_packet_layers(pkt)

def send_request():
    """HTTP(S) Request an Google.de"""
    try:
        requests.get("https://www.google.de")
    except Exception as e:
        print(f"Fehler bei HTTP Request: {e}")

if __name__ == "__main__":
    iface = get_active_ethernet_interface()
    if not iface:
        print("Kein aktiv Interface gefunden!")
        exit()

    # Thread für Packet Sniffer
    sniffer_thread = threading.Thread(target=capture_packets, args=(10, iface))
    sniffer_thread.start()

    # Kurze Pause, dann Request schicken
    time.sleep(2)
    send_request()

    sniffer_thread.join()
    print("Capture beendet.")
