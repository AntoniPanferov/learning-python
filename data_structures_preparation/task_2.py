# Write a program that finds the common elements of two lists, A and B, and outputs them in the console as a list.
# Duplicates in a list are only recorded once. Your program allows the user to input elements of lists A and B
# via the console. In this process, the user enters all values of the respective list separated by spaces at once.
# All entered values are to be managed as integers in a list.

A = [int(i) for i in input("Please enter several integers, separating them with whitespaces: ").split()]
B = [int(i) for i in input("Please enter several integers, separating them with whitespaces: ").split()]

C = []

for number in A:
    if number in B and number not in C:
        C.append(number)


print(f"Result: {C}")
