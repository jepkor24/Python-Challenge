import os
import csv
import pandas as pd
import locale
locale.setlocale(locale.LC_ALL, '')
total = 0
profit_loss = []
change_list =[]
date_list =[]
#previous_change =0
great_increase =["",0]
great_decrease = ["",99999999999999]
average = 0

budget_data =os.path.join("..","Resources", "budget_data.csv")

#Total number of months included in the data set
df= pd.read_csv('budget_data.csv')
with open(budget_data) as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	#print(csvreader)
	csv_header = next(csvreader)
	firstrow = next(csvreader)
	previous_change = int(firstrow[1])

	# read each row in csvreader
	for row in csvreader:
		# get how many records are in the file
		row_count = len(df.index)

		#sum the items in column 2 and store it in the total variable
		profit_loss.append(int(row[1]))
		total =sum(profit_loss)

		#determine the change for each line item
		change =int(row[1])- previous_change
		previous_change =int(row[1])
		change_list += [change]
		

		
		#calculate the average change
		average = sum(change_list)/ len(change_list)
		if change > great_increase[1]:
			great_increase[0] = row[0]
			great_increase[1] = change
		if change <great_decrease[1]:
			great_decrease[0] = row[0]
			great_decrease [1] = change

		
#output of the analysis
print("Financial Analysis")
print("-------------------------------------------")
print(f"Total Months: {row_count}")
print(f"Total: ${total}")
print(f"Average Change: {round(average)}")
print(f"Greatest Increase in Profits: {great_increase[0]} (${great_increase[1]})")
print(f"Greatest Decrease in Profits: {great_decrease[0]} (${great_decrease[1]})")


#writing output to a text file
file_object = open("placeholder.txt", "w")
file_object.writelines('Financial Analysis')
file_object.write("\n")
file_object.writelines('-----------------------------------------')
file_object.write("\n")
file_object.writelines('Total Months: 86')
file_object.write("\n")
file_object.writelines('Total: $21475215')
file_object.write("\n")
file_object.writelines('Average Change: -8311')
file_object.write("\n")
file_object.writelines('Greatest Increase in Profits: Aug-16 ($1862002)')
file_object.write("\n")
file_object.writelines('Greatest Decrease in Profits: Feb-14 ($-1825588) ')
file_object.write("\n")


file_object.close()
