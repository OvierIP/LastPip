import unittest
import pandas as pd
from desoper.LastPip import solutionfinal 

#test base


class Test_hello(unittest.TestCase):
    def test__working1(self):
        ls1=solutionfinal(5)
        self.assertEqual(11,ls1.shape[0], True)

    def test__working2(self):
        ls2=solutionfinal(6)
        self.assertEqual(141,ls2.shape[0], True)
       

if __name__ == '__main__':
    unittest.main()
