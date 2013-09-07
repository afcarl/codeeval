import unittest

from beautiful import beauty_of


class BeautyTestCase(unittest.TestCase):
    def test_beauty_of(self):
        self.assertEqual(152, beauty_of('ABbCcc'))
        self.assertEqual(754, beauty_of('Good luck in the Facebook Hacker Cup this year!'))
        self.assertEqual(491, beauty_of('Ignore punctuation, please :)'))
        self.assertEqual(729, beauty_of('Sometimes test cases are hard to make up.'))
        self.assertEqual(646, beauty_of('So I just go consult Professor Dalves'))


if __name__ == '__main__':
    unittest.main()
