def city():
    name=input("enter the name of person:")
    gender=input("enter the gender of person ")
    age=int(input("enter the age of person"))
    if (gender =='F' and age>=58):
        print("she is a senior citizen")
    elif (gender == 'M' and  age>=60):
        print("he is a senior citizen")
    elif (gender == 'F' and age<58):
        print("she is not a senior citizen")
    elif (gender == 'M' and age<60):


        print("he is not a senior citizen")
city()
