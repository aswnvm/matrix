import numpy as np

def input_matrix(rows, cols):
    print(f"Enter elements for a {rows}x{cols} matrix:")
    matrix = []
    for i in range(rows):
        row = list(map(float, input().split()))
        if len(row) != cols:
            raise ValueError("Incorrect num of columns entered")
        matrix.append(row)
    return np.array(matrix)

def main():
    print("Matrix Operations: 1. Add  2. Subtract  3. Multiply  4. Transpose  5. Inverse  6. Determinant  7. Eigenvalues")
    choice = int(input("Enter operation num: "))
    
    if choice in [1, 2, 3]:
        rows1 = int(input("Enter num of rows for first matrix: "))
        cols1 = int(input("Enter num of cols for first matrix: "))
        matrix1 = input_matrix(rows1, cols1)
        
        rows2 = int(input("Enter num of rows for second matrix: "))
        cols2 = int(input("Enter numb of cols for second matrix: "))
        matrix2 = input_matrix(rows2, cols2)
        
        if choice == 1:
            if matrix1.shape != matrix2.shape:
                print("Error: Matrices must be of the same shape for addition.")
            else:
                print("Result of Addition:")
                print(matrix1 + matrix2)
        elif choice == 2:
            if matrix1.shape != matrix2.shape:
                print("Error: Matrices must be of the same shape for subtraction.")
            else:
                print("Result of Subtraction:")
                print(matrix1 - matrix2)
        elif choice == 3:
            if cols1 != rows2:
                print("Error: Numb of cols of first matrix must equal num of rows of second matrix for multiplication.")
            else:
                print("Result of Multiplication:")
                print(np.dot(matrix1, matrix2))
    
    elif choice == 4:
        rows = int(input("Enter num of rows: "))
        cols = int(input("Enter num of cols: "))
        matrix = input_matrix(rows, cols)
        print("Transpose:")
        print(matrix.T)
    
    elif choice == 5:
        size = int(input("Enter size of square matrix: "))
        matrix = input_matrix(size, size)
        if np.linalg.det(matrix) == 0:
            print("Error: Matrix is singular and cannot be inverted.")
        else:
            print("Inverse:")
            print(np.linalg.inv(matrix))
    
    elif choice == 6:
        size = int(input("Enter size of square matrix: "))
        matrix = input_matrix(size, size)
        print("Determinant:")
        print(np.linalg.det(matrix))
    
    elif choice == 7:
        size = int(input("Enter size of square matrix: "))
        matrix = input_matrix(size, size)
        eigenvalues, eigenvectors = np.linalg.eig(matrix)
        print("Eigenvalues:", eigenvalues)
        print("Eigenvectors:")
        print(eigenvectors)
    else:
        print("Invalid choice")
        
if __name__ == "__main__":
    main()
