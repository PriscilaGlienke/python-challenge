#importing the modules necessary

import os
import csv

#defining the path of the file to open
data_csv = os.path.join("Challenge instructions","PyBank/Resources","budget_data.csv")

#defining the veariables
months = 0
profit_losses = 0
previous_pl = 0
change_pl = 0
changes = []

greatest_increase = ["",0]
greatest_decrease = ["", 999999999]

#reading through the data
with open(data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader) #making sure we skip the first row - header

#calculating the months, profit ans losses and its changes over the entire period in the file by looping through the file
    for row in csvreader:
        months = months + 1 
        profit_losses = profit_losses + int(row[1])
        change_pl = int(row[1]) - previous_pl
        changes.append(change_pl) #adding each change to the list created for all changes
        previous_pl = int(row[1])

#using if function to define the greatest increase and decrease
        if change_pl > greatest_increase[1]: 
            greatest_increase[0] = row[0]
            greatest_increase[1] = change_pl

        if change_pl < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = change_pl

#calculating the average of the above changes using the sum and the len of the list of changes
average = round(sum(changes)/len(changes),2)

#printing the results 
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {months}")
print(f"Total: ${profit_losses}")
print(f"Average Change: ${average}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

#exporting to a text file
output_file = os.path.join("python-challenge", "PyBank", "analysis", "PyBank_analysis.txt")
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Financial Analysis"])
    writer.writerow(["----------------------------"])
    writer.writerow([f"Total Months: {months}"])
    writer.writerow([f"Total: ${profit_losses}"])
    writer.writerow([f"Average Change: ${average}"])
    writer.writerow([f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})"])
    writer.writerow([f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})"])