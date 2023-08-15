import warnings
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
warnings.filterwarnings('ignore')
matplotlib.use("TkAgg")

filter_list = ['resources\\WITH_TCP_FILTER_TARGET1.csv', 'resources\\WITH_TCP_FILTER_TARGET2.csv',
               'resources\\WITH_TCP_FILTER_TARGET3.csv', 'resources\\WITH_TCP_FILTER_TARGET4.csv']
# TARGET1 = txt
# TARGET2 = audio and files
# TARGET3 = images
# TARGET4 = videos

# Loop through the CSV files
df1 = pd.read_csv(filter_list[0])
df2 = pd.read_csv(filter_list[1])
df3 = pd.read_csv(filter_list[2])
df4 = pd.read_csv(filter_list[3])

# Simulated data for different types: txt, images, files, videos
# You would replace this with your actual data
txt_data = df1['Length'].values
files_and_audios_data = df2['Length'].values
images_data = df3['Length'].values
videos_data = df4['Length'].values

# Sort the data in ascending order
txt_data = np.sort(txt_data)
images_data = np.sort(images_data)
files_and_audios_data = np.sort(files_and_audios_data)
videos_data = np.sort(videos_data)

# Calculate the CCDF values for each type
ccdf_txt = 1 - np.arange(1, len(txt_data) + 1) / len(txt_data)
ccdf_images = 1 - np.arange(1, len(images_data) + 1) / len(images_data)
ccdf_files_and_audios = 1 - np.arange(1, len(files_and_audios_data) + 1) / len(files_and_audios_data)
ccdf_videos = 1 - np.arange(1, len(videos_data) + 1) / len(videos_data)

# Normalize x-axis to be between 0 and 1
normalized_txt_data = (txt_data - np.min(txt_data)) / (np.max(txt_data) - np.min(txt_data))
normalized_images_data = (images_data - np.min(images_data)) / (np.max(images_data) - np.min(images_data))
normalized_files_data = (files_and_audios_data - np.min(files_and_audios_data)) / (np.max(files_and_audios_data) - np.min(files_and_audios_data))
normalized_videos_data = (videos_data - np.min(videos_data)) / (np.max(videos_data) - np.min(videos_data))

# Plot the CCDFs with normalized x-axis
plt.loglog(normalized_txt_data, ccdf_txt, 'co', linestyle='-', label='Text')
plt.loglog(normalized_images_data, ccdf_images, '*', color='orange', linestyle='-', label='Images')
plt.loglog(normalized_files_data, ccdf_files_and_audios, 'rs', linestyle='-', label='Files')
plt.loglog(normalized_videos_data, ccdf_videos, 'g^', linestyle='-', label='Videos')

plt.xlabel('Normalized Message Sizes To Their Maximum')
plt.ylabel('Complementary CDF')
plt.title('Complementary CDF for Different Types of messages')
plt.legend()
plt.grid(True)
plt.savefig('res/CCDF_plot.png')
plt.show()