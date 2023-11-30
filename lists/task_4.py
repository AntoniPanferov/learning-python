# Search in a list of numbers for the first neighbor elements that have the same sign and print them.

numbers = [-1, 2, -3, 4, -5, 6, -7, 8, 9]
for i in range(0, len(numbers) - 1):
    if numbers[i] * numbers[i + 1] > 0:
        print(f"{numbers[i]} {numbers[i + 1]}")
        break
