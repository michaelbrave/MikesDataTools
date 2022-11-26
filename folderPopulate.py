# this tool will take a csv file and create folder structures named after the contents of the rows in col[2] then subfolders named for col[3]

import os
import csv

# tell it which directory to change to
os.chdir(os.path.expanduser("..\..\..\Code\DataSets\PokemonMaster"))

# needed utf 8 seems a problem with python 3
with open('PokemonData.csv', encoding="utf8", newline='') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    next(readCSV) #skips first row which is a header
    for row in readCSV:
        dirName = "/".join((row[2], row[3])).replace(' ', '_') #this changes spaces to _, the join rows makes sub folders for the second joined row
        if not os.path.exists(dirName):
            os.makedirs(dirName)
            print(dirName + " Folder Created")
        else:
            print("No Directories Created")

# tell what current directory is
print(os.getcwd)
