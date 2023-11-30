# Write a program that outputs the reciprocal for a whole number entered via the console.
# If the entered number is equal to 0, a message should be displayed stating that no reciprocal can be formed.

number = int(input("Enter a whole number: "))
print(f"Reciprocal of {number} is {1 / number}") if number != 0 else print("There is no reciprocal for 0.")
