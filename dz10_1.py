class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        return '\n'.join('\t'.join([str(el) for el in line]) for line in self.my_list)

    def __add__(self, other):
        matrix = []
        for i in range(len(self.my_list)):
            matrix.append([])
            for j in range(len(self.my_list)):
                matrix[i].append(self.my_list[i][j] + other.my_list[i][j])
        return '\n'.join(map(str, matrix))


m_1 = [[4, 16, 55], [7, 12, -49], [103, -48, 0]]
m_2 = [[44, -12, 9], [78, 0, -2], [19, 1, 39]]

mat_1 = Matrix(m_1)
mat_2 = Matrix(m_2)
goal_mat = mat_1 + mat_2
print(mat_1)
print(mat_2)
print(goal_mat)
