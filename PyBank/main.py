# PyBank -budget_data.csv analysis of minimum value, maximun value, sum total, and average.
#importing sub-routines for path and csv reader and writer files.
import os
import csv
# Establishing dictionary Bank for data information, and setting counters in zero value.
dictionary_bank = {}
min_pl = 0
max_pl = 0
average_pl = 0
total_pl = 0
# Calling data budget as budget as csv file also reading the csv file with comma as delimiter including the instruction to skip
# header and have just data to work in line 16, line 17 to place data budget into a list, and 18 to estimate the number of rows to work with.
budget_csv = os.path.join("budget_data.csv")
with open(budget_csv, newline = "") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvfile)
    data_list = list(csv.reader(csvfile))
    length_data = len(data_list)
    # Placing data in dictionary, so we can access the date when finding the target values (max, min)
    for i in range(length_data):
        dictionary_bank[data_list[i][1]] = data_list[i][0]
        
# Data placed in dictionary as key, will be used to find target values in a list.
pl_list = list(dictionary_bank.keys())

# Dictionary hold objects so to calculate our column of profit/loss shall be numbers
for i in range(length_data):
    pl_list[i] = float(pl_list[i])

# Calculations
max_pl = (max(pl_list))
max_pls = str(max_pl)
# After calculationg the maximun value in the budget we will transform that value into string and take the decimals off to
# locate the corresponding date in the dictionary bank.
max_pls_short = "{:.0f}".format(max_pl)
# Minimun value in budget data file with string transformation and taking the decimal off.
min_pl = (min(pl_list))
min_pls = str(min_pl)
min_pls_short = f"{min_pl:.0f}"

# Calculating the total as sum of profit/loss and the average value.
pl_list_sum = 0
for i in range(length_data):
    pl_list_sum = pl_list_sum + pl_list[i]
    
average_pl = (pl_list_sum/length_data)
average_pl_short = f"{average_pl:.2f}"

# Finding in the dictionary the metching date for the maximun and minimum profit/loss column.
date_max_value = dictionary_bank.get(max_pls_short)
date_min_value = dictionary_bank.get(min_pls_short)
# Placing results into a list
results_list = []
results_list.append("Financial Analysis for PyBank, ")
results_list.append("Total of months: ")
results_list.append(length_data)
results_list.append(", Total amount: $")
results_list.append(pl_list_sum)
results_list.append(", Average Change: $")
results_list.append(average_pl_short)
results_list.append(", Greatest Increase in Profit: $")
results_list.append(max_pl)
results_list.append(" on ")
results_list.append(date_max_value)
results_list.append(", Greatest Decrease in Profit: $")
results_list.append(min_pls_short)
results_list.append(" on  ")
results_list.append(date_min_value)
print("".join(str(x) for x in results_list))
          
# Print into a csv file
import csv
with open('BankData_Analysis.csv','w',newline = "") as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(["".join(str(x) for x in results_list)])
    