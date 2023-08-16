import os
import warnings
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

warnings.filterwarnings('ignore')
matplotlib.use("TkAgg")


def create_and_save_ccdf_plot(dataframes, labels, markers, output_filename):
    plt.figure(figsize=(10, 6))

    for df, label, marker in zip(dataframes, labels, markers):
        data = np.sort(df['Length'].values)
        ccdf = 1 - np.arange(1, len(data) + 1) / len(data)
        normalized_data = (data - np.min(data)) / (np.max(data) - np.min(data))
        plt.loglog(normalized_data, ccdf, marker, linestyle='-', label=label)

    plt.xlabel('Normalized Message Sizes To Their Maximum')
    plt.ylabel('Complementary CDF')
    plt.title('Complementary CDF for Different Types of Messages')
    plt.legend()
    plt.grid(True)

    if not os.path.exists('CCDF_results'):
        os.makedirs('CCDF_results')
    plt.savefig(output_filename)
    plt.show()


def main():
    filtered_list = ['../resources/Clean/TextClean.csv', '../resources/Clean/ImageClean.csv',
                   '../resources/Clean/VideoClean.csv', '../resources/Clean/Audio&FilesClean.csv']

    unfiltered_list = ['../resources/Raw/TextRaw.csv', '../resources/Raw/ImageRaw.csv',
                   '../resources/Raw/VideoRaw.csv', '../resources/Raw/Audio&FilesRaw.csv']

    while 1:
        print("To Analyze the Filtered Files press 1\nTo Analyze the Unfiltered Files press 2\n")
        x =input()
        if x == '1':
            dataframes = [pd.read_csv(file) for file in filtered_list]
            labels = ['Text', 'Images', 'Files', 'Videos']
            markers = ['co', '*', 'rs', 'g^']
            output_file_name = '../res/CCDF_results/CCDF_Clean.png'
            create_and_save_ccdf_plot(dataframes, labels, markers, output_file_name)
            break
        elif x == '2':
            dataframes = [pd.read_csv(file) for file in unfiltered_list]
            labels = ['Text', 'Images', 'Files', 'Videos']
            markers = ['co', '*', 'rs', 'g^']
            output_file_name = '../res/CCDF_results/CDF_Raw'
            create_and_save_ccdf_plot(dataframes, labels, markers, output_file_name)

            break
        else:
            print("Wrong Input, Please Try Again.")


if __name__ == "__main__":
    main()
