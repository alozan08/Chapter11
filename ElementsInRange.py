'''
    Write a program that first gets a list of integers from input.
    That list is followed by two more integers representing lower
    and upper bounds of a range. Your program should output all
    integers from the list that are within that range (inclusive of the bounds).
        Ex: If the input is:
            25 51 0 200 33
            0 50
        the output is:
            25 0 33
            The bounds are 0-50, so 51 and 200 are out of range and thus not output.
    For coding simplicity, follow each output integer by a space, even the last one. Do not end with newline.
'''
user_input = input("Enter your numbers: ")
numbers = user_input.split(' ')
upper_str, lower_str = input("Enter lower and upper bounds: ").split(' ')

lower = int(upper_str)
upper = int(lower_str)

for number in numbers:
    num = int(number)
    if lower <= num <= upper:
        print(num, end = ' ')