import os
import csv

#path to data file
budget_data = os.path.join('Resources', 'budget_data.csv')

with open(budget_data) as csvfile:
    
    csv_reader = csv.reader(csvfile, delimiter=',')
    #read header
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")
           
