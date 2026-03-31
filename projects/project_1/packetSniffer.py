from scapy.all import sniff, Raw
import numpy as np
import csv 
from datetime import datetime 


class PacketAnalysis:
    def __init__(self):
        self.packet_number = 0
        self.csvwriter = None
        self.fields = ["Time", "Packet_Number", "Bytes", "Entropy", "Verdict"]
        self.file_name = "/Users/jeromeparungao/learnpython/learn-python/projects/project_1/summary.csv"

        with open(self.file_name, "w", newline="") as csvfile:
            csv.writer(csvfile).writerow(self.fields)

    def entropy_vectorized(self, data) -> float:
        if data.size == 0:
            return 0.0
        counts = np.bincount(data, minlength=256)
        prob = counts[counts > 0]/ len(data)
        return -np.sum(prob * np.log2(prob))

    def verdict(self, ent: float) -> str:
        if ent > 7.0:
            return "HIGH" # (likely encrypted/random)
        elif ent < 5.0:
            return "LOW" # (likely plain text)
        else:
            return "MEDIUM" # (mixed or compressed)

    def packet_handle(self, packet):
        self.packet_number += 1

        if not packet.haslayer(Raw):
            print(f"{self.packet_number} Packet | No Raw Data")
            return
        
        payload = packet[Raw].load
        arr = np.frombuffer(payload, dtype=np.uint8)
        entropy = self.entropy_vectorized(arr)
        verdict = self.verdict(entropy)

        print(f"{self.packet_number} Packet | {len(payload)} Bytes | Entropy = {entropy:.4f} bits/byte -> {verdict}")
        
        with open(self.file_name, "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([
                datetime.now().isoformat(),
                self.packet_number,
                len(payload),
                round(entropy, 4),
                verdict
            ])

if __name__ == "__main__":
    analyst = PacketAnalysis()
    print("Starting packet analysis")
    try: 
        sniff(prn=analyst.packet_handle, store=False)
    except KeyboardInterrupt:
        print("\nSniffer stopped.")

# print("Sniffing...")
# packets = sniff(count = 10)
# for i, packet in enumerate(packets):
#     if (packet.haslayer(Raw)):
#         raw_data = packet[Raw].load
#         arr = np.frombuffer(raw_data, dtype=np.uint8)
#         counts = np.bincount(arr, minlength=256)
#         entropy = entropy_vectorized(counts)
#         print(f"{i}th packet, and entropy = {entropy:.4f} -> {verdict(entropy)}: {len(raw_data)} bytes")
#         # print("Non-zero frequencies")
#         # for byte_val, freq in enumerate(counts):
#         #     if (freq> 0):
#         #         print(f"{byte_val}th byte with (0x{byte_val:02x}) {chr(byte_val)} : {freq}")
#     else:
#         print(f"Packet {i} has no Raw")


# sniffing a packet -> process of capturing, logging and analyzing data packets across a network
# packet = sniff(count = 1) # sniffs exactly count number of packets

# print(packet[0].summary())
# To see the full tree including the data:
# packet[0].show()

# # # To print just the raw data:
# def packet_callback(packet):
#     # Check if the packet has Raw
#     if packet.haslayer(Raw):
#         # Load the raw data
#         raw_data = packet[Raw].load
#         print("Found raw data with " + str(len(raw_data)) + " bytes")
#         print("First 50 bytes: " + str(raw_data[:50]))
#         print(f"Decoded: {raw_data[:50].decode('utf-8', errors='ignore')}")
#         print(50*"-")
#     else:
#         print("No Raw found")