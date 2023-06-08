# Check if the nth power of a number is even or not (get the number and the power as an input).

n = int (input ('Enter number to Check if the nth power of a number is even or not:'))
power = int (input('Enter the power:'))
result =pow(n,power)
if(result%2 == 0):
    print('Even number')
else:
    print('Not Even number')