X = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]
Y = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

rmatrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for row in range(len(X)):
    for column in range(len(X[0])):
        rmatrix[row][column] = X[row][column] * Y[row][column]
        
print("Matrix Multiplication",)
for r in rmatrix:
    print(r)
        
for i in range(len(X)):
    for j in range(len(X[0])):
        rmatrix[row][column] = X[row][column] // Y[row][column]

print("\nMatrix Division",)   
for r in rmatrix:
    print(r) 