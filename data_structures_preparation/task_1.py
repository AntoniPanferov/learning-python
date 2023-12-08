# Input the list. The output shows that the list contains integers and no strings.
# Reverse the list so that the first element is swapped with the last element in the list,
# the second element with the second-to-last element, and so on. Display the modified list in the console.

numbers = [int(i) for i in input("Please enter several integers, separating them with whitespaces: ").split()]
print(f"Original list: {numbers}")
print(f"Reversed list: {numbers[::-1]}")
