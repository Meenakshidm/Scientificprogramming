X = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]
Y = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
Add_result = [[X[row][column] + Y[row][column]
               for column in range(len(X[0]))] 
               for row in range(len(X))]
Sub_result = [[X[row][column] - Y[row][column]
               for column in range(len(X[0]))] 
               for row in range(len(X))]

print("Matrix Addition")
for r in Add_result:
    print(r)

print("\nMatrix Subtraction")
for r in Sub_result:
    print(r)  