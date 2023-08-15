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
    plt.yticks(range(0, 1501, 500))  # Adjust y-axis ticks to every 500 bytes

    if not os.path.exists('res'):
        os.makedirs('res')
    plt.savefig(output_filename)
    plt.show()


def process_data_files(data_files):
    for data_file in data_files:
        dataframe = pd.read_csv(data_file)

        output_file_name = f'res/{os.path.basename(data_file)[:-4]}.png'
        create_and_save_histogram(dataframe, output_file_name)


def main():
    data_files = ['TextClean.csv','TextNonClean','ImageClean.csv', 'ImageNonClean','VideoClean.csv','VideoNonClean','' ]  # List of filtered data files
    process_data_files(data_files,)


if __name__ == "__main__":
    main()
