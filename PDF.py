from scapy.all import rdpcap
import numpy as np
import matplotlib.pyplot as plt


# Define a function to explore message delay distribution
def analyze_message_delays(file_path):
    # Load packet data from the trace file
    packets = rdpcap(file_path)

    # Extract packet timestamps and compute message delays
    timestamps = [packet.time for packet in packets]
    delays = np.array(np.diff(timestamps), dtype=float)  # Convert to float

    # Create a histogram to understand message delay pattern
    plt.hist(delays, bins=50, density=True, alpha=0.7, label="Message Delays")

    # Estimate exponential distribution parameter
    est_lambda = 1.0 / np.mean(delays)  # Estimate lambda

    # Generate points for the fitted exponential distribution
    x_vals = np.linspace(0, max(delays), 1000)
    y_vals = est_lambda * np.exp(-est_lambda * x_vals)

    # Plot the fitted exponential distribution
    plt.plot(x_vals, y_vals, label="Fitted Distribution", color="red")

    # Labels and title for the plot
    plt.xlabel("Delay between Messages (Seconds)")
    plt.ylabel("Probability Density")
    plt.title("Message Delay Distribution and Fitted PDF")
    plt.legend()

    # Show the plot
    plt.show()


# Analyze message delays using pcap file
analyze_message_delays("pcaps/FileAudio.pcap")
