num = int(input("enter the number "))
number = num
sum = 0
while num > 0:
    temp = num % 10
    sum = sum+temp**3
    num = num//10

if number == sum:
    print(number, "is Amstrong")

else:
    print(number, "is not amstrong number")
