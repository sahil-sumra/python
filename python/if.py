age = input("enter your age : ")
age = int(age)
if age >= 18:
    print("you are an adult")
    print("you can vote")
elif age < 18 and age > 3 :
    print("you are in school") 

else:
    print ("you are kid")