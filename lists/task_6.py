# Given is a list of numbers. Determine the element in the list with the highest value.
# Print the value of the highest element and then its index number.
# If the highest element is not unique, print the index of the first instance.

numbers = [1, 2, 3, 4, 5, 6, 6, 3, 2, 6]

highest_value = max(numbers)
index = min(i for i in range(0, len(numbers)) if numbers[i] == highest_value)
print(f"Value: {highest_value}; Index: {index}")
