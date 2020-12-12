
"""
Manuel Castillo
1431705

@author: 18327
"""
#First code i tried
#d = []
#p = []
#m = []
#print("Shorted alphabetically")
#with open(file, 'r') as csv_file:
#    csv_reader = csv.reader(csv_file)
    # for apfhabetically order
#    for line in csv_reader:
#        m.append(line)
#def getKey(item):
#    return item[1]
#svdata.sort(key=getKey)
#for i in csvdata:
#    print(i)
#print("Shorted by their Id:")
# for service date oldest to recent
#with open(file, 'r') as csv_file:
#    csv_reader = csv.reader(csv_file)
#    for row in csv_reader:
#        print(row)
#        m.append(row)
#    for i in csvdata:
#        print(i)
#        d.sort()
#print("service date")

#real code
import csv
from operator import itemgetter

# creatin lists to put all csv files in
d = []
p = []
m = []

# Adding the data to the lists and reading it
with open("ManufacturerList.csv", "r") as csv_file:
    m_1 = csv.reader(csv_file)
    for line in m_1:
        m.append(line)

#opening second csv
with open("ServiceDatesList.csv", 'r') as csv_file:
    s_1 = csv.reader(csv_file)
    for line in s_1:
        d.append(line)

#opening third csv
with open("PriceList.csv", 'r') as csv_file:
    p_1 = csv.reader(csv_file)
    for line in p_1:
        p.append(line)

# sorting it
manu = (sorted(m, key=itemgetter(0)))

# adding prices/service dates to the manu list to make it look like the output files

for x in range(len(manu)):
    manu[x].append(d[x][1])

for x in range(len(manu)):
    manu[x].append(p[x][1])
#inventory is finall product sorting the last one for columns 1 and 2 to be able to be abc and manu short
inventory = (sorted(manu, key=itemgetter(1, 2)))
print(inventory)
#print('')


#creating query using def function

def start():
    while True:
        i = input("Enter item manufactuer ex: Apple, Dell, Dells, Lenovo, Lenovos, Samsung or enter 'q' to quit:")
# The reason for the many if statements made it seem the fastest apporach for the query
        if i == "q":
            break
        elif i == "Apple":
            print("Your item is:", inventory[1])
            break
        elif i == "Dell":
            print("Your item is:", inventory[2])
            break
        elif i == "Dells":
            print("Your item is:", inventory[3])
            break
        elif i == "Lenovo":
            print("Your item is:", inventory[4])
            break
        elif i == "Lenovos":
            print("Your item is:", inventory[5])
            break
        elif i == "Samsung":
            print("Your item is:", inventory[6])
            break
        else:
            print("No such item in inventory")
            print("Please re-enter specfic words")


start()

