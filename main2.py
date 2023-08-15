import matplotlib.pyplot as plt
import numpy as np

# Data from the table
content_types = ['Text', 'Photo', 'Video', 'File', 'Audio']
avg_sizes = [306.61, 91.33, 35.49 * 1024 * 1024, 52.56 * 1024, 4.44 * 1024 * 1024]

# Sort average sizes in ascending order
sorted_avg_sizes = np.sort(avg_sizes)

# Calculate CCDF
ccdf = 1 - np.arange(1, len(sorted_avg_sizes) + 1) / len(sorted_avg_sizes)

# Create the CCDF plot
plt.semilogx(sorted_avg_sizes, ccdf, marker='o', linestyle='-', color='b')

plt.xlabel('Average Message Size')
plt.ylabel('Complementary Cumulative Distribution Function (CCDF)')
plt.title('CCDF of IM Size Distributions for Different Message Types')
plt.grid(True)

plt.show()