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
    counter = 0
    for result in result_matrix:
        if result == -1:
            counter += 1
        if counter == 2:
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


def reduction_of_rows(matrix_of_path):
    di = find_minimum_on_rows(matrix_of_path)
    for x in range(len(matrix_of_path)):
        if di[x] == float('inf'):
            continue
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


def reduction_of_columns(matrix_of_path):
    dj = find_minimum_on_column(matrix_of_path)
    for x in range(len(matrix_of_path)):
        if dj[x] == float('inf'):
            continue
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
        if matrix_of_path[x][point[1]] == 0:
            continue
        if matrix_of_path[x][point[1]] < min_of_column:
            min_of_column = matrix_of_path[x][point[1]]
    min_of_row = float('inf')
    for y in range(len(matrix_of_path)):
        if matrix_of_path[point[0]][y] == 0:
            continue
        if matrix_of_path[point[0]][y] < min_of_row:
            min_of_row = matrix_of_path[point[0]][y]
    return min_of_column + min_of_row


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


def block_row(matrix_of_path, row_index):
    matrix_of_path[row_index] = [float('inf')] * len(matrix_of_path)


def block_column(matrix_of_path, column_index):
    for x in range(len(matrix_of_path)):
        matrix_of_path[x][column_index] = float('inf')


def create_voyager_problem_solution(result_matrix):
    index = result_matrix.index(-1)
    voyager_problem_solution = [index, result_matrix.index(index)]
    for x in range(len(result_matrix) - 2):
        voyager_problem_solution.append(result_matrix.index(voyager_problem_solution[-1]))
    voyager_problem_solution.append(voyager_problem_solution[0])
    return reversed(voyager_problem_solution)


def reduction_of_matrix(matrix_of_path, result_matrix):
    dot = find_maximum_null_dots(matrix_of_path)
    result_matrix[dot[0]] = dot[1]
    block_row(matrix_of_path, dot[0])
    block_column(matrix_of_path, dot[1])
    matrix_of_path[dot[1]][dot[0]] = float('inf')


def solve_voyager_problem(matrix_of_path):
    result_matrix = [-1] * len(matrix_of_path)
    while not is_path_done(result_matrix):
        reduction_of_rows(matrix_of_path)
        reduction_of_columns(matrix_of_path)
        reduction_of_matrix(matrix_of_path, result_matrix)
    return create_voyager_problem_solution(result_matrix)


def show_voyager_problem_solution(voyager_problem_solution):
    print("Розв'язок задачі комівояжера: ")
    for solution in voyager_problem_solution:
        print(solution + 1, end="->")


distanceMatrix = [[float('inf'), 5, 11, 9],
                  [10, float('inf'), 8, 7],
                  [7, 14, float('inf'), 8],
                  [12, 6, 15, float('inf')]]

show_voyager_problem_solution(solve_voyager_problem(distance_matrix(get_data())))
