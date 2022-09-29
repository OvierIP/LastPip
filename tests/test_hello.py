import unittest
from desoper import SecondPip


class Test_hello(unittest.TestCase):
    def test__working(self):
        self.assertEqual(SecondPip.hello(),
                         1, 1, True)


if __name__ == '__main__':
    unittest.main()
