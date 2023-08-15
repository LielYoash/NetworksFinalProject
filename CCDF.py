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

    plt.savefig(output_filename)
    plt.show()


def main():
    filter_list = ['csvs/Audio&FilesNonClean.csv', 'csvs/ImageNonClean.csv',
                   'csvs/TextNonClean.csv', 'csvs/VideoNonClean.csv']

    dataframes = [pd.read_csv(file) for file in filter_list]
    labels = ['Text', 'Images', 'Files', 'Videos']
    markers = ['co', '*', 'rs', 'g^']

    output_file_name = 'CCDF_results/CCDF_NonClean.png'
    create_and_save_ccdf_plot(dataframes, labels, markers, output_file_name)


if __name__ == "__main__":
    main()
