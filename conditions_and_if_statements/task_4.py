# Write a program that outputs the month names "January" to "December" when the numbers 1 to 12 are entered.
# For other numbers entered, the message "Number outside the allowed range!" should be displayed.
# NOTE: I have to use if-statements due to the theme,
#       but I decided to implement it with an array because it's more elegant.

months = ("January", "February", "March", "April", "May", "June",
          "July", "August","September", "October", "November", "December")
month_number = int(input("Enter a whole number 1 to 12: "))

if 1 <= month_number <= 12:
    month_name = months[month_number - 1]
    print(f"The month corresponding to {month_number} is {month_name}.")
else:
    print("Number outside the allowed range!")
