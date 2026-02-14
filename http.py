from scapy.all import *
from scapy.layers.http import HTTPRequest

def http_yakala(pkt):
    if pkt.haslayer(HTTPRequest):
        try:
            host = pkt[HTTPRequest].Host.decode(errors="ignore")
            path = pkt[HTTPRequest].Path.decode(errors="ignore")
            print("\n[HTTP] İstek: " + host + path)

            if pkt.haslayer(Raw):
                raw_data = pkt[Raw].load.decode(errors="ignore")
                print("[BODY] Veri:")
                print(raw_data)
        except:
            pass

sniff(filter="tcp port 80", prn=http_yakala, store=False)