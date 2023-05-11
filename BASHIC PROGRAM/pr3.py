'''Write a Python program to calculate the wind chill index.
The given program calculates the wind chill index using the temperature and wind speed entered by the user. The wind chill index is an estimate of how cold the air feels to the human body, taking into account the cooling effect of the wind on the skin.
prompts the user to enter the wind speed in kilometers per hour and the temperature in degrees Celsius using the input() function.
The program calculates the wind chill index using the formula:
13.12 + 0.6215*t - 11.37*v**0.16 + 0.3965*t*v**0.16
where t is the temperature in degrees Celsius and v is the wind speed in kilometers per hour. 
Output
The calculated wind chill index is then rounded to the nearest integer. '''


t = int (input ('Enter the temperature in degrees Celsius:'))
v = int (input ('Enter the wind speed in kilometers per hour:'))
wind_chill = 13.12 + 0.6215*t - 11.37*v**0.16 + 0.3965*t*v**0.16
print('The wind chill index is:',wind_chill)

