# Search and print, in a list of numbers, all list elements with an even index number (i.e., A[0], A[2], A[4], ...).

elements = input("Enter elements and divide them with whitespace: ").split()
even_index_elements = [elements[i] for i in range(0, len(elements), 2)]
print(f"Elements with even index: {even_index_elements}")
