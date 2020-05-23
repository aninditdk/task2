#Program to create simple calculator in Python which on input of 1,2,3,4 should add , subtract , multiply and divide respectively.

num1=int(input())
num2=int(input())

choice=int(input())

if choice == 1:
    result = num1 + num2
elif choice == 2:
    result = num1 - num2
elif choice == 3:
    result = num1 * num2
elif choice == 4:
    result = num1 / num2
print(result)
