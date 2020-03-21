#PyPoll Main.py
import os
import csv

election_csv = os.path.join('..', 'Resources', 'election_data.csv')
num_votes = 0
# Read in the CSV file
with open(election_csv, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    candidates = []
    candid_votes = []
    percentage = []
    # Loop through the data
    for row in csvreader:
        # Add to our vote-counter 
        num_votes += 1 
        if row[2] not in candidates:
            candidates.append(row[2])
            index_candid = candidates.index(row[2])
            candid_votes.append(1)
        else:
            index_candid = candidates.index(row[2])
            candid_votes[index_candid] += 1
    #percentage calculation
    for i in candid_votes:
        percent_votes = (i/num_votes) * 100
        percent_votes = int(round(percent_votes))
        percentage.append(percent_votes)

    #Find winner
    winner = max(candid_votes)
    win_candid = candid_votes.index(winner)
    winner_candid = candidates[win_candid]
       
print("Election Results")
print("-"*50)
print(f"Total Votes: {str(num_votes)}")
print("-"*50)
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percentage[i])}% ({str(candid_votes[i])})")
print("-"*50)
print(f"Winner: {winner_candid}")
print("-"*50)


file = open("PyPoll_output.txt","w")
head_line = "Election Results"
dot_line= (f"-"*50)
Votes = (f"Total Votes: {num_votes}")
winner = (f"Winner: {winner_candid}")
file.write(f'{head_line}\n{dot_line}\n{Votes}\n{dot_line}')
for i in range(len(candidates)):
    final = (f"{candidates[i]}: {str(percentage[i])}% ({str(candid_votes[i])})")
    file.write(f'\n{final}')
file.write(f'\n{dot_line}\n{winner}\n{dot_line}\n')