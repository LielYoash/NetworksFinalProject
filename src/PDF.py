import os
import matplotlib.pyplot as plt
import numpy as np
from scapy.all import rdpcap


def analyze_message_delays(file_path, output_filename):
    packets = rdpcap(file_path)
    timestamps = [packet.time for packet in packets]
    delays = np.array(np.diff(timestamps), dtype=float)

    plt.figure(figsize=(10, 6))
    plt.hist(delays, bins=50, density=True, alpha=0.7, label="Message Delays")

    est_lambda = 1.0 / np.mean(delays)
    x_vals = np.linspace(0, max(delays), 1000)
    y_vals = est_lambda * np.exp(-est_lambda * x_vals)

    plt.plot(x_vals, y_vals, label="Fitted Distribution", color="red")

    plt.xlabel("Inter-Message Delay (Seconds)")
    plt.ylabel("Probability Density Function")
    plt.title("Message Delay Distribution and Fitted PDF")
    plt.legend()

    plt.savefig(output_filename)  # Save the plot as a PNG file


def main():
    pcap_files_list = ['../resources/Raw/TextOnly.pcap','../resources/Raw/IMGonly.pcap','../resources/Raw/VideoOnly.pcap','../resources/Raw/FileAudio.pcap','../resources/Raw/Mixed_.pcap']
    for pcap_file in pcap_files_list:
        output_file_name = f'../res/PDF_results/{os.path.basename(pcap_file)[:-4]}.png'
        analyze_message_delays(pcap_file, output_file_name)


if __name__ == "__main__":
    main()
