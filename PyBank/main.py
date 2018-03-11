#Import libraries
import os
import csv
#Create new file to save results
file=open("FinancialAnalysis.txt","w")
#Loop to iterate within all files
for filename in os.listdir("Data"):
    #Conditional to read only CSV files in the directory
    if filename.endswith(".csv"): 
        #Declare variables
        totalMonths=0
        totalRevenue=0
        greatestIncRevenue=0
        greatestDecRevenue=0
        #Path to the CSV files
        financialCSV = os.path.join("Data", filename)
        
        # Read in the CSV file
        with open(financialCSV, 'r') as csvfile:
            # Split the data on commas
            csvreader = csv.reader(csvfile, delimiter=',')
            # Get filename
            filename = os.path.basename(financialCSV)
            #Loop to 
            for row in csvreader:
                #Conditional to skip first row
                if row[0] == "Date":
                    continue
                elif row==2:
                    #To get an initial value for further comparison
                    greatestIncRevenue=int(row[1])
                    greatestDecRevenue=int(row[1])
                #Incremental to count months and revenue
                totalMonths = int(totalMonths) + 1 
                totalRevenue = int(totalRevenue) + int(row[1])
                #Conditional to compare values to find month with greatest increase revenue
                if int(row[1]) > int(greatestIncRevenue):
                    greatestIncRevenue = int(row[1])
                    greatestIncRevenueMonth= row[0]
                #Conditional to compare values to find month with greatest decrease revenue
                if int(row[1]) < int(greatestDecRevenue):
                    greatestDecRevenue = int(row[1])
                    greatestDecRevenueMonth = row[0]
        #To calculate average revenue change
        avgRevChg = round(int(totalRevenue)/int(totalMonths))

        #Report of Financial Analysis
        print("Financial Analysis - " + filename)
        print("-------------------------")
        print("Total Months: " + str(totalMonths))
        print("Total Revenue: $" + str(totalRevenue))
        print("Average Revenue Change: $" + str(avgRevChg))
        print("Greatest Increase in Revenue: " + str(greatestIncRevenueMonth) + " ($" + str(greatestIncRevenue)+")")
        print("Greatest Decrease in Revenue: " + str(greatestDecRevenueMonth) + " ($" + str(greatestDecRevenue)+")")
        print("                                  ")
        #Report added to the file
        file.write("Financial Analysis - " + filename + "\n")
        file.write("-------------------------\n")
        file.write("Total Months: " + str(totalMonths)+ "\n")
        file.write("Total Revenue: $" + str(totalRevenue) + "\n")
        file.write("Average Revenue Change: $" + str(avgRevChg) + "\n")
        file.write("Greatest Increase in Revenue: " + str(greatestIncRevenueMonth) + " ($" + str(greatestIncRevenue)+")\n")
        file.write("Greatest Decrease in Revenue: " + str(greatestDecRevenueMonth) + " ($" + str(greatestDecRevenue)+")\n")
        file.write("                                  \n")
#File closed
file.close()