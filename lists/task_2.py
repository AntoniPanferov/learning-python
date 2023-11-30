# Find all elements in a list of numbers that are even and print them. In this case,
# use a for loop that iterates over the list, not its indices! Do not use range().

numbers = [1, 2, 3, 4, 6, 9, 20, 5, 700, 8]
even_numbers = [number for number in numbers if number % 2 == 0]
print(f"Numbers: {numbers}")
print(f"Even Numbers: {even_numbers}")
