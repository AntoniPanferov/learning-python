# Search and print, in a list of numbers, all elements that are greater than the previous element.

numbers = [1, 2, 3, 50, 20, 25, 32, 23, 40, 200]
greater_than_previous = [numbers[i] for i in range(1, len(numbers)) if numbers[i] > numbers[i - 1]]
print(greater_than_previous)
