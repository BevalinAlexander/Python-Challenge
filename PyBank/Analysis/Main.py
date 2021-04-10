#import Modules 
import os
import csv

#set path for file 
csvpath = os.path.join("..","resources","budget_data.csv")

#open csv file 
with open(csvpath) as csvfile
    csvreader = csv.reader(csvfile, delimiter=",")
    next (csvreader,None)