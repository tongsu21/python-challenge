import csv
import os

budget_csv = os.path.join("budget_data.csv")

change = 0
totalChange = 0
counter = 0
totalProfitLoss = 0
previousProfitLoss = 0
rowProfitLoss = 0
greatestIncrease = 0
greatestDecrease = 0

# Open and read csv
with open(budget_csv) as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")

	# Read the header row
	csv_header = next(csvfile) 
	
	for row in csvreader:
		if counter >= 1:
			previousProfitLoss = rowProfitLoss
			rowProfitLoss = int(row[1])
			# The net total amount of "Profit/Losses" over the entire period
			totalProfitLoss += int(row[1])
			change = rowProfitLoss - previousProfitLoss
			if change > 0:
				# The greatest increase in profits (date and amount) over the entire period
				if change > greatestIncrease:
					greatestIncreaseDate = str(row[0])
					greatestIncrease = change
			else:
				# The greatest decrease in losses (date and amount) over the entire period
				if change < greatestDecrease:
					greatestDecreaseDate = str(row[0])
					greatestDecrease = change

			# The average of the changes in "Profit/Losses" over the entire period
			totalChange = totalChange + change
		else:
			rowProfitLoss = int(row[1])
			totalProfitLoss += int(row[1])
		# The total number of months included in the dataset
		counter = counter + 1


	print("Total Months: " + str(counter))
	print("Total: $" + str(totalProfitLoss))
	print("Average Change: $" + str(round(totalChange/(counter - 1), 2)))
	print("Greatest Increase in Profits: " + greatestIncreaseDate + "($" + str(greatestIncrease) + ")")
	print("Greatest Decrease in Profits: " + greatestDecreaseDate + "($" + str(greatestDecrease) + ")")


f = open('workfile', 'w')
f.write('Total Months: ' + str(counter) + '\n')
f.write('Total: $' + str(totalProfitLoss) + '\n')
f.write('Average Change: $' + str(round(totalChange/(counter - 1), 2)) + '\n')
f.write('Greatest Increase in Profits: ' + greatestIncreaseDate + '($' + str(greatestIncrease) + ')\n')
f.write('Greatest Decrease in Profits: ' + greatestDecreaseDate + '($' + str(greatestDecrease) + ')\n')
f.close()

