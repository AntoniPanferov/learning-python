# Swap pairwise neighbor elements in a list of numbers (A[0] with A[1], A[2] with A[3], etc.).
# Print the resulting list. If a list has an odd number of elements, leave the last element in its place.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(0, len(numbers) - 1, 2):
    numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
print(numbers)
