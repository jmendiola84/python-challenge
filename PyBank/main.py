#PyBank
import os
import csv

file=open("FinancialAnalysis.txt","w")

for filename in os.listdir("Data"):
    if filename.endswith(".py"): 
        print(os.path.join(filename))
        continue

    totalMonths=0
    totalRevenue=0
    greatestIncRevenue=0
    greatestDecRevenue=0

    financialCSV = os.path.join("Data", filename)

    # Read in the CSV file
    with open(financialCSV, 'r') as csvfile:
    # Split the data on commas
        csvreader = csv.reader(csvfile, delimiter=',')
    # Loop through the data
        filename = os.path.basename(financialCSV)

        for row in csvreader:
            if row[0] == "Date":
                continue
            elif row==2:
                greatestIncRevenue=int(row[1])
                greatestDecRevenue=int(row[1])

            totalMonths = int(totalMonths) + 1 
            totalRevenue = int(totalRevenue) + int(row[1])
        
            if int(row[1]) > int(greatestIncRevenue):
                greatestIncRevenue = int(row[1])
                greatestIncRevenueMonth= row[0]

            if int(row[1]) < int(greatestDecRevenue):
                greatestDecRevenue = int(row[1])
                greatestDecRevenueMonth = row[0]

    avgRevChg = round(int(totalRevenue)/int(totalMonths))


    print("Financial Analysis - " + filename)
    print("-------------------------")
    print("Total Months: " + str(totalMonths))
    print("Total Revenue: $" + str(totalRevenue))
    print("Average Revenue Change: $" + str(avgRevChg))
    print("Greatest Increase in Revenue: " + str(greatestIncRevenueMonth) + " ($" + str(greatestIncRevenue)+")")
    print("Greatest Decrease in Revenue: " + str(greatestDecRevenueMonth) + " ($" + str(greatestDecRevenue)+")")
    print("                                  ")

    file.write("Financial Analysis - " + filename + "\n")
    file.write("-------------------------\n")
    file.write("Total Months: " + str(totalMonths)+ "\n")
    file.write("Total Revenue: $" + str(totalRevenue) + "\n")
    file.write("Average Revenue Change: $" + str(avgRevChg) + "\n")
    file.write("Greatest Increase in Revenue: " + str(greatestIncRevenueMonth) + " ($" + str(greatestIncRevenue)+")\n")
    file.write("Greatest Decrease in Revenue: " + str(greatestDecRevenueMonth) + " ($" + str(greatestDecRevenue)+")\n")
    file.write("                                  \n")

file.close()