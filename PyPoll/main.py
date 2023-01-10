# Import dependencies

import csv

# load data 
election_data_csv =  "Resources/election_data.csv"
election_analysis = "analysis/pypoll_output.txt"

# Define variables
total_votes = 0 
votes_per_candidate = {}

# open folder 

with open(election_data_csv, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)
    
    # For each row 
    for row in csvreader:
        total_votes += 1

        if row[2] not in votes_per_candidate:
            votes_per_candidate[row[2]] = 1
        else:
            votes_per_candidate[row[2]] += 1   
        
        
print("Election Results")
print("----------------------")
print("Total Votes: " + str(total_votes))
print("-----------------------------")

for candidate, votes in votes_per_candidate.items():
    print(candidate + ": " + "{:.3%}".format(votes/total_votes) + "   (" +  str(votes) + ")")
    
print("-------------------------------") 

winner = max(votes_per_candidate, key = votes_per_candidate.get)

print(f"Winner: {winner}")

# export a text file with the results 
with open(election_analysis, "w") as outfile:
    outfile.write("Election Results")
    outfile.write('\n')
    outfile.write("--------------------")
    outfile.write('\n')
    outfile.write("Total Votes: " + str(total_votes))
    outfile.write('\n')
    outfile.write("--------------------------")
    outfile.write('\n')
    outfile.write(candidate + ": " + "{:.3%}".format(votes/total_votes) + "   (" +  str(votes) + ")")
    outfile.write('\n')
    outfile.write("-------------------------") 
    outfile.write('\n')
    outfile.write(f"Winner: {winner}")
    outfile.write('\n')
