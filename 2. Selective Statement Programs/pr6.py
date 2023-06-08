''' A Rotary Club has decided to conduct a blood donation camp. The eligibility criteria for the blood donation camp will be that the person should be above 18 and his or her weight should be above 40. The volunteers will enter the name, age, and weight of the person, and then it will display whether they are eligible or not.
Display "1" if they are eligible and "0" if they are not eligible.'''

name =input('Enter the name of volunteers: ')
age =int( input('Enter the volunteers age: '))
weight =int(input('Enter the weight: '))
if(age>18 and weight>40):
    print("1")
else:
    print("0")