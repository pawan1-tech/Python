''' ACB, the Omni Bus Company, has decided to give a 20% traveling fare concession for senior citizens; the actual fare will be Rs 1020. The upper age limit for senior citizens is above 60. 
For verification, they will ask for the date of birth (take the year alone), and if satisfied, they will be given a concession and will be displayed the final traveling charge; if not, the original fare will be displayed. '''

Year = int(input('Enter the Year of Birth: '))
Month = int(input('Enter the Month of Birth: '))
Day = int(input('Enter the Day of Birth: '))
fare = 1020-(20/100)*1020
if((2023-Year)>=60):
    print('The fare is ',fare)
else:
    print('The fare is 1020')
