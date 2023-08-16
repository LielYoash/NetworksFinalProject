import matplotlib.pyplot as plt
import pandas as pd
import os
import matplotlib

matplotlib.use("TkAgg")


def create_and_save_histogram(dataframe, output_filename):
    plt.figure(figsize=(10, 6))
    plt.bar(dataframe['Time'], dataframe['Length'], color='black', width=0.3)
    plt.xlabel('Time (seconds)')
    plt.ylabel('Size (bytes)')
    plt.title('Bar Histogram: Time vs. Size')

    plt.xticks(range(0, 91, 30))  # Adjust x-axis ticks to every 30 seconds
    plt.yticks(range(0, 6001, 500))  # Adjust y-axis ticks to every 500 bytes

    if not os.path.exists('res'):
        os.makedirs('res')
    plt.savefig(output_filename)
    plt.show()


def main():
    data_file = 'FileAudioTCP.csv'
    dataframe = pd.read_csv(data_file)

    output_file_name = f'res/{os.path.basename(data_file)[:-4]}.png'
    create_and_save_histogram(dataframe, output_file_name)


if __name__ == "__main__":
    main()