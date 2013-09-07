import sys


class QueryBoard(object):
    def __init__(self, size):
        self.size = size
        self.matrix = []

        self.generate_matrix()

    def generate_matrix(self):
        for i in xrange(self.size):
            row = []
            for j in xrange(self.size):
                row.append(0)
            self.matrix.append(row)

    def set_row(self, row, value):
        for i in xrange(self.size):
            self.matrix[row][i] = value

    def set_col(self, col, value):
        for i in xrange(self.size):
            self.matrix[i][col] = value

    def query_row(self, row):
        result = 0
        for i in xrange(self.size):
            result += self.matrix[row][i]

        return result

    def query_col(self, col):
        result = 0

        for i in xrange(self.size):
            result += self.matrix[i][col]

        return result


if __name__ == '__main__':
    query_board = QueryBoard(size=256)

    with open(sys.argv[1]) as tests_handle:
        for line in tests_handle.readlines():
            args = line.strip().split(' ')

            if args[0] == 'SetCol':
                col, value = int(args[1]), int(args[2])
                query_board.set_col(col, value)
            elif args[0] == 'SetRow':
                row, value = int(args[1]), int(args[2])
                query_board.set_row(row, value)
            elif args[0] == 'QueryCol':
                col = int(args[1])
                print query_board.query_col(col)
            elif args[0] == 'QueryRow':
                row = int(args[1])
                print query_board.query_row(row)
