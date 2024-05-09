'''
    Statistics are often calculated with varying amounts of input data.
    Write a program that takes any number of integers as input, and outputs the average and max.
        Ex: If the input is:
            15 20 0 5
        the output is:
            10 20
Note: For output, round the average to the nearest integer.
'''

user_input = input("Enter your numbers: ")
numbers = user_input.split(' ')

total = 0
max = 0
for number in numbers:
    total += int(number)
    if int(number) > max:
        max = int(number)

average = total / len(numbers)
print(f'The average is: {int(average)}')
print("The max is: ", max)
