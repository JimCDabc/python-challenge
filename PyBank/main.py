import os
import csv
#* In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. (Thankfully, your company has rather lax standards for accounting so the records are simple.)
#* Your task is to create a Python script that analyzes the records to calculate each of the following:

#  * The total number of months included in the dataset
#
#  * The net total amount of "Profit/Losses" over the entire period
#
#  * The average of the changes in "Profit/Losses" over the entire period
# 
#   * The greatest increase in profits (date and amount) over the entire period
#   * The greatest decrease in losses (date and amount) over the entire period

# * As an example, your analysis should look similar to the one below:
#   ```text
#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)
#   ```
# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.
# # Path to collect data from the Resources folder


# BEGIN CODE FOR ASSIGNMENT

# declare pahts for input and output files
inputData_csv = os.path.join('.', 'Resources', 'budget_data.csv')
resultsFile = os.path.join('.', "pyBankeResults.txt")

# FUNCTION: calculateResults(bankData) 
# Input: takes rows of bankData 
# Ouput: 
# Returns a results dictionary with the folling key value pairs
#   resultsDict = {
#        'Total Months': months,
#        'Ave Change': averageChange,
#        'Greatest Increase' { 'date': date, 'change': incAmount},
#        'Greatest Decrease' { 'date': date, 'change': decAmount}
#   }
def calculateResults(bankData):
    # Set up results dict
    results = {}

    totalChange = 0
    maxChange = 0
    maxDate = ''
    minChange = 0
    minDate =''
    numRows = 0
    # For readability, it can help to assign your values to variables with descriptive names
    for row in bankData:
        change = float(row[1])
        totalChange += change
        if (change > maxChange):
            maxDate = row[0]
            maxChange = change

        if (change < minChange):
            minDate = row[0]
            minChange = change
        numRows += 1 
    
    aveChange = totalChange / numRows

    # Assemble Results Dictionary
    results['Months'] = numRows
    results['AveChange'] = aveChange
    results['MaxInc'] = {'date': maxDate, 'change': maxChange}
    results['MinDec'] = {'date': minDate, 'change': minChange}

    return results

def outputResults(results, outFile) :
    textLines = [
        "  Financial Analysis\n"
        "----------------------------\n"
        f"Total Months: {results['Months']}\n"
        f"Average Change: ${results['AveChange']:.2f}\n"
        f"Greatest Increase: {results['MaxInc']['date']} ${results['MaxInc']['change']:.2f}\n"
        f"Greatest Decrease: {results['MinDec']['date']} ${results['MinDec']['change']:.2f}\n"
    ]
    
    for line in textLines:
        print(line)
    
    outFile.writelines(textLines)

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


