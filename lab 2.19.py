# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 13:48:48 2020
Manuel Castillo
1431705
@author: 18327
"""

lemon_1 = float(input('Enter amount of lemon juice (in cups): '))

water_1 = float(input('Enter amount of water (in cups): '))

agave_1 = float(input('Enter amount of agave nectar (in cups): '))

res_1 = float(input('How many servings does it make?: '))


print('Lemonade ingredients - yeilds 6.00: {:.2f} servings'.format(res_1))

print('{:.2f}'.format(lemon_1), 'cup(s) lemon juice')
print('{:.2f}'.format(water_1), 'cup(s) water')
print('{:.2f}'.format(agave_1), 'cup(s) agave nectar')

#part 2

res_2 = float(input('How many servings would you like to make?: '))

lemon_2 = res_2 - 32
water_2 = res_2 + 80
agave_2 = res_2 - 28

print('{:.2f}'.format(lemon_2), 'cup(s) lemon juice')
print('{:.2f}'.format(water_2), 'cup(s) water')
print('{:.2f}'.format(agave_2), 'cup(s) agave nectar')

#part 3

#(3) Convert the ingredient measurements from (2) to gallons. Output the ingredients and serving size. 
#Note: There are 16 cups in a gallon. (Submit for 2 points, so 8 points total).

#Lemonade ingredients - yields 48.00 servings
#1.00 gallon(s) lemon juice
#8.00 gallon(s) water
#1.25 gallon(s) agave nectar


res_3 = float(input('Lemonade ingredients - yields: '))
gallons_to_cups = res_3 / 16

print()

#hours_to_fly = miles / 500.0
#hours_to_drive = miles / 60.0

#print(miles, 'miles would take:')
#print(hours_to_fly, 'hours to fly')
#print(hours_to_drive, 'hours to drive')






