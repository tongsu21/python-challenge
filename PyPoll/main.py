import csv
import os

poll_csv = os.path.join("election_data.csv")

totalVotes = 0
candidateDict = {}
highestVote = 0

f = open('workfile', 'w')

# Open and read csv
with open(poll_csv) as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")

	# Read the header row
	csv_header = next(csvfile) 
	
	for row in csvreader:
		# The total number of votes
		totalVotes = totalVotes + 1
		candidate = row[2]
		# Dictonary of candidate and votes
		if candidate in candidateDict.keys():
			#The total number of votes each candidate won
			candidateDict[candidate] += 1
		else:
			candidateDict[candidate] = 1
	print("Election Results")
	print("-------------------------------")
	print("Total Votes: " + str(totalVotes))
	print("-------------------------------")
	f.write("Election Results\n")
	f.write("-------------------------------\n")
	f.write("Total Votes: " + str(totalVotes)+ ')\n')
	f.write("-------------------------------\n")

	#total number of votes for each candidate
	for candidate in candidateDict:
		#The percentage of votes each candidate won
		votePercent = (candidateDict[candidate])/(totalVotes) * 100
		print(str(candidate) + ": " + str(round(votePercent, 2)) + "% (" + str(candidateDict[candidate]) + ")")
		f.write(str(candidate) + ": " + str(round(votePercent, 2)) + "% (" + str(candidateDict[candidate]) + ")\n")
		#The winner of the election based on popular vote.
		if candidateDict[candidate] > highestVote:
			highestVoted = candidate
			highestVote = candidateDict[candidate]
	
	
	# The winner of the election based on popular vote.
	print("-------------------------------")
	print("Winner: " + str(highestVoted))
	print("-------------------------------")
	f.write("-------------------------------\n")
	f.write("Winner: " + str(highestVoted)+ '\n')
	f.write("-------------------------------\n")
	f.close()