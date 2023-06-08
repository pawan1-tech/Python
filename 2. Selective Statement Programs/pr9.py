''' Accept the name, age, gender (‘M’ or ‘F’), number of days, and display the wages accordingly.Age: greater than or equal to 18 and greater than 30, gender: "M”, then wages will be Rs 700 per dayAge: greater than or equal to 18 and less than 30, gender: "F" then wages will be Rs 750 per day.If age is greater than or equal to 30 and less than or equal to 40, and gender is "M’, then wages will be Rs 800 per day.Age: greater than or equal to 30 and less than or equal to 40; gender: "F," then wages will be Rs 800 per day. '''


name=input("Enter the name: ")
age=int(input("Enter the age"))
gender=input("Enter gender")
if(age>=18 and age<30 and gender=="M"):
    print("The wages will be Rs 700 per day")
if(age>=18 and age<30 and gender=="F"):
    print("The wages will be Rs 750 per day")
if(age>=30 and age<=40 and gender=="M"):
    print("The wages will be Rs 800 per day")
if(age>=30 and age<=40 and gender=="F"):   
    print("The wages will be Rs 800 per day")