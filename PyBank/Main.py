#PyBank Main.py
import os
import csv

budget_csv = os.path.join('..', 'Resources', 'budget_data.csv')

num_rows = 0
total = 0
inc_profit = 0
dec_profit = 0
inc_month_profit = 0
dec_month_profit = 0
# Read in the CSV file
with open(budget_csv, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    First_line = next(csvreader)
    num_rows = num_rows + 1
    Profit = []
    Month = []
    Avg_change = []
    first_value = int(First_line[1])
    # Loop through the data
    for row in csvreader:
        num_rows += 1
        net_total =int(row[1])
        pl_change = net_total - first_value
        first_value = net_total

        Profit.append(net_total)
        Month.append(row[0])
        Avg_change.append(pl_change)
        total = sum(Profit) + int(First_line[1])

    inc_profit = max(Avg_change)
    max_index= Avg_change.index(inc_profit)
    max_month = Month[max_index]
   
    dec_profit = min(Avg_change)
    min_index= Avg_change.index(dec_profit)
    min_month = Month[min_index]
  
    avg_change = sum(Avg_change)/len(Avg_change)
print("Finanacial Analysis")
print("-"*50)
print(f"Total Months: {(num_rows)}")
print(f"Total: $ {(total)}")
print(f"Average Change:  ${round(avg_change,2)}")
print(f"Greatest Increase in Profits: {max_month}  ${inc_profit}") 
print(f"Greatest Decrease in Profits: {min_month}  ${dec_profit}")

file = open("PyBank_output.txt","w")
head_line = "Financial Analysis"
dot_line = (f"-"*50)
Months = (f"Total Months: {num_rows}")
Total = (f"Total: ${total}")
Change = (f"Average Change: ${round(avg_change,2)}")
Great_inc = (f"Greatest Increase in Profits: {max_month}  ${inc_profit}")
Great_dec = (f"Greatest Decrease in Profits: {min_month}  ${dec_profit}")
file.write(f'{head_line}\n{dot_line}\n{Months}\n{Total}\n{Change}\n{Great_inc}\n{Great_dec}\n')

