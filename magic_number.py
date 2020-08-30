num = int(input("enter the number "))
sum = 0
while (num > 0 or sum > 9):
    if num == 0:
        num = sum
        sum = 0
    sum = sum+(num % 10)
    num //= 10
if sum == 1:
    print("magic number")
else:
    print("not a magic number")
