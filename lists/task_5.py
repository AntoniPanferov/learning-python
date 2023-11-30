# Determine and print, in a list of numbers, the count of elements that are greater than both of their neighbors.
# The first and last elements of the list should not be considered as they do not have two neighbors.

numbers = [1, 5, 1, 5, 1, 2, 3, 2, 4, 20, 21, 5]
count = sum(1 for i in range(1, len(numbers) - 1) if numbers[i - 1] < numbers[i] > numbers[i + 1])
print(count)
