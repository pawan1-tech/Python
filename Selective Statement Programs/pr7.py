''' A company has decided to give bonuses to their employees based on their service.More than 10 Years: 10%More than 6 years and less than 10–8%Less than 6 years: 5%Ask the user to enter the salary and year of service and print their bonus.'''


salary=int(input("Enter the salary: "))
yos=int(input("Enter year of service: "))
if(yos>10):
    print("The bonus amoount is: ",(10/100)*salary)
if(yos>6 and yos<10):
    print("The bonus amount is :",(9/100)*salary)
if(yos<6):
    print("The bonus amount is: ")