import os
import csv

totalVotes=0
voting=0
for filename in os.listdir("Data"):
    if filename.endswith(".py"):
        continue

    electionCSV =os.path.join("Data",filename)
    candidates=[]
    votes=[]
    numvotes=[]
    pctvotes=[]
    moreVotes=0
    with open(electionCSV,'r') as csvfile:
        csvreader=csv.reader(csvfile,delimiter=',')
        header=next(csvreader)

        
        for row in csvreader:
            votes.append(row[2])
            if row[2] not in candidates:
                candidates.append(row[2])
            
            totalVotes=totalVotes + 1

        for candidate in candidates:
            voted = votes.count(candidate)
            numvotes.append(voted)
            if voted > moreVotes:
                moreVotes = voted
                winner = candidate


        print ("Elections Results")
        print ("------------------")   
        print ("Total Votes: " + str(totalVotes))
        for i in range(len(candidates)):
            pctVotes = round(int(numvotes[i])/int(totalVotes)*100,2)
            print(candidates[i] + ": " + str(pctVotes) + "% (" + str(numvotes[i]) + ")")
        print("----------------")
        print ("Winner: " + winner)
       
