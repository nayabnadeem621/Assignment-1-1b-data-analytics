# # Q1

print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

# Q2
import sys
print("Python version:", sys.version)
print("Python Version info. :", sys.version_info)

# Q3

import datetime
now= datetime.datetime.now()
print ("Current date and Time:") 
print (now.strftime("%d-%m-%Y %H:%M:%S"))

# Q4

from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))


# Q5
first_name =(input("your first name: "))
last_name =(input("your last name: "))
print(last_name, first_name)

# Q 6

first_num = int(input("first number:" ))
sec_num = int(input("second number:" ))
total = first_num + sec_num

print (total)

#or

fname =(input("your first name: ", ))
lname =(input("your last name: "))
full_name= fname+" "+lname
print(full_name)

# Q7


print("input marks obtained in 5 different subjects")
maths= int(input("Input Maths marks: "))
Isl= int(input("Input Islamiat marks: "))
english= int(input("Input English marks: "))
computer= int(input("Input computer marks: "))
urdu= int(input("Input urdu marks: "))

obtained_marks= maths+ Isl+ english
total_marks= 300

perc = int((obtained_marks/total_marks*100))

if perc <=100 and perc >=80:
    print("Your Grade is A+ and your percentage is", perc)
elif perc <80 and perc >=70:
    print("Your Grade is A and your percentage is", perc)
elif perc <70 and perc >=60:
    print("Your Grade is B and your percentage is", perc)
elif perc <60 and perc >=50:
    print("Your Grade is C and your percentage is", perc)
elif perc <50 and perc >=40:
    print("Your Grade is D and your percentage is", perc)
elif perc <40 and perc >=33:
    print("Your Grade is E and your percentage is", perc)
elif perc > 100 or perc < 0:
    print("This is an inappropriate percentage please input correct marks")
else:
    print("fail")



# Q 8

num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")

