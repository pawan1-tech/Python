num = int (input ('Enter Number : '))
if(num%2 != 0):
    print('Number is Odd ')
    fact = 1
    while(num > 0):
        fact = fact * num
        num = num-1
    print('the factorial of the number is :',fact)
    digits = 0
    while(fact>0):
        fact = int(fact/10)
        digits = digits+1
    print('the number of digits in the factorial of the number is : ',digits)
else:
    rev=0
    n =num
    while(n > 0):
        rem = n % 10
        rev = rev * 10 + rem
        n = int (n / 10)
    print(rev)
    if (num == rev):
        print('the given number is a palindrome')
    else:
        print('the given number is a not palindrome')