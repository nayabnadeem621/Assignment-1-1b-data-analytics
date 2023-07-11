
print("input marks obtained in maths, islamiat and english")
maths= int(input("Input Maths marks: "))
Isl= int(input("Input Islamiat marks: "))
english= int(input("Input English marks: "))

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

