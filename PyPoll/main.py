# PyPoll

# You will be give a set of poll data called election_data.csv
# The dataset is composed of three columns: Voter ID, County, and Candidate.
# Your task is to create a Python script that analyzes the votes and calculates each of the following:

#Import lIbratires

import os
import csv

# Start Under PyPoll folder
csvpath = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')

# Create list
names = []


# set variables

total_votes = 0
c_votes = 0
k_votes = 0
l_votes = 0
o_votes = 0

# Let's open the file
with open(csvpath, 'r') as election_data:
    Pypoll = csv.reader(election_data, delimiter=',')
    next(Pypoll)

    
    # Obtain names
    #The total number of votes cast
    for row in Pypoll:
        total_votes = total_votes + 1
        #store Data in list
        names.append(row[2])


# obtain names from list
unique_candidate = []
[unique_candidate.append(name) for name in names if name not in unique_candidate]

#being loop
# obtain The percentage of votes each candidate won  
# obtain names in list and get count for each through loop
# obtain The total number of votes each candidate won
for name in names:
    if name == "Khan":
        k_votes = k_votes + 1
        k_percent = "{:.00%}".format(k_votes / total_votes)
    if name == "Correy":
        c_votes = c_votes + 1
        c_percent = "{:.00%}".format(c_votes / total_votes)
    if name == "Li":
        l_votes = l_votes + 1
        l_percent = "{:.00%}".format(l_votes / total_votes)
    if name == "O'Tooley":
        o_votes = o_votes + 1
        o_percent = "{:.00%}".format(o_votes / total_votes)

#Create List
candidates = {
    "Correy":c_votes,
    "Khan":k_votes,
    "Li":l_votes,
    "O'Tooley":o_votes,
}

# The winner of the election based on popular vote.


#PRINT

print(f"""

          Election Results!
--------------------------------------
        Total Votes: {total_votes}
--------------------------------------
      Khan:     {k_percent}  ({k_votes})
      Correy:   {c_percent}   ({c_votes})
      Li:       {l_percent}   ({l_votes})
      O'Tooley:  {o_percent}   ({o_votes})
--------------------------------------
           Winner: {max(candidates, key=candidates.get)}
--------------------------------------
""")

#create .txt file and export

with open("election_results.txt", 'w') as results:
    results.write("Election Results!\n")
    results.write("--------------------------------------\n")
    results.write(f"Total Votes: {total_votes}\n")
    results.write("--------------------------------------\n")
    results.write(f"Khan:     {k_percent}  ({k_votes})\n")
    results.write(f"Correy:   {c_percent}   ({c_votes})\n")
    results.write(f"Li:       {l_percent}   ({l_votes})\n")
    results.write(f"O'Tooley:  {o_percent}   ({o_votes})\n")
    results.write("--------------------------------------\n")
    results.write(f"Winner: {max(candidates, key=candidates.get)} \n")
    results.write("--------------------------------------\n")
