import csv

# convert txt files into a csv format
def convertTxtToCsv(inputFile, outputFile):
    with open(inputFile, 'r') as txtFile:
        stripped = (line.strip() for line in txtFile)
        lines = (line.split(" ") for line in stripped if line)
        with open(outputFile, 'w') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(('First Name', 'Count'))
            writer.writerows(lines)

convertTxtToCsv("2000_BoysNames.txt", "2000_BoysNames.csv")
convertTxtToCsv("2000_GirlsNames.txt", "2000_GirlsNames.csv")