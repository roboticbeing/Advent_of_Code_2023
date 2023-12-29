# What is the sum of all the calibration values?

# Add the input file into a list
input_file = open('input.txt', 'r')
first = ''
last = ''
sum = 0

for word in input_file:
    for char in word:
        if char.isdigit():
            if first == '':
                first = char
            last = char
        if char == "\n":
            num = first + last
            first = ''
            sum += int(num)
print(sum)

