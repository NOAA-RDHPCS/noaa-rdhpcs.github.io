'''
    csvToRstTable.py - generate a table in .rst format from an input CSV file
    
    Execution arguments:
        -f --filename -> location of .csv input file
        -w --wrapafter -> (Optional - defaults to 999) number of characters per line before wrapping text
        -n --noheaderrow -> (Optional) .csv data does not include a header row
        -d --debug -> (Optional) increase logging for debugging purposes 
'''

import csv
import argparse
import sys

parser = argparse.ArgumentParser()

parser.add_argument("-f", "--filename", dest="filename", help="Location of .csv input file")
parser.add_argument("-d", "--debug", dest="debug", help="Additional logging for debugging", action=argparse.BooleanOptionalAction)
parser.add_argument("-w", "--wrapAfter", dest="wrapAfter", help="Wrap lines after n characters", default=999, type=int)
parser.add_argument("-n", "--noheaderrow", dest="noHeaderRow", help="First line is not a header row", action=argparse.BooleanOptionalAction)

args = parser.parse_args()

inputFilename = args.filename
outputFileName = (args.filename).replace('.csv', '_table.rst')

if args.debug:
    print("CSV File Location:", inputFilename)
    print("Table without header row?:", args.noHeaderRow)
    print("Wrap lines after", str(args.wrapAfter), "characters")
    print("Output destination:", outputFileName)


#####################
#  Work Variables!  #
#####################

# To capture row data
inputRows = []

# All rows should have the same number of fields - this will be captured on the first row,
#   and all other rows will be checked that they have the same number of fields
expectedFieldCount = 0

# As we iterate through, identify the maximum size for each field, for use with later formatting
maxFieldSizes = []

# Open output file for writing
outputFile = open(outputFileName, 'w')


#####################
#    Functions!!    #
#####################

# Load and process input CSV file, determining number of fields and max size for each field
def readInCsvData():
    with open(inputFilename, newline='') as f:
        reader = csv.reader(f)
        for row in reader:

            # For first row, grab the expected number of fields and set baseline for max field size
            if len(inputRows) == 0:
                expectedFieldCount = len(row)


                # Iterate through fields and capture length as initial max value
                # - if it exceeds the wrap limit, set the wrap limit as the max
                fieldCount = 0
                for field in row:
                    if len(field) > args.wrapAfter:
                        maxFieldSizes.append(args.wrapAfter)
                    else:
                        maxFieldSizes.append(len(field))
                    fieldCount = fieldCount + 1

            else:
                # If this row does not contain the expected number of fields, fail the script with the appropriate error message
                if len(row) != expectedFieldCount:
                    sys.exit(" ".join(
                        ["Error! Row #", str(len(inputRows) + 1), "has", str(len(row)), "fields - was expecting",
                         str(expectedFieldCount), "- please check and update file before rerunning!"]))

                # Iterate through fields and compare length to current max falue
                # - if it is greater, capture this as the new max length for the field
                # - if it exceeds the wrap limit, set the wrap limit as the max
                fieldCount = 0
                for field in row:
                    if len(field) > maxFieldSizes[fieldCount]:
                        if len(field) > args.wrapAfter:
                            maxFieldSizes[fieldCount] = args.wrapAfter
                        else:
                            maxFieldSizes[fieldCount] = len(field)
                    fieldCount += 1

            inputRows.append(row)

    if args.debug:
        print("Total input rows", inputRows)
        print("Expected field count", expectedFieldCount)
        print("Array of max field sizes", maxFieldSizes)


# Now, process the data row!
# - generate all markup fields to format into .rst grid table
# - split text into multiple lines when it exceeds wrap length
def processRowData(row):
    overflowForThisRow = []
    fieldCount = 0

    # Iterate through each field and split out any text beyond the determined wrap threshold
    for field in row:
        overflow = ""
        maxFieldSize = maxFieldSizes[fieldCount]
        if len(field) >= maxFieldSize:
            field, overflow = splitOverflowForField(field, maxFieldSize)

        overflowForThisRow.append(overflow)

        outputFile.write("| " + field + (" " * (maxFieldSize - len(field) + 1)))
        fieldCount += 1

    return overflowForThisRow

# If a field exceeds the max length, trim it to the final space before that limit
def splitOverflowForField(field, maxFieldSize):

    trimmedField = field[0:maxFieldSize]
    indexOfLastSpace = trimmedField.rfind(' ')

    # Return trimmed field for writing and remaining field text to continue recursively trimming
    return field[0:indexOfLastSpace], field[indexOfLastSpace + 1:]


# Write out the input data in .rst format
def writeOutRstTable():
    # Lighter than always going back to get the Count...
    rowCount = 0;

    # Iterate through each row to format accordingly
    for row in inputRows:

        ### First, print out border above line ###
        # For regular rows, use a hyphen -- for the first data row below the header, use an equal sign
        fillerCharacter = "-"
        if rowCount == 1 and not args.noHeaderRow:
            fillerCharacter = "="
        # Write out with a one character buffer on either side of the field size
        for fieldSize in maxFieldSizes:
            outputFile.write("+" + (fillerCharacter * (fieldSize + 2)))
        # Final grid marker and new line for the actual data
        outputFile.write("+\n")

        # Process and write out the row, and receive back any "overflow" data from the field being longer than the set limit
        overflowForThisRow = processRowData(row)

        # If we have fields which exceed the max length, loop through and break into acceptable-sized strings and write out
        while any(overflowForThisRow):
            # Close off previous line
            outputFile.write("|\n")

            # Process row and update overflowForThisRow list
            overflowForThisRow = processRowData(overflowForThisRow)

        # Final grid marker and new line, then on to the next one!
        outputFile.write("|\n")
        rowCount += 1

    # Bottom border of grid -- write out with a one character buffer on either side of the field size
    for fieldSize in maxFieldSizes:
        outputFile.write("+" + ('-' * (fieldSize + 2)))

    # Final grid marker 
    outputFile.write("+")

################
# Core Logic   #
################

readInCsvData()
writeOutRstTable()

print("Your .rst table should be available in", outputFileName)
