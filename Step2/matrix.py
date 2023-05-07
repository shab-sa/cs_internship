class Matrix:
    def __init__(self, matrix_string):
        self.matrix=[]
        rows=matrix_string.split('\n')
        for row in rows:
            self.matrix.append(list(map(int, row.split())))

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        return [i[index-1] for i in self.matrix]
