import numpy as np

arr = np.array(([18, 2, 3, 4], [1, 4, 7, 6], [7, 60, 8, 18],
               [1, 1, 1, 1], [77, 11, 50, 0]))

dom_val = []
row = 5
column = 4


def neighbours(arr, _row, _column):
    if _row+_column == 0:
        a = [arr[0][1], arr[1][:2]]
        return a
    elif _row == 0 and _column != column-1:
        a = [arr[0][[_column-1, _column+1]], arr[1]
             [[_column, _column+1, _column-1]]]
        return a
    elif _row == 0 and _column == column-1:
        a = [arr[0][_column-1], arr[1][[_column-1, _column]]]
        return a
    elif _row == row-1 and _column == 0:
        a = [arr[_row][1], arr[_row-1][[_column+1, _column]]]
        return a
    elif _row == row-1 and _column != column-1:
        a = [arr[_row][[_column-1, _column+1]],
             arr[_row-1][[_column, _column+1, _column-1]]]
        return a
    elif _row == row-1 and _column == column-1:
        a = [arr[_row][_column-1], arr[_row-1][[_column-1, _column]]]
        return a
    elif _column == 0:
        a = [arr[_row-1][[_column, _column+1]], arr[_row]
             [_column+1], arr[_row+1][[_column, _column+1]]]
        return a
    elif _column == column-1:
        a = [arr[_row-1][[_column, _column-1]], arr[_row]
             [_column-1], arr[_row+1][[_column, _column-1]]]
        return a
    else:
        a = [arr[_row-1][[_column-1, _column, _column+1]], arr[_row]
             [[_column-1, _column+1]], arr[_row+1][[_column-1, _column, _column+1]]]
        return a


def neighbour_compare(r, c, neigbours):
    a = True
    for x in neigbours:
        if type(x) == np.ndarray:
            for y in x:
                if arr[r][c] <= y:
                    a = False
        else:
            if arr[r][c] <= x:
                a = False
    if a:
        dom_val.append((r, c))


for x in range(row):
    for y in range(column):
        neighbour_compare(x, y, neighbours(arr, x, y))

print("--------Dominadas-----------------------")
print("---Matriz insertada----")
print(arr)
print()
print("Resultado")
print(dom_val)
print("-------------FIN------------------------")