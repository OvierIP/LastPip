import unittest
from desoper import SecondPip


class Test_hello(unittest.TestCase):
    def test__working(self):
        self.assertEqual(SecondPip.hello(),
                         'Hello, World!', True)


if __name__ == '__main__':
    unittest.main()
