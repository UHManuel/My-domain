x1 = int(input())
y1 = int(input())
a1 = int(input())
# this is for the second part
x2 = int(input())
y2 = int(input())
a2 = int(input())

the_answer = False
#For every value of x from -10 to 10
 #  For every value of y from -10 to 10
for x in range(-10, 10):
    for y in range(-10, 10):
        if (x1 * x) + (y1 * y) == a1:
            print ( x,y )
        if (x2 * x) + (y2 * y) == a2:
            print(x,y)
            the_answer = True
            break


if the_answer == (0):
    print ('No solution')