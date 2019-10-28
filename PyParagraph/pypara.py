# # PyParagraph
# ![Language](Images/language.png)
# In this challenge, you get to play the role of chief linguist at a local learning academy. As chief linguist, you are responsible for assessing the complexity of various passages of writing, ranging from the sophomoric Twilight novel to the nauseatingly high-minded research article. Having read so many passages, you've since come up with a fairly simple set of metrics for assessing complexity.
# Your task is to create a Python script to automate the analysis of any such passage using these metrics. Your script will need to do the following:

# * Import a text file filled with a paragraph of your choosing.
# * Assess the passage for each of the following:
#   * Approximate word count
#   * Approximate sentence count
#   * Approximate letter count (per word)
#   * Average sentence length (in words)

# * As an example, this passage:
# > “Adam Wayne, the conqueror, with his face flung back and his mane like a lion's, stood with his great sword point upwards, the red raiment of his office flapping around him like the red wings of an archangel. And the King saw, he knew not how, something new and overwhelming. The great green trees and the great red robes swung together in the wind. The preposterous masquerade, born of his own mockery, towered over him and embraced the world. This was the normal, this was sanity, this was nature, and he himself, with his rationality, and his detachment and his black frock-coat, he was the exception and the accident a blot of black upon a world of crimson and gold.”
# ...would yield these results:

# ```output
# Paragraph Analysis
# -----------------
# Approximate Word Count: 122
# Approximate Sentence Count: 5
# Average Letter Count: 4.6
# Average Sentence Length: 24.0
# ```

# * **Special Hint:** You may find this code snippet helpful when determining sentence length (look into [regular expressions](https://en.wikipedia.org/wiki/Regular_expression) if interested in learning more):

# ```python
# import re
# re.split("(?<=[.!?]) +", paragraph)
# ```


import os
import csv

# import regular expression module
import re

# remove some special cases and spurious conditions from the content stream
def cleanContents(contents):

    # because splitSentence regex is mistakenly cating periods after middle inital
    # get rid of period after abbreviated middle name Ann V. Coates => Anne V coates
    # this is brute force, case by case.  I can't think of elegant general solution right now
    cleaned = contents.replace("Anne V. Coates", "Anne V Coates")
    return cleaned

def splitSentences(paragraph):
    # split sentences using sentence punctiation (. ! ?) as delimeter
    # keep the punction in the sentence that is split out
    # uses a "positive look-behined assertion"  explained here:  
    #          https://docs.python.org/2/library/re.html
    #    sentences = re.split("(?<=[.!?])[ \n]+", paragraph)
    # added checks for space and newline [ \n]+ as whitespace after punctioan
    # added check for end quotes after punctiaton
    sentences = re.split("(?<=[.!?])[\"\']?[ \n]+", paragraph)

    #print(f"\nSentences are: \n{sentences}\n")
    return sentences

def splitWords(sentence):
    # alternative 1
    # split out words by matching any non-alphamumeric char as delimeter (\W+)
    words = re.split("\W+", sentence)

    # alternative 2
    # split words using regexp of any whitespace or puncuation as delimeter
    #words = re.split("[ \r\t\v\n.,!?\"\']+", sentence)

    #print(f"\nOriginal Sentence: {sentence}\n")
    #print(f"Detected Words: {words}")

    return words

# analyze paragrpah contents and return results in a dictionary
# results = {
#     'WordCnt': totalWordCount,
#     'SentenceCnt': sentenceCount,
#     'AveSentenceLen', aveSentenceLen
#     'AveWordLen', aveWordLen
#     }
def analyzeContents(contents) :
    results = {}

    sentences = splitSentences(contents)

    totalWordCount = 0 
    sentenceCount = 0
    letterCount = 0

    for sentence in sentences:
        # count sentences
        sentenceCount += 1

        # split words from sentence
        words = splitWords(sentence)
        wordCount = 0

        for word in words:
            # count words and letters
            if word != '':
                wordCount += 1
                letterCount += len(word)

        totalWordCount += wordCount

    # calculate averages
    aveWordLen = letterCount / totalWordCount 
    aveSentenceLen = totalWordCount / sentenceCount

    # return results in a dictionary
    results['WordCnt'] = totalWordCount
    results['SentenceCnt'] = sentenceCount
    results['AveSentenceLen'] = aveSentenceLen
    results['AveWordLen'] = aveWordLen

    return results

# Recieve Results in dictionary form and print to terminal and output analysis file
# resultsDictionary = {
#     'WordCnt': totalWordCount,
#     'SentenceCnt': sentenceCount,
#     'AveSentenceLen', aveSentenceLen
#     'AveWordLen', aveWordLen
#     }
def outputResults(results, outstream, inFileName) :
    #print("Results are: \n")
    #print(results)

    # create test to be output
    textlines = []
    textlines.append(f"Analysis Results for file {inFileName}")
    textlines.append("-------------------------------------------")
    textlines.append(f"Approximate Word Count: {results['WordCnt']}")
    textlines.append(f"Approximate Sentence Count: {results['SentenceCnt']}") 
    textlines.append(f"Average Letter Count: {results['AveWordLen']:.3f}")
    textlines.append(f"Average Sentence Length: {results['AveSentenceLen']:.3f}")

    for text in textlines:
        print(text)
        outstream.write(text)
        outstream.write("\n")


# Main Function
# I used this website to define main function and pass commandline args
# https://www.tutorialspoint.com/python/python_command_line_arguments.htm 
# it also uses try:except exeption handling.  
# Assumption:  something equivalent will eventually be boiler plate in the class.
import sys, getopt

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print('pypara.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('pypara.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    if ((inputfile == '') or (outputfile == '')) :
        print("Inputfile and Outputfile are required arguments")
        print('pypara.py -i <inputfile> -o <outputfile>')
        sys.exit()

    print('Input file is ', inputfile)
    print('Output file is ', outputfile)
    inputPath = inputfile
    outputPath = outputfile
    #inputPath = os.path.join('.', 'inputfile')
    #outputPath = os.path.join('.', "outputfile")

    # Read in the paragraph text raw datafile
    with open(inputPath, 'r') as inputStream:
        print(inputStream)

        # Read the paragraphs
        contents = inputStream.read()

        # clean the contents from spurious conditions
        cleanedContents = cleanContents(contents)

        # analyzeContents to accumulate summary data
        results = analyzeContents(cleanedContents)

    # output the results to screen and output text file
    # https://cmdlinetips.com/2012/09/three-ways-to-write-text-to-a-file-in-python/'
    with open(outputPath, "w") as outputStream:
        print(outputStream)
        print()

        outputResults(results, outputStream, inputfile)

# not sure what the If block is for, but just need to call main from global area
if __name__ == "__main__":
   main(sys.argv[1:])




 