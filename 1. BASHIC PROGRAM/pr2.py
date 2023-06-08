''' Write a Python program to calculate the surface volume and area of a cylinder.
Formula: 
Volume = pi * radius * radius * height 
Surface area of a cylinder = ((2*pi*radius)*height) + ((pi*radius**2)*2)'''

radius = int (input ('Enter radius of a cylinder:'))
height = int (input ('Enter height of a cylinder:'))
pi=3.14
Volume = pi * radius * radius * height 
area = ((2*pi*radius)*height) + ((pi*radius**2)*2)
print(Volume)
print(area) 
