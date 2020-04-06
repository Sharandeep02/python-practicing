def marks():
    mark=int(input("enter marks of student:"))
    if (mark == 0):
        print("Absent")
    elif (mark  <40):
        print("grade:F,points:0")
    elif mark in range(40,45):
        print("grade:P,points:4")
    elif mark in range(45,50):
        print("grade:C,points:5")
    elif mark in range(50,60):
        print("grade:B,points:6")
    elif mark in range(60,70):
        print("grade:B+,points:7")
    elif mark in range(70,80):
        print("grade:A,points:8")
    elif mark in range(80,90):
        print("grade:A+,points:9")
    elif mark in range(90,101):
        print("grade:O,points:10")
marks()





























    






































    
    
