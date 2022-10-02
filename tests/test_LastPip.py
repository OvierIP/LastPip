import unittest
import pandas as pd
from desoper.LastPip import solutionfinal 

#test base 

class Test_hello(unittest.TestCase):
     
    def test_n5(self):
        sls_5 = solutionfinal(5)
        self.assertEqual(11, sls_5.shape[0],True)                                

    def test_n6(self):
        sls_6 = solutionfinal(6)
        self.assertEqual(112, sls_6.shape[0],True)
       

if __name__ == '__main__':
    unittest.main()
