import unittest
import pandas as pd
from desoper.myfirstpypi import principal 

#test base



class Test_hello(unittest.TestCase):
    def test__working1(self):
        ls1=principal(5,9,0,30,400000)
        self.assertEqual(12,ls1.shape[0], True)

    def test__working2(self):
        ls2=principal(6,9,0,30,400000)
        self.assertEqual(141,ls2.shape[0], True)
       


if __name__ == '__main__':
    unittest.main()
