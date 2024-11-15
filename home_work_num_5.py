#START Question 1
movie: int = int(input("how long is the movie ? "))

hours: int = movie// 60
minutes: int = movie % 60

print(f"hours: {hours}, minutes: {minutes}.")
#END

#START Question 2
for i in range(0, 11):
    print(i, end=" ")
print("")

for i in range(40, 89, 2):
    print(i, end=" ")
print(" ")

for i in range(77, 106):
    if i % 7 == 0:
        print(i, end=" ")

for i in range(99, 65, -1):
    if i % 3 == 0:
        print(i, end=" ")
#END

#START Question C1
while True:
    height: float = float(input("Enter your height (in centimeters): "))
    if 0.4 <= height <= 2.5:
        break
    print("input wrong")
#END

#START Question C2
num1: int = int(input("Enter a first number:"))
num2: int = int(input("Enter a second number:"))

if num1 < num2:
    for i in range(num1, num2 + 1):
        print(i, end=" ")
else:
    for i in range(num1, num2 - 1, -1):
        print(i, end=" ")
print()
#END

#START Question C3
pie: float = 3.14
attempts: int = 3

for i in range(attempts):
    user_answer: float = float(input("Enter how much is a pie worth?"))
    if user_answer == pie:
        print("Correct are you")
        break
else:
    print("3.14 is pie")

#END

#START Question C4
while True:
    num1: int = int(input("Enter a number:"))
    num2: int = int(input("Enter a number:"))
    num3: int = int(input("Enter a number:"))

    if 0 <= num1 <= 10 and 10 <= num2 <= 60 and  60 <= num3 <= 100 and num2 == (num1 + num2 + num3) / 3:
        break
    print("Try again...")
#END

#START Question 4
beers: int = 10

while beers > 0:
    age = int(input("What is your age? "))
    if age >= 18:
        beers -= 1
    else:
        print("Only from the age of 18 can you get beer, try again")

print("Out of beers!")
#END
