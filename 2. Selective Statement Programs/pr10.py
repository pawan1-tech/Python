''' Restaurant Tip Calculator:Steps:Ratings will be: 1 is bad, 2 is not bad, 3 is average, 4 is good, and 5 is excellent.
Read Food Rating: 1-5 
Read Service Rating: 1-5 
Read Ambience Rating: 1-5 
Read the bill's amount.
If the food is good or excellent:Service and ambience are also good or excellent.
Then the tip is 10% of your bill amount.Service and ambience are average/okay/bad.
Then the tip is 5% of your amount.If the food is average, okay, or bad:Service and ambience are also good or excellent.
Then the tip is 5% of your bill amount.Service and ambience are average/okay/bad.Then the tip is 1% of your bill amount. '''

amount=float(input("your bill amount is: "))
print(amount)
sentence=("Please give rating")
print(sentence)
food_rating=int(input("Enter the food rating: "))
service_rating=int(input("Enter the service rating: "))
ambience_rating=int(input("Enter the ambience rating: "))
if(food_rating==4 or food_rating==5 and service_rating==4 or service_rating==5 and ambience_rating==4 or ambience_rating==5):
    print("The tip amount is: ",(10/100)*amount)
elif(service_rating==1 or service_rating==2 or service_rating==3 and ambience_rating==1 or  ambience_rating==2 or  ambience_rating==3):
    print("The tip amount is: ",(5/100)*amount)
elif(food_rating==4 or food_rating==2 or food_rating==1 and service_rating==4 or service_rating==5 and ambience==4 or service_rating==5):
    print("The tip amount is: ",(5/100)*amount)
elif(service_rating==3 or service_rating==2 or service_rating==1 and ambience_rating==3 or ambience_rating==2 or ambience_rating==1):
    print("The tip amount is: ",(1/100)*amount)
    
