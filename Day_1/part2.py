# Part 2
# What is the sum of all of the calibration values?

# Add the input file into a list
input_file = open('input.txt', 'r').read()
num_list = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
total = 0

for line in input_file.split('\n'):
    digits = []
    for i, c in enumerate(line):
        if c.isdigit():
            digits.append(c)
        for d, val in enumerate(num_list):
            if line[i:].startswith(val):
                digits.append(str(d + 1))
    total += int(digits[0] + digits[-1])
print(total)