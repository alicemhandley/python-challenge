import os
import csv

#path to data file
budget_data = os.path.join('Resources', 'budget_data.csv')


# read csv file
with open(budget_data) as csvfile:
    # CSV reader specifies delimiter and variable 
        csv_reader = csv.reader(csvfile, delimiter=',')
    #read header
    csv_header = next(csvfile)

# Read the header row first
csv_header = next(csv_file)
print(f"Header: {csv_header}")
