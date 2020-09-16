# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 17:24:08 2020
Manuel Castillo
HW1
@author: 18327
"""

#Write a short Python program for problems.
#Calculate the age of person based on current date und the birthday of the
#user. The program should:
#* Prompt the user to enter the current date by month, day and year
#* Prompt the user to enter the birthday by month, day and year
#* Output the age of the user in years
#* Output a "Happy Birthday!" message if the current date is the user's
#actual birthday.
#* Have nice looking output as shown in the example below
#Example Output
#Birthday Calculator
#Current day
#Month: 9
#Day: 13
#Year: 2005
#Birthday
#Month: 9
#Day: 21
#Year: 1981
#You are 23 years old.


print('Birthday Calculator')
print('Current day')

current_month = int(input('Month: '))
current_day = int(input('Day: '))
current_year = int(input('Year: '))

print('Birthday')
birth_month = int(input('Month: '))
birth_day = int(input('Day: '))
birth_year = int(input('Year: '))

years_1 = current_year - birth_year
print('You are', years_1, 'years old.')


a = 



#if b > a:
 # print("b is greater than a")