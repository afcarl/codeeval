import unittest

from capitalize import title


class CapitalizeTestCase(unittest.TestCase):
    def test_capitalize_word(self):
        self.assertEqual('Hello World', title('Hello world'))
        self.assertEqual('JavaScript Language', title('javaScript language'))
        self.assertEqual('A Letter', title('a letter'))


if __name__ == '__main__':
    unittest.main()
