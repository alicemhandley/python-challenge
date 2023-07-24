import os
import csv

#path to csv file
data_path=os.path.join('Resources', 'budget_data.csv')

# set counters for variables
total_months = 0
total_profit_loss = 0
# counters for profit and loss output
amount = 0
change = 0
# list for date of output
date = []
# list for porfit and loss output
profits = []


# read csv file 
with open(data_path, newline="") as csvfile:
    # CSV reader specifies delimiter and variable 
    csv_reader = csv.reader(csvfile, delimiter=',')
    #read header
    csv_header = next(csv_reader)
    # start at first row
    row_one = next(csv_reader)
    #'from gitlab

    # count rows
    total_months += 1

    # count profit and loss
    total_profit_loss += int(row_one[1])
    amount = int(row_one[1])

    # continue reading rows
    for row in csv_reader:

        # the date is
        date.append(row[0])

        # change in profit and loss
        change = int(row[1])-amount
        profits.append(change)
        amount = int(row[1])

        # total months
        total_months += 1

        # calculate the net sum of profit/loss
        total_profit_loss = total_profit_loss + int(row[1])

        # calculate average change of profit/loss 
        ave_change = sum(profits)/len(profits)

    # greatest increase in profits
    greatest_increase = max(profits)    
    index_greatest_increase = profits.index(greatest_increase)
    date_greatest_increase = date[index_greatest_increase]

    # greatest decrease in profits
    greatest_decrease = min(profits)
    index_greatest_decrease = profits.index(greatest_decrease)
    date_greatest_decrease = date[index_greatest_decrease]

# print output analysis

printoutput = (
    f"Financial Analysis\n"
    f"----------------------\n"
    f"Total Months: {str(total_months)}\n"
    f"Total: ${str(total_profit_loss)}\n"
    f"Average Change: ${str(round(ave_change,2))}\n"
    f"Greatest Increase in Profits: {date_greatest_increase} (${str(greatest_increase)})\n"
    f"Greatest Decrease in Profits: {date_greatest_decrease} (${str(greatest_decrease)})\n")
print(printoutput)

# export results to text file

output_path = os.path.join("output", "PyBank_output.txt")

PyBank_output = open(output_path, "w")

PyBank_output.write(printoutput)

