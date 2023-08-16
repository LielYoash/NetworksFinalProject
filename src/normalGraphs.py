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


    if not os.path.exists('../res/Time_Size_results'):
        os.makedirs('../res/Time_Size_results')
    plt.savefig(output_filename)


def main():
    clean_data_files = ['../resources/Clean/TextClean.csv','../resources/Clean/ImageClean.csv','../resources/Clean/VideoClean.csv','../resources/Clean/Audio&FilesClean.csv']
    raw_data_file = ['../resources/Raw/TextRaw.csv','../resources/Raw/ImageRaw.csv','../resources/Raw/VideoRaw.csv','../resources/Raw/Audio&FilesRaw.csv']
    while 1:
        print("To Analyze the Filtered Files press 1\nTo Analyze the Unfiltered Files press 2")
        x =input()
        if x == '1':
            for data_file in clean_data_files:
                dataframe = pd.read_csv(data_file)
                output_file_name = f'../res/Time_Size_results/{os.path.basename(data_file)[:-4]}.png'
                create_and_save_histogram(dataframe, output_file_name)
            break
        elif x == '2':
            for data_file in raw_data_file:
                dataframe = pd.read_csv(data_file)
                output_file_name = f'../res/Time_Size_results/{os.path.basename(data_file)[:-4]}.png'
                create_and_save_histogram(dataframe, output_file_name)
            break
        else:
            print("Wrong Input, Please Try Again.")




if __name__ == "__main__":
    main()
