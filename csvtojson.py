import csv
import json
from pprint import pprint


with open("csv file.csv", "r") as f:
    reader = csv.DictReader(f)
    csv_file = list(reader) 
mylist = []

for list in csv_file:
    #print(list["surname"][0:1])
    if list['surname'][0:1] == "a":
        mylist.append(list)


with open("json file2.json", "w") as f:
    json.dump(mylist, f, indent=2)


