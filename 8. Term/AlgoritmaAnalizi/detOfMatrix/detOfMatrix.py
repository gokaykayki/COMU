import random

def fillMatrix(i, j):
    m = [[random.randint(0, 10) for a in range(i)] for b in range(j)]
    return m


def fillTriangleMatrix(i, j, c):
    if c == "u":
        m = [[random.randint(1, 10) if a >= b else 0 for a in range(i)] for b in range(j)]
        return m
    elif c == "l":
        m = [[random.randint(1, 10) if a <= b else 0 for a in range(i)] for b in range(j)]
        return m
    else:
        print("Invalid value. Closing program...")
        exit(1)


def getMatrixMinor(matrix, i, j):
    return [row[:j] + row[j+1:] for row in (matrix[:i]+matrix[i+1:])]


def getDeterminantofMatrix(matrix):
    # base case for 2x2 matrix
    if len(matrix) == 2:
        return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]

    det = 0
    for i in range(len(matrix)):
        det += ((-1)**i)*matrix[0][i]*getDeterminantofMatrix(getMatrixMinor(matrix, 0, i))
    return det

s = int(input("Creating nxn matrix. Please enter the value of n: "))
c = input("Normal or Triangular Matrix: Enter n or t: ")

if c == "n":
    m = fillMatrix(s, s)
elif c == "t":
    t = input("Upper of Lower Triangular: Enter u or l: ")
    m = fillTriangleMatrix(s, s, "u") if t == "u" else fillTriangleMatrix(s, s, "l")

print("Our matrix: {}".format(m))
print("Determinant of Our Matrix: {}".format(getDeterminantofMatrix(m)))
