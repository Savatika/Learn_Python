# print_operation_table(operation, num_rows=6, num_columns=6)
operation = lambda x,y: x+y
def print_operation_table(operation, rows=6, colums=6):
    for i in range(1, rows + 1):
        print('\n')
        for j in range(1, colums + 1):
            print(operation(i, j), end = (' '))
print_operation_table(operation, 6, 6)