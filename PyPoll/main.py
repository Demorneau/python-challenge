import os
import csv
# Importing the path os and the csv routine 
from operator import itemgetter
# Importing the item getter for the dictionary sort_list
poll_data = os.path.join("election_data.csv")
with open(poll_data, newline = "") as csv_data_file:
    csv_header = next(csv_data_file)
    # not using the header of the election data file
    data_list = list(csv.reader(csv_data_file))
    # Placing election data into a list
    length_data = len(data_list)
    # Calculating the number of data in a column
sort_list = {}
sort_list = sorted(data_list,key=itemgetter(2))
# Selecting data into a dictionary where the candidate names are located and sorting the name in alphabetical order
candidate_name = sort_list[0][2]
#initializing counters to move along the rows (line counter) and  initializing vote counter to add them per candidate.
line_counter = 0
vote_counter = 0
sum_votes = 0
# Adding the votes per candidate
results_list = []
# Creating an empty list to place all results of the analysis
for line_counter in range(0,length_data,1):
    # Across the rows of data comparing the name of the condidate, if the name does not change then counting the votes.
    if candidate_name == sort_list[line_counter][2]:
        vote_counter = vote_counter + 1
    else:
        # When the candidate name changes, taking the new name to add his/her votes. As well as adding results to our list
        results_list.append(candidate_name)
        results_list.append(vote_counter)
        candidate_name = sort_list[line_counter][2]
        sum_votes = sum_votes + vote_counter
        vote_counter = 1
results_list.append(candidate_name)
results_list.append(vote_counter)
sum_votes = sum_votes + vote_counter
# Verifying the number of total votes 
print("total votes", sum_votes)
length_results = len(results_list)
print("Candidate    Votes   % of Total Votes")
# Calculating the percentage of votes per candidates and who has more votes is the winner!
cntr = 0
winner_name = ""
for j in range(0,length_results,2):
    percent = (float(results_list[j+1]/length_data))
    if percent > cntr:
        cntr = percent
        winner_name = results_list[j]
    print(results_list[j],results_list[j+1], "{:.3%}".format(percent))
print("And the winner is  ", winner_name)
# To write in a csv file
with open('electiondata_analysisresults.csv','w', newline = '') as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(["Candidate","\t","Votes","\t","Percent/Votes"])
    for j in range(0,length_results,2):
        csvwriter.writerow([results_list[j],"\t", results_list[j+1],"\t", "{:.3%}".format(percent)])
    csvwriter.writerow(["Winner name", winner_name])
    csvwriter.writerow(["Total of votes", sum_votes])