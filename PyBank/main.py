# Import OS for file path
import os

# import csv module to read .csv file
import csv

# start under PyBank folder
csvpath = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

# create lists to store data
months =  []
profit_loss = []
profit_change = []

# clasify variables
month_count = 0
total_profit_loss = 0
intial_price = 0

# Module for readingn csv files
with open(csvpath, 'r') as budget_file:
    csvreader = csv.reader(budget_file, delimiter=',')
    next(csvreader)

    for row in csvreader:
        # Store Data
        months.append(row[0])
        profit_loss.append(int(row[1]))
        # calculate the total number of months includeed in the dataset
        # total amount of months
        month_count = month_count + 1
    
        # Calculate the net total of "pprofit/losses" over the enrite preiod
        total_profit_loss = total_profit_loss + int(row[1])

        # Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
        profit_change.append(int(row[1]) - intial_price)
        intial_price = int(row[1])
        
        # find the greatest increase in profits (date and amount) over the entire period
        
        greatest_inc = max(profit_change)
        greatest_inc_date = months[profit_change.index(greatest_inc)]
        # the greatest decrease in losses (date and amount) over the entire period
        greatest_dec = min(profit_change)
        greatest_dec_date = months[profit_change.index(greatest_dec)]
       
        # print anaylsis in Terminal

del profit_change[0]
average_change = round(sum(profit_change) / (month_count -1), 2)
#print(profit_change)

print("Financial Analysis")

print("-------------------------------------")
    
print(f"Total Months: {month_count}")
print(f"Total Profit/Loss: ${total_profit_loss}")
print(f"Total Average: ${average_change}")
print(f"Greatest increase in profits: {greatest_inc_date} ${greatest_inc}")
print(f"Greatest loss in profits: {greatest_dec_date} ${greatest_dec}")
# export a .txt file

with open("Financial_analysis.txt", 'w') as summary:
    summary.write("Financial Analysis\n")
    summary.write("--------------------------------------\n")
    summary.write(f"Total Months: {month_count}\n")    
    summary.write(f"Total Profit/Loss: ${total_profit_loss}\n")
    summary.write(f"Total Average: ${average_change}\n")
    summary.write(f"Greatest increase in profits: {greatest_inc_date} ${greatest_inc}\n")
    summary.write(f"Greatest loss in profits: {greatest_dec_date} ${greatest_dec}\n")
