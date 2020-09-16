# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 17:12:42 2020
Manuel Castillo
1431705
@author: 18327
"""
print('Davy\'s auto shop services')
print('Oil change --$35')
print('Tire rotation --$19')
print('Car wash -- $7')
print('Car wax -- $12')




service_1 = input("Select first service:")
service_2 = input("Select second service:")

print('Davy\'s auto shop services')


if service_1 == '-':
    print('No service')
elif service_1 == 'Oil Change':
    print("Service 1: Oil change, $35")    
elif service_1 == 'Tire rotation':
    print('Service 1: Tire rotation, $19')
elif service_1 == 'Car wash':
    print('Service 1: Car wash, $7')
elif service_1 == 'Car wax':
    print('Service 1: Car wax, $12')

if service_2 == '-':
    print('No service')
elif service_2 == 'Oil Change':
    print("Service 2: Oil change, $35")    
elif service_2 == 'Tire rotation':
    print('Service 2: Tire rotation, $19')
elif service_2 == 'Car wash':
    print('Service 2: Car wash, $7')
elif service_2 == 'Car wax':
    print('Service 2: Car wax, $12')
    
    






