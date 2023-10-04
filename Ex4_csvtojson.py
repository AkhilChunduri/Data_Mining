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


# Initialize an empty result dictionary
result_dict = {}

# Open the JSON file for reading
with open("items.json", "r") as input_file:
    item_data = input_file.readlines()

# Iterate over each line in the file
for line in item_data:
    print(line)
    trans_dict = json.loads(line)






    




