# Write a Python program to solve the equation z = |x - y| * (x + y).
x = int (input ('Enter value of x:'))
y = int (input ('Enter value of y:'))
z = abs(x - y) * (x + y)
print(z)