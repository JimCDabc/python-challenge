# # PyBoss

# ![Boss](Images/boss.jpg)
# In this challenge, you get to be the _boss_. 
# You oversee hundreds of employees across the country developing Tuna 2.0, a world-changing snack food based on canned tuna fish. 
# Alas, being the boss isn't all fun, games, and self-adulation.
# The company recently decided to purchase a new HR system, and unfortunately for you, the new system requires employee records be stored completely differently.
# Your task is to help bridge the gap by creating a Python script able to convert your employee records to the required format. 
# 
# Your script will need to do the following:

# * Import the `employee_data.csv` file, which currently holds employee records like the below:
# ```csv
# Emp ID,Name,DOB,SSN,State
# 214,Sarah Simpson,1985-12-04,282-01-8166,Florida
# 15,Samantha Lara,1993-09-08,848-80-7526,Colorado
# 411,Stacy Charles,1957-12-20,658-75-8526,Pennsylvania
# ```

# * Then convert and export the data to use the following format instead:
# ```csv
# Emp ID,First Name,Last Name,DOB,SSN,State
# 214,Sarah,Simpson,12/04/1985,***-**-8166,FL
# 15,Samantha,Lara,09/08/1993,***-**-7526,CO
# 411,Stacy,Charles,12/20/1957,***-**-8526,PA
# ```

# * In summary, the required conversions are as follows:
#   * The `Name` column should be split into separate `First Name` and `Last Name` columns.
#   * The `DOB` data should be re-written into `MM/DD/YYYY` format.
#   * The `SSN` data should be re-written such that the first five numbers are hidden from view.
#   * The `State` data should be re-written as simple two-letter abbreviations.

# * Special Hint: You may find this link to be helpful—[Python Dictionary for State Abbreviations](https://gist.github.com/afhaque/29f0f4f37463c447770517a6c17d08f5).

import os
import csv

# import the us state abbreviatons
import us_abbrevs

# declare pahts for input and output files
inputData_csv = os.path.join('.', 'employee_data.csv')
outputPath = os.path.join('.', "pyBossData.csv")

def cleanData(dataRows):
    IDs = []
    FirstNames = []
    LastNames = []
    DOBs = []
    SSNs = []
    States = []

    for row in dataRows:
        # append Employee ID
        IDs.append(row[0])

        # split name and append first and last name
        names = row[1].split(' ')
        FirstNames.append(names[0])
        LastNames.append(names[1])

        # split DoB into [yyyy, mm, dd], reformat as MM/DD/YYYY and append
        date = row[2].split('-')
        DOBs.append(f"{date[1]}/{date[2]}/{date[0]}")

        # split SSN and reformat as ***-**-nnnn and append
        ssn = row[3].split('-')
        SSNs.append(f"***-**-{ssn[2]}")

        # look up state abbrev and append
        # use dictionary imported from us_abbrevs.py
        state = row[4]
        States.append(us_abbrevs.us_state_abbrev[state])

    # Zip lists together
    cleaned_csv = zip(IDs, FirstNames, LastNames, DOBs, SSNs, States)
    return cleaned_csv

# Main routine 
# Read in the CSV file
with open(inputData_csv, 'r') as inputFile:
    print(inputFile)

    # Split the data on commas
    dataReader = csv.reader(inputFile, delimiter=',')

    header = next(dataReader)

    cleaned_csv = cleanData(dataReader)

#  Open the the cleane data to the output file
with open(outputPath, "w", newline="") as dataFile:
    print(dataFile)
    writer = csv.writer(dataFile)

    # Write the header row
    writer.writerow(["Emp ID", "First Name", "Last Name","DOB","SSN","State"])

    # Write in zipped rows
    writer.writerows(cleaned_csv)
   