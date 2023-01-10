# Import dependencies
import csv

budget_data_csv = "Resources/budget_data.csv"
profit_loss_analysis = "analysis/pybank_output.txt"

# Define PyBank's variables
months = []
changes_in_profit_losses = []

total_months = 0
net_amount = 0
previous_amount = 0
current_amount = 0
change_in_amount = 0

# Open and read csv
with open(budget_data_csv) as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvfile)
             
    # Read through each row of data after the header
    for row in csv_reader:

        # Count number of months
        total_months += 1

        # Net total amount of "Profit/Losses" over the entire period
        current_amount = int(row[1])
        net_amount += current_amount

        if (total_months == 1):
            previous_amount = current_amount
            continue

        else:

            # Calculate change in profit loss 
            change_in_amount = current_amount - previous_amount

            # Add to the end of the list 
            months.append(row[0])

            # Add each to the end of the list 
            changes_in_profit_losses.append(change_in_amount)

            # Make the current_month_loss to be previous_month_profit_loss for the next loop
            previous_amount = current_amount

    #Calculate sum and average of the changes in entire period
    sum_pl = sum(changes_in_profit_losses)
    average_pl = round(sum_pl/(total_months - 1), 2)

    # Greatest increase in profits (max & min)
    max_change = max(changes_in_profit_losses)
    min_change = min(changes_in_profit_losses)

    # Locate value
    max_month_index = changes_in_profit_losses.index(max_change)
    min_month_index = changes_in_profit_losses.index(min_change)

    # Assign best and worst month
    best_month = months[max_month_index]
    worst_month = months[min_month_index]

# -->>  Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {total_months}")
print(f"Total:  ${net_amount}")
print(f"Average Change:  ${average_pl}")
print(f"Greatest Increase in Profits:  {best_month} (${max_change})")
print(f"Greatest Decrease in Losses:  {worst_month} (${min_change})")

# Export text file with the result 
with open(profit_loss_analysis, "w") as outfile:

    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months:  {total_months}\n")
    outfile.write(f"Total:  ${net_amount}\n")
    outfile.write(f"Average Change:  ${average_pl}\n")
    outfile.write(f"Greatest Increase in Profits:  {best_month} (${max_change})\n")
    outfile.write(f"Greatest Decrease in Losses:  {worst_month} (${min_change})\n")