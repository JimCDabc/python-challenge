# You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). 
# The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. 
# Your task is to create a Python script that analyzes the votes and calculates each of the following:

#   * The total number of votes cast
#   * A complete list of candidates who received votes
#   * The percentage of votes each candidate won
#   * The total number of votes each candidate won
#   * The winner of the election based on popular vote.
# * As an example, your analysis should look similar to the one below:
#   ```text
#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------
#   ```

# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# ---  BEGIN SOLUTIONS ----
import os
import csv

# declare pahts for input and output files
inputData_csv = os.path.join('.', 'Resources', 'election_data.csv')
resultsFile = os.path.join('.', "pyPollResults.txt")

# FUNCTION: calculateResults(bankData) 
# Input: takes rows of bankData 
# Ouput: 
# Returns a results dictionary with the folling key value pairs
#   resultsDict = {
#        'votes': votecount,
#        '<candidate's name 1>': votes,
#         ...
#        '<candidate's name n>': votes,
#        'candidates: ["name1", "name2", "name n"]
#   }

def calculateResults(pollData):

    results = {}  # results dictionary
    numVotes = 0  # counter for total number of votes
    candidateList = [] # list of candidates detected

    for row in pollData:
        numVotes += 1  # increment total vote count
        candidate = row[2] # get the current candidate name
        if not(candidate in candidateList):
            # newly recognized candidate
            # add new candidate to list and initalize first vote
            # print(f"adding {candidate} to candidate list")
            candidateList.append(candidate)
            results[candidate] = 1
        else:
            # add one to candidate's vote tally
            results[candidate] = results[candidate] + 1        

    # add total vote count ot results dictionary
    results['votes'] = numVotes
    # add candidate list to results dictionary
    results['candidates'] = candidateList

    # return results dictionary
    return results
 
    

def outputResults(results, outFile) :
    # print(results)
    totalVotes = results['votes']  # retrieve total votes form results dict

    # initailize textLines to be output iwth header and total votes
    textLines = [
        "Election Results",
        "----------------------------",
        f"Total Months: {totalVotes}",
        "----------------------------" ]
 
    # append votes and percentage of total for each candidate to textLines
    candidates = results['candidates']
    winner = ""
    maxVotes = 0
    for candidate in candidates:
        votes = results[candidate]
        percentVotes =  votes / totalVotes   
        textLines.append(f"{candidate}: {100 * percentVotes:.3f}% ({votes})")

        # determine the winner by finding max vote count across candidates 
        if votes > maxVotes:
            maxVotes = votes
            winner = candidate

    textLines.append(f"Winner: {winner}")

    #print(textLines)
    
    for line in textLines:
        print(line)
        outFile.write(line)
        outFile.write("\n")

# Main routine 
# Read in the CSV file
with open(inputData_csv, 'r') as inputFile:
    print(inputFile)

    # Split the data on commas
    dataReader = csv.reader(inputFile, delimiter=',')

    header = next(dataReader)

    resultsDict = calculateResults(dataReader)

# output the results to screen and output text file
# https://cmdlinetips.com/2012/09/three-ways-to-write-text-to-a-file-in-python/'
with open(resultsFile, "w") as outputFile:
    print(outputFile)
    print()
    print()

    outputResults(resultsDict, outputFile)


