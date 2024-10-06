import csv
import os

filename = "C:\Temp\EggPlant Training\C2ImportCalEventSample.csv"
#filename = "C:\Temp\EggPlant Training\PatientInformation.csv"

def file_is_empty(filename):
    return os.stat(filename).st_size==0


#initializing column name and row
rows =[]
fields =[]

#reading csv file

with open(filename,'r') as csvfile:
    #create reader object
    csvreader = csv.reader(csvfile)
    #extracting field name
    if not file_is_empty(filename):
        fields = csvreader.__next__()
    

        for row in csvreader:
            rows.append(row)
        print("Total no of lines: %d"%(csvreader.line_num))    

        print("field  names are"+','.join(field  for field in fields))

        print('\n Rows values are:\n')
        for row in rows[:csvreader.line_num]:
            # parsing each column of a row
            #for col in row:        
            print(' '.join(col for col in row))
            
            print('\n')
    else:
        print("File is empty")

     
  
