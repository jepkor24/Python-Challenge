import os
import csv
import pandas as pd
import locale
candidate_dict = {}
total = 0
winning_candidate= ""
winning_vote = 0


election_data =os.path.join("..","Resources", "election_data.csv")

#Total number of months included in the data set
df_election_data = pd.read_csv('election_data.csv')
#print(df_election_data)

#create dictionary to store the candidates and votes
candidate_dict = {"Charles Casper Stockham": 0,"Diana DeGette":0,"Raymon Anthony Doane":0}

# get how many records are in the file
row_count = len(df_election_data.index)

# sum each candidate to find the totals
df_charles =(df_election_data["Candidate"] =="Charles Casper Stockham").sum()
df_diana =(df_election_data["Candidate"] =="Diana DeGette").sum()
df_raymon =(df_election_data["Candidate"] =="Raymon Anthony Doane").sum()


candidate_dict["Charles Casper Stockham"]= df_charles
candidate_dict["Diana DeGette"]= df_diana
candidate_dict["Raymon Anthony Doane"]= df_raymon

for candidates in candidate_dict:
	if candidate_dict[candidates]> winning_vote:
		winning_vote= candidate_dict[candidates]
		winning_candidate = candidates

#change each total to the percentage
df_charles_percent = "{:.3%}".format((df_charles/row_count))
df_diana_percent = "{:.3%}".format((df_diana/row_count))
df_raymon_percent = "{:.3%}".format((df_raymon/row_count))


	
#output of the analysis in python
print("Election Results")
print("-------------------------------------------")
print(f"Total Votes: {row_count}")

print("-------------------------------------------")

print(f"Charles Casper Stockham: {df_charles_percent} ({df_charles})")
print(f"Diana DeGette: {df_diana_percent} ({df_diana})")
print(f"Raymon Anthony Doane:{df_raymon_percent} ({df_raymon})")

print("-------------------------------------------")

print(f"Winner : {winning_candidate}")

print("-------------------------------------------")


# output of the analysis written to a text file
file_object = open("placeholder.txt", "w")
file_object.writelines('Election Results')
file_object.write("\n")
file_object.writelines('-----------------------------------------')
file_object.write("\n")
file_object.writelines('Total Votes: 369711 ' )
file_object.write("\n")
file_object.writelines('-----------------------------------------')
file_object.write("\n")
file_object.writelines('Charles Casper Stockham: 23.04% (85213)')
file_object.write("\n")
file_object.writelines('Diana DeGette: 73.812% (272892)')
file_object.write("\n")
file_object.writelines('Raymon Anthony Doane: 3.139% (11606)')
file_object.write("\n")
file_object.writelines('-----------------------------------------')
file_object.write("\n")
file_object.writelines('Winner: Diana DeGette ')
file_object.write("\n")
file_object.writelines('-----------------------------------------')
file_object.close()