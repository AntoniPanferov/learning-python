# Write a program that counts how often each element occurs in an integer list and outputs the result
# in a dictionary in the console. The key represents each element, and the value represents its frequency.
# Your program allows the user to input the elements of the list via the console. In this process,
# user enters all values of the list separated by spaces at once.

numbers = [int(i) for i in input("Please enter several integers, separating them with whitespaces: ").split()]

frequency = {}

for number in numbers:
    if number not in frequency:
        frequency[number] = 1
    else:
        frequency[number] += 1

print(f"Result: {frequency}")
