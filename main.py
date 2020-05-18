import math


def get_data():
    data = []
    with open("input.txt") as iFile:
        while True:
            line = iFile.readline()
            if not line:
                break
            temp = list(map(int, (line[:len(line)] + line[len(line) + 1:]).split()))
            data.append(temp)
    del data[0]
    return data


def theorem_of_pifagor(dot1, dot2):
    return math.sqrt(math.pow(dot1[0] - dot2[0], 2) + math.pow(dot1[1] - dot2[1], 2))


def distance_matrix(e_data):
    size = len(e_data)
    matrix = [float('inf')] * size
    for x in range(size):
        matrix[x] = [float('inf')] * size
    for i in range(size):
        for j in range(size):
            if i == j:
                continue
            matrix[i][j] = theorem_of_pifagor(e_data[i], e_data[j])
    return matrix


def is_path_done(result_matrix):
    for result in result_matrix:
        if result == -1:
            return False
    return True


def find_minimum_on_rows(matrix_of_path):
    di = []
    for row in matrix_of_path:
        min_element = row[0]
        for element in row:
            if element < min_element:
                min_element = element
        di.append(min_element)
    return di


def reduction_of_rows(matrix_of_path, di):
    for x in range(len(matrix_of_path)):
        for y in range(len(matrix_of_path)):
            matrix_of_path[x][y] -= di[x]


def find_minimum_on_column(matrix_of_path):
    dj = []
    for x in range(len(matrix_of_path)):
        min_element = matrix_of_path[0][x]
        for y in range(len(matrix_of_path)):
            if matrix_of_path[y][x] < min_element:
                min_element = matrix_of_path[y][x]
        dj.append(min_element)
    return dj


def reduction_of_columns(matrix_of_path, dj):
    for x in range(len(matrix_of_path)):
        for y in range(len(matrix_of_path)):
            matrix_of_path[y][x] -= dj[x]


def find_null_dots(matrix_of_path):
    array_of_null_dots = []
    for x in range(len(matrix_of_path)):
        for y in range(len(matrix_of_path)):
            if matrix_of_path[x][y] == 0:
                array_of_null_dots.append([x, y])
    return array_of_null_dots


def find_mark(matrix_of_path, point):
    min_of_column = float('inf')
    for x in range(len(matrix_of_path)):
        if matrix_of_path[x][point[0]] < min_of_column:
            min_of_column = matrix_of_path[x][point[0]]
    return min(matrix_of_path[point[0]]) + min_of_column


def find_maximum_null_dots(matrix_of_path):
    array_of_null_dots = find_null_dots(matrix_of_path)
    mark = find_mark(matrix_of_path, array_of_null_dots[0])
    dot = array_of_null_dots[0]
    for null_dot in array_of_null_dots:
        temp_mark = find_mark(matrix_of_path, null_dot)
        if temp_mark > mark:
            mark = temp_mark
            dot = null_dot
    return dot


def solve_voyager_problem(matrix_of_path):
    result_matrix = [-1] * len(matrix_of_path)
    while not is_path_done(result_matrix):
        di = find_minimum_on_rows(matrix_of_path)
        reduction_of_rows(matrix_of_path, di)
        dj = find_minimum_on_column(matrix_of_path)
        reduction_of_columns(matrix_of_path, dj)
