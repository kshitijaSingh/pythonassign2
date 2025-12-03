# task 1
# checking if the integer is odd / even using if-else statement
number = int(input("enter your number :"))
if number % 2 ==  0 :
    print(f"{number} is a even number")
elif number % 2 != 0 :
    print(f"{number} is a odd number")

# task 2
# sum of all the integers in the range from 1 to 50

sum = 0
for i in range(1,51):
    sum += i
    print(f"the total sum of the number from 1 to 50 is {sum}")