#Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
#которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
#Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией называется любая операция, 
#у которой ровно два аргумента, как, например, у операции умножения.

def print_operation_table(operation, num_rows=6, num_columns=6):
    a = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
    for i in a:
        print(*[f"{x:>3}" for x in i])

print_operation_table(lambda x, y: x * y)