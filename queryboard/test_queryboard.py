import unittest

from queryboard import QueryBoard


class QueryBoardTestCase(unittest.TestCase):
    def setUp(self):
        self.query_board = QueryBoard(size=256)

    def test_query_board(self):
        self.query_board.set_col(32, 20)
        self.query_board.set_row(15, 7)
        self.query_board.set_row(16, 31)
        self.assertEqual(5118, self.query_board.query_col(32))

        self.query_board.set_col(2, 14)
        self.assertEqual(34, self.query_board.query_row(10))

        self.query_board.set_col(14, 0)
        self.assertEqual(1792, self.query_board.query_row(15))

        self.query_board.set_row(10, 1)
        self.assertEqual(3571, self.query_board.query_col(2))

if __name__ == '__main__':
    unittest.main()
