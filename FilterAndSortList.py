'''
    Write a program that gets a list of integers from input, and outputs
    non-negative integers in ascending order (lowest to highest).
        Ex: If the input is:
            10 -7 4 39 -6 12 2
        the output is:
            2 4 10 12 39
    For coding simplicity, follow every output value by a space.
    Do not end with newline.
'''

user_input = input("Enter your numbers: ")
numbers = user_input.split(' ')
non_negative = []

for number in numbers:
    if int(number) >= 0:
        non_negative.append(int(number))

non_negative.sort()

for number in non_negative:
    print(number, end = ' ')
