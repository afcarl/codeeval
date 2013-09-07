import unittest

from hextodec import hex_to_decimal


class ModTestCase(unittest.TestCase):
    def test_mod(self):
        self.assertEqual(159, hex_to_decimal('9f'))
        self.assertEqual(17, hex_to_decimal('11'))
        self.assertEqual(39619, hex_to_decimal('9AC3'))

if __name__ == '__main__':
    unittest.main()
