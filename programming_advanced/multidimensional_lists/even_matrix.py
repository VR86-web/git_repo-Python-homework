rows = int(input())
even_matrix = []

for i in range(rows):
    numbers = [int(x) for x in input().split(", ") if int(x) % 2 == 0]
    even_matrix.append(numbers)

print(even_matrix)
