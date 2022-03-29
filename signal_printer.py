# import helper_code
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import pandas as pd
import scipy.stats
import os
import sys
from scipy.io import wavfile
import scipy.fftpack
from glob import glob

## Functions
"""
All the functions are defined here
"""
def signal_printer_murmur_present(data_info, directoryData):
    """
    This function takes a signal and plots it
    data_info is the variable containing all the information about the signal should be a pandas dataframe.
    the directoryData is the directory where the signal files are stored (in this case it is **.wav and other files) 
    """
    for index, row in data_info.iterrows(): # data_info contains all of the infos related to the dataset
        if row['Murmur'] == 'Present':
            # print(index)
            # print(row['PatientID'])
            # directoryData = str('Dataset\\training_data\\') # windows
            # directoryData = str(data_set_directory)

            # list of files in the current directory
            list_of_files = os.listdir(directoryData)
            recording_File_ID = str(row['PatientID'])
            file_format = '.wav'
            for each_file in list_of_files:
                # if recording_File_ID in each_file and file_format in each_file: print(each_file)
                if recording_File_ID in each_file and file_format in each_file:  # the files in the dataset are stored with the patientID (the files name contains the patientID). So here the ones containing the patient ID and have the .wav format are selected.
                    print(each_file) # prints the file name related to the patients with Murmer = present and having the formate of .wav
                    samplerate, data = wavfile.read(directoryData + each_file) # reads the .wav file
                    data = np.array(data) # convert it to numpy array
                    # print(data[1:200])
                   
                    plt.figure(figsize=(10, 5))
                    plt.plot(data[1:200])
                    plt.xlabel('Time [sampling]')
                    plt.ylabel('Amplitude')
                    plt.title('Recording (1:200)')
                    plt.savefig(recording_File_ID)
                    # plt.show()
                    plt.show()
                    for ii in range(0, len(data), 2000):
                        yf = scipy.fftpack.fft(data[ii:ii+2000])
                        plt.figure(figsize=(10, 5))
                        plt.plot(yf)
                        # xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
                        # fig, ax = plt.subplots()
                        # ax.plot(xf, 2.0/N * np.abs(yf[:N//2]))
                        plt.show()

                        

                

    return
###


training_data_info = pd.read_csv('Dataset\\training_data.csv') # Windows
# training_data_info = pd.read_csv('/Volumes/GoogleDrive/Shared drives/Physionet 2022/Dataset - Copy/training_data.csv')  # MAc
print(training_data_info.info())
list(training_data_info)
# print(training_data_info.columns)
# print(training_data_info.iloc[0,:])
# print(training_data_info.head(4)) # prints the first 4 rows of the dataframe.
# print(training_data_info['PatientID'])
signal_printer_murmur_present(training_data_info, str('Dataset\\training_data\\'))

