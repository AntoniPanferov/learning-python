# The application reads an integer from the console and checks whether it is
# greater, smaller or equal to 0. It then outputs whether the number is even or odd.

number = int(input("Enter a whole number: "))
if number < 0:
    print(f"{number} is smaller than 0", end=" ")
elif number > 0:
    print(f"{number} is greater than 0", end=" ")
else:
    print("Number is equal to 0", end=" ")

print("and even.") if number % 2 == 0 else print("add odd.")
