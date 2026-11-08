
rowsA = int(input('Enter rows for Matrix A: '))
columnsA = int(input('Enter columns for Matrix A: '))

print()

rowsB = int(input('Enter rows for Matrix B: '))
columnsB = int(input('Enter columns for Matrix B: '))

print()

if columnsA != rowsB:
    print('Matrix multiplication is not possible.')
    print('Number of columns in Matrix A must equal number of rows in Matrix B.')

else:
    print('Enter Matrix A values (comma-separated):')
    valuesA = input().split(',')

    print()
    print('Enter Matrix B values (comma-separated):')
    valuesB = input().split(',')

    matrixA = []
    matrixB = []

    index = 0

    for i in range(rowsA):
        row = []
        for j in range(columnsA):
            row.append(int(valuesA[index]))
            index += 1
        matrixA.append(row)

    index = 0

    for i in range(rowsB):
        row = []
        for j in range(columnsB):
            row.append(int(valuesB[index]))
            index += 1
        matrixB.append(row)

    print()
    print('Matrix A:')

    for i in range(rowsA):
        for j in range(columnsA):
            print(matrixA[i][j], end=' ')
        print()

    print()
    print('Matrix B:')

    for i in range(rowsB):
        for j in range(columnsB):
            print(matrixB[i][j], end=' ')
        print()

    result = []

    for i in range(rowsA):
        row = []

        for j in range(columnsB):
            total = 0

            for k in range(columnsA):
                total += matrixA[i][k] * matrixB[k][j]

            row.append(total)

        result.append(row)

    print()
    print('Resulting Matrix:')

    for i in range(rowsA):
        for j in range(columnsB):
            print(result[i][j], end=' ')
        print()
