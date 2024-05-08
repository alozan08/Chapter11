num_resistors = 5
resistors = []
voltage_drop = []

print(f'{num_resistors} resistors are in the series.')
print('This program calculates the'),
print('voltage drop across each resistor.')

input_voltage = float(input('Input voltage applied to circuit: '))
print(input_voltage)

print(f'Input ohms of {num_resistors} resistors')
for i in range(num_resistors):
    res = float(input(f'{i + 1}) '))
    print(res)
    resistors.append(res)

#  Calculate current
current = input_voltage / sum(resistors)

# ***************** YOUR CODE *****************
# Calculate voltage drop over each resistor
for resistor in resistors:
    voltage_drop.append(resistor * current)

print('Voltage drop per resistor is:')
# Print the voltage drop per resistor
for index, voltage in enumerate(voltage_drop):
    print(f'{index+1}) {voltage:.1f} V')


