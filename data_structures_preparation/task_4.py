# Write a program where the user inputs integer numbers. These numbers are managed within a tuple.
# Your program allows the user to input the elements of the tuple via the console. In this process,
# the user enters all values of the tuple separated by spaces at once. All entered values are to be managed
# as integers within the tuple. Display the following elements from the tuple using slicing.
# Control structures such as for, range, while, etc., are not allowed.

numbers = tuple(int(i) for i in input("Please enter several integers, separating them with whitespaces: ").split())

print(f"Second element: {numbers[1]}")
print(f"Penultimate element: {numbers[-2]}")
print(f"Second to penultimate: {numbers[1:-1]}")
print(f"All elements on even index: {numbers[::2]}")
print(f"All elements on odd index: {numbers[1::2]}")
