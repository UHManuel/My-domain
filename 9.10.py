"""

Manuel Castillo
1431705

"""

#with open('grades.csv', 'r') as csvfile:
 #   grades_reader = csv.reader(csvfile, delimiter=',')

  #  row_num = 1
   # for row in grades_reader:
    #    print('Row #{}:'.format(row_num), row)
     #   row_num += 1
#from book
import csv
file = input()
dup_1 = {}

with open(file, 'r') as csvfile:
  csvreader = csv.reader(csvfile)
  for row in csvreader:
    for word in row:
      if word not in dup_1.keys():
        dup_1[word] = 1
      else:
        dup_1[word] += 1

for key in dup_1.keys():
  print( key + " " + str(dup_1[key]))