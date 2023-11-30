# A program is intended to calculate the sum of natural numbers up to a limit 'g'
# (provided by the user via the console) according to the following rule:
# Sum = 1+2+3+4+...+n
# With sum <=g.
# Console output: Limit, number of steps, and sum.

limit = int(input("Enter the limit: "))
result = 0
steps = 0

while result + steps + 1 <= limit:
    steps += 1
    result += steps

print(f"Limit: {limit}; Number of steps: {steps}; Sum: {result}")
