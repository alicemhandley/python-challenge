import os
import csv

# set up data path
csv_path = os.path.join('Resources', "election_data.csv")

# create lists to hold variables 
candidates = []
number_votes = []
percentage_votes = []

# set counter for the total number of votes
total_votes = 0

#read csv file
with open(csv_path, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    # read header row
    csv_header = next(csv_reader)

    for row in csv_reader:
        # add to total number of votes counter
        total_votes += 1
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            number_votes.append(1)
        else:
            index = candidates.index(row[2])
            number_votes[index] += 1
            # 'Github ermaisgelaye

    # add to percentage of votes
    for votes in number_votes:
        percentage = round((votes/total_votes) * 100, 2)
        percentage_votes.append(percentage)       

    winner = max(number_votes)
    index = number_votes.index(winner)
    election_winner = candidates[index]

# print results
print("Election Results")
print("------------------------------")
print(f"Total Votes: {str(total_votes)}")
print("------------------------------")

for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percentage_votes[i])}% ({str(number_votes[i])})") 
print("------------------------------")
print(f"Winner: {election_winner}")    
print("------------------------------")

# export results to text rile

output_path = os.path.join("output", "PyPoll_output.txt")

PyPoll_output = open(output_path, "w")

line1 = "Election Results"
line2 = "------------------------------" 
line3 = str(f"Total Votes: {str(total_votes)}")
line4 = "------------------------------"
PyPoll_output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range(len(candidates)):
    line = str(
        f"{candidates[i]}: {str(percentage_votes[i])} ({str(number_votes[i])})")
    PyPoll_output.write('{}\n'.format(line))
line5 = "------------------------------"
line6 = str(f"Winner: {election_winner}")
line7 = "------------------------------"
PyPoll_output.write('{}\n{}\n{}\n'.format(line5, line6, line7))

