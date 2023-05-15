# Accept three sides of the triangle and check whether the triangle is possible or not.

a = int(input('Enter the first side of triangle:'))
b = int(input('Enter the Second side of triangle:'))
c = int(input('Enter the third side of triangle:'))
if((a+b>c) and (a+c>b) and (b+c>a)):
    print('the triangle is possible')
else:
    print('the triangle is Not possible')
