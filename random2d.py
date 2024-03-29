import random
numbers = list(range(9))
random.shuffle(numbers)
random_3x3_matrix = [numbers[i:i+3] for i in range(0, 9, 3)]
for row in random_3x3_matrix:
    print(row)
