numbers = [1,4,6,45,3,7,22,55,4,0]
largest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number
print(largest)