import matplotlib.pyplot as plt
import numpy as np

# Data from the table
content_types = ['Text', 'Photo', 'Video', 'File', 'Audio', 'Mix']
avg_inter_message_delay = [306.61, 91.33, 35.49, 52.56, 4.44]  # Average inter-message delay in seconds

# Create bins for histogram
bins = np.arange(0, max(avg_inter_message_delay) + 10, 10)

# Create the histogram
plt.hist(avg_inter_message_delay, bins=bins, density=True, alpha=0.7, color='b', label='Empirical PDF')

# Exponential distribution for comparison
lambda_parameter = 1 / np.mean(avg_inter_message_delay)
x = np.linspace(0, max(avg_inter_message_delay) + 10, 100)
exponential_pdf = lambda_parameter * np.exp(-lambda_parameter * x)
plt.plot(x, exponential_pdf, color='r', label='Exponential Distribution')

plt.xlabel('Average Inter-Message Delay (seconds)')
plt.ylabel('PDF')
plt.title('PDF of Inter-Message Delays and Exponential Distribution Fit')
plt.legend()

plt.grid(True)
plt.show()
