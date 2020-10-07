"""

Manuel Castillo
1431705

"""


#months = dict(Jan=1, Feb=2, Mar=3)
#months_1 = months
#print(months_1())
'''''''''''
March 1, 1990
April 2 1995
7/15/20
December 13, 2003
-1
--
then the output is:
--
3/1/1990
12/13/2003
'''''''''''
months={ "jan":"1","feb":"2", "march":"3","april":"4", "may":"5", "jun":"6","jul":"7", "aug":"8", "sep":"9","oct":"10", "nove":"11", "dec":"12"}

#mo = input()
#day = input()
#year = input()

#for x in months:
    #if x != 'jan':
        #print('ok')
       # if x in mo:
            #print

def average2grade( month ):
   if month == 1:
       return "Jan"
   if month == 2:
       return"Feb"
   if month == 3:
       return" Mar"
   if month == 4:
       return "Apr"
   if month == 5:
       return"May"
   if month == 6:
       return"Jun"
   if month == 7:
       return"Jul"
   if month == 8:
       return"Aug"
   if month == 9:
       return"Sep"
   if month == 10:
       return"Oct"
   if month == 11:
       return"Nov"
   if month == 12:
       return"Dec"



month_1 = float(input("  "))

Day = input()
Year = input()

print(month_1, Day , Year)
