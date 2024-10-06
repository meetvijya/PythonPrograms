import csv 

filename = "C:\Temp\EggPlant Training\PatientInformation.csv"

#initializing column name and row
rows =[]
fields =[]

#reading csv file

with open(filename,'r') as csvfile:
    #create reader object
    csvreader = csvfile.read(csvfile)
     # extracting field name
    fields = csvreader.__next__()

    for row in csvreader:
        rows.append(row)
    print("Total no of lines %d"%(csvreader.line_num))    
    
print("field  names are"+','.join(field  for field in fields))

for row in rows[:5]:
    for col in rows:
        print("Value is %s"%col)
    print('\n')    
 
