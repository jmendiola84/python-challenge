#Import libraries 
import os
import csv
#Create a file to store elections results
file=open("Elections Results.txt","w")
#Declare variables
totalVotes=0
#Select only CSV files required into the directory
for filename in os.listdir("Data"):
    if filename.endswith(".csv"):
        #CSVS files path
        electionCSV = os.path.join("Data",filename)
        #Declare variables
        candidates=[]
        votes=[]
        numvotes=[]
        pctvotes=[]
        moreVotes=0
        #Read CSV files
        with open(electionCSV,'r') as csvfile:
            csvreader=csv.reader(csvfile,delimiter=',')
            #Skip first row (headers)
            header=next(csvreader)
            #Loop to count total votes
            for row in csvreader:
                votes.append(row[2])
                #Conditional to add candidates names to Candidates list
                if row[2] not in candidates:
                    candidates.append(row[2])
                #Count of total votes
                totalVotes=totalVotes + 1
            #Loop to count votes for each candidate
            for candidate in candidates:
                voted = votes.count(candidate)
                #Candidate votes added to Votes per Candidate list
                numvotes.append(voted)
                #Conditional to define which candidate got more votes
                if voted > moreVotes:
                    moreVotes = voted
                    winner = candidate

            #Elections report
            print ("Elections Results")
            print ("------------------")   
            print ("Total Votes: " + str(totalVotes))
            print ("------------------")   
            for i in range(len(candidates)):
                pctVotes = round(int(numvotes[i])/int(totalVotes)*100,2)
                print(candidates[i] + ": " + str(pctVotes) + "% (" + str(numvotes[i]) + ")")
            print("----------------")
            print ("Winner: " + winner)
            print ("------------------")   
            print ("          ")
            #Report added to file generated
            file.write ("Elections Results \n")
            file.write ("------------------ \n")   
            file.write ("Total Votes: " + str(totalVotes) + "\n")
            file.write ("------------------ \n")   
            for i in range(len(candidates)):
                pctVotes = round(int(numvotes[i])/int(totalVotes)*100,2)
                file.write(candidates[i] + ": " + str(pctVotes) + "% (" + str(numvotes[i]) + ") \n")
            file.write("---------------- \n")
            file.write ("Winner: " + winner + "\n")
            file.write ("------------------ \n")   
            file.write ("           \n")
#File closed
file.close()