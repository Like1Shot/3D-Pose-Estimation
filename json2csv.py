import os
import json 
import csv

directory = 'files'

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        print(f)

    with open(filename) as json_file:
        json_data = json.load(json_file)

        joint_data = json_data['joints']

        data_file  = open('', 'w')
        csv_writer = csv.writer (data_file)

        for i in range(len(joint_data)):
            csv_writer.writerow(joint_data[i])
        
        data_file.close()