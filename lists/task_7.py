# Determine and print the count of distinct elements in a list of numbers,
# where the elements are sorted ind ascending order.

numbers = [1, 1, 2, 2, 2, 2, 3, 4, 5, 5, 6, 7, 9, 25]
unique_numbers = []
count = len([unique_numbers.append(number) for number in numbers if number not in unique_numbers])
print(count)
