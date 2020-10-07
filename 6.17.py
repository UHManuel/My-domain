"""

Manuel Castillo
1431705

"""




For_pass = input()
code = ''
# i = '!'
# if For_pass == i:
# print(i)

for x in For_pass:
    if (x == 'i'):
        code += "!"
    elif (x == 'a'):
        code += "@"
    elif (x == 'm'):
        code += "M"
    elif (x == 'B'):
        code += "8"
    elif (x == 'o'):
        code += "."
    else:
        code += x

code += "q*s"
print(code)