num = int (input ('Enter Number : '))
if(num%2 != 0):
    print('Number is Odd ')
    fact = 1
    while(num%2 == 0):
        fact = fact * num
        num = num-1
    print('the factorial of the number is :',fact)
    digits = 0
    while(fact>0):
        fact = fact/10
        digits = digits+1
    print('the number of digits in the factorial of the number is : ',digits)
else:
    num = str(num)
    rev = num[::-1]
    if num == rev:
        print('the given number is a palindrome')
    else:
        print('the given number is a not palindrome')