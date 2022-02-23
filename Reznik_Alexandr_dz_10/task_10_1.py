from typing import List


class Matrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        m_rows = len(self.matrix)
        self.__matrix_size = frozenset([(m_rows, len(row)) for row in self.matrix])

        if len(self.__matrix_size) != 1:
            raise ValueError("Fail initialization matrix")

    def __str__(self):
        result = ''
        for i in range(len(self.matrix)):
            result = result + '|' + '\t'.join(map(str, self.matrix[i])) + '|' + '\n'
        return result

    def __add__(self, other):
        result = []
        for item in zip(self.matrix, other.matrix):
            result.append([sum([j, k]) for j, k in zip(*item)])
        return Matrix(result)


first_matrix = Matrix([[1, 2], [3, 4], [5, 6]])
second_matrix = Matrix([[6, 5], [4, 3], [2, 1]])
print(first_matrix)
print(second_matrix)
print(first_matrix + second_matrix)
fail_matrix = Matrix([[1, 2], [3, 4, 7], [5, 6]])
print(fail_matrix)

# |1	2|
# |3	4|
# |5	6|
#
# |6	5|
# |4	3|
# |2	1|
#
# |7	7|
# |7	7|
# |7	7|
#
# Traceback (most recent call last):
#   File "C:\PythonProjects\pythonProject\Python_tasks.git\Reznik_Alexandr_dz_10\task_10_1.py", line 32, in <module>
#     fail_matrix = Matrix([[1, 2], [3, 4, 7], [5, 6]])
#   File "C:\PythonProjects\pythonProject\Python_tasks.git\Reznik_Alexandr_dz_10\task_10_1.py", line 11, in __init__
#     raise ValueError("Fail initialization matrix")
# ValueError: Fail initialization matrix
