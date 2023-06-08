'''  The rules for determining whether or not a year is a leap year follow: Any year that is divisible by 400 is a leap year. Of the remaining years, any year that is divisible by 100 is not a leap year. Of the remaining years, any year that is divisible by 4 is a leap year. All other years are not leap years. Write a program that reads a year from the user and displays a message indicating whether or not it is a leap year.'''

year=int(input("Enter the year"))
if(year%400==0 and year%4==0):
    print("It is a leap year")
else:
    print("It is not a leap year")