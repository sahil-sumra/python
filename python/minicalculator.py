first_number = input ("enter first number ")
operator = input("enter any operator (+ , - , / , * , %): ")
second_number = input("enter second number: ")

first_number = int(first_number) ; second_number = int(second_number)

if operator == '+':
    print("the sum is: " , first_number + second_number)
elif operator == '-':
    print("the sub is: " , first_number + second_number)
elif operator == '*':
    print("the multiplication is: " , first_number + second_number)
elif operator == '/':
    print("the div is: " , first_number + second_number)
elif operator == '%':
    print("the modulo  is: " , first_number + second_number)
else : 
    print("wrong input please try again : ")
                    