# import helper_code
import matplotlib.pyplot as plt
import numpy as np, scipy as sp, pandas as pd, scipy.stats, os, sys
from scipy.io import wavfile


training_data_info = pd.read_csv('Dataset\\training_data.csv')
# print(training_data_info.info())
# list(training_data_info)
# print(training_data_info.columns)
# print(training_data_info.iloc[0,:])
# print(training_data_info.head(4)) # prints the first 4 rows of the dataframe.
#print(training_data_info['PatientID'])
for index, row in training_data_info.iterrows():
    if row['Murmur'] == 'Present':
        # print(index)
        # print(row['PatientID'])
        directoryData = str('Dataset\\training_data\\')
        directoryData = directoryData + (str(row['PatientID'])) + '*'+ str('.wav')
        print(directoryData)
        # samplerate, data = wavfile.read(directoryData)        
        # plt.plot(data)
        # plt.show()
        # plt.show(data)
# samplerate, data = wavfile.read('G:\\Shared drives\\Physionet 2022\\Dataset\\training_data\\9979_AV.wav')        
# plt.plot(data)
# plt.show()

    


# indexes = training_data_info.index
# sample = training_data_info.loc[[1]]
# print(indexes)

# for index,row in training_data_info.iterrows():
    

