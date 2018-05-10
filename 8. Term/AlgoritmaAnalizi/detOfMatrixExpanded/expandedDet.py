import random


def fillMatrix(i, j):
    m = [[random.randint(0, 10) for a in range(i)] for b in range(j)]
    return m


def expandedMatrix(s):
    expanded = s
    for i in range(len(s)-1):
        expanded.append(s[i])
    return expanded


def getDeterminantofMatrix(matrix, s):
    totalRight = 0
    totalLeft = 0
    tempRight = 1
    tempLeft = 1
    matrix = expandedMatrix(matrix)

    if s == 2:
        for i in range(2):
            tempRight *= matrix[i][i]
            tempLeft *= matrix[i][1-i]
        totalRight = tempRight
        totalLeft = tempLeft
    else:
        for i in range(s):
            for j in range(s):
                tempRight *= matrix[i+j][j]
                tempLeft *= matrix[i+j][s-j-1]
            totalRight += tempRight
            totalLeft += tempLeft
            tempRight = 1
            tempLeft = 1
    return totalRight-totalLeft


def main():
    s = int(input("NxN matris oluşturmak için boyut girin: "))
    print("Matris oluşturuluyor...")
    m = fillMatrix(s, s)
    print("Oluşturulan matris:")
    for i in range(s):
        print(m[i])
    print("Oluşturulan matrisin determinantı: {}".format(getDeterminantofMatrix(m, s)))


if __name__ == "__main__":
    main()

