numbers = [5, 2, 1, 7, 3,5 , 4, 5]
solution = []

for number in numbers:
    if number not in solution:
        solution.append(number)
print(solution)