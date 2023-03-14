#importing the necessary modules 
import os
import csv

#defining the path
filepath = os.path.join ("Challenge instructions","PyPoll/Resources","election_data.csv")

#defining the variables
total_votes = 0
candidates = []
votes = {}

winner = ""
winner_votes = 0

#opening the file to read it and looping through it with the appropriate functions
with open (filepath) as csvfile:
    csv_reader = csv.reader(csvfile,delimiter=",")
    next(csv_reader)

    for row in csv_reader:
        total_votes = total_votes + 1
        candidate = row[2]

        if candidate not in candidates:
            candidates.append(candidate)
            votes[candidate] = 0

        votes[candidate] = votes[candidate] + 1

#printing the analysis
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")


#calculating the percentage of votes
for candidate in candidates:
    vote_count = votes[candidate]
    vote_percentage = round(vote_count / total_votes * 100, 3)
    print(f"{candidate}: {vote_percentage}% ({vote_count})")

print("-------------------------")

#found the formula for the winner with the help of ChatGPT
winner = max(votes, key=votes.get)
print(f"Winner: {winner}")
print("-------------------------")

#exporting the results as a text file

output_path = os.path.join("python-challenge", "PyPoll", "analysis", "PyPoll_analysis.txt")
with open(output_path, "w") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Election Results"])
    writer.writerow(["----------------------------"])
    writer.writerow([f"Total Votes: {total_votes}"])
    writer.writerow(["----------------------------"])

    for candidate in candidates:
        vote_count = votes[candidate]
        vote_percentage = round(vote_count / total_votes * 100, 3)
        writer.writerow([f"{candidate}: {vote_percentage}% ({vote_count})"])
    
    writer.writerow(["----------------------------"])
    winner = max(votes, key=votes.get)
    writer.writerow([f"Winner: {winner}"])
    writer.writerow(["----------------------------"])
