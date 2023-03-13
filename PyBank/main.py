import os
import csv

data_csv = os.path.join("Challenge instructions","PyBank/Resources","budget_data.csv")

months = 0
profit_losses = 0
previous_pl = 0
change_pl = 0
changes = []

greatest_increase = ["",0]
greatest_decrease = ["", 999999999]

with open(data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)

    for row in csvreader:
        months = months + 1
        profit_losses = profit_losses + int(row[1])
        change_pl = int(row[1]) - previous_pl
        changes.append(change_pl)
        previous_pl = int(row[1])

        if change_pl > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = change_pl

        if change_pl < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = change_pl


average = sum(changes)/len(changes)

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {months}")
print(f"Total: ${profit_losses}")
print(f"Average Change: ${average:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

output_file = os.path.join("python-challenge", "PyBank", "analysis", "PyBank_analysis.txt")
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)
    writer.writerow("Financial Analysis")
    writer.writerow("----------------------------")
    writer.writerow(f"Total Months: {months}")
    writer.writerow(f"Total: ${profit_losses}")
    writer.writerow(f"Average Change: ${average:.2f}")
    writer.writerow(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
    writer.writerow(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")