import unittest
from subtractor.diff_calc import diff


class TestSubtract(unittest.TestCase):
    def test_int_int(self):
        """
        Test that we can subtract two integers
        """
        self.assertEqual(diff(9, 10), -1)
        self.assertEqual(diff(5, 3), 2)
        self.assertEqual(diff(12, 2), 10)

    def test_float_float(self):
        """
        Test that diff can subtract two floats
        """
        self.assertEqual(diff(9.0, 10.0), -1.0)
        self.assertEqual(diff(3.1, 0.6), 2.5)
        self.assertEqual(diff(1.2, 1.0), 0.2)

    def test_mixed_input(self):
        """
        Test that diff can subtract ints and floats
        """
        self.assertEqual(diff(9.0, 10), -1.0)
        self.assertEqual(diff(3, 0.6), 2.4)

    def test_single_arg(self):
        """
        Tests what happens when one argument is given
        """
        self.assertEqual(diff(4), 4)
        self.assertEqual(diff(6.3), 6.3)

    def test_errors(self):
        """
        Test that insensible input gives the right error
        """
        self.assertRaises(ValueError, diff, "hi", 6)
        self.assertRaises(ValueError, diff, 2., "bonjour")
        self.assertRaises(ValueError, diff, "hola")


if __name__ == '__main__':
    unittest.main(verbosity=2)
