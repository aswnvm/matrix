row = int(input("Enter row:  "))
col = int(input("Enter column:  "))
matrix=[]
for i in range(1, row+1):
  a= []
  for j in range(col):
    k = row * j+i
    a.append(k)
  matrix.append(a)

for i in range(row):
  for j in range(col):
    print(matrix[i][j], end=" ")
  print()