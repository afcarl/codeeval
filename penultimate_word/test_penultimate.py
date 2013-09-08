import unittest

from penultimate import penultimate_word


class PenultimateTestCase(unittest.TestCase):
    def test_penultimate_word(self):
        self.assertEqual('with', penultimate_word('some line with text'))
        self.assertEqual('another', penultimate_word('another line'))


if __name__ == '__main__':
    unittest.main()
