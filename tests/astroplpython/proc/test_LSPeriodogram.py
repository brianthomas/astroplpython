'''
Created on Jul 16, 2014

@author: thomas
'''
import unittest

from astroplpython.proc.LSPeriodogram import LSPeriodogram
from astroplpython.data.Timeseries import x_t

class TestLSPeriodogramTestCase (unittest.TestCase):

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_basic (self):
        data = []
        data.append(x_t(0,0))
        data.append(x_t(0,1))
        data.append(x_t(0,2))
        lsp = LSPeriodogram(data, 1, 1)
        pgram = lsp.pgram()
        self.assertEqual(3, len(pgram), "Output PGram has correct number of data points")

if __name__ == "__main__":
    import sys; sys.argv = ['', 'TestLSPeriodogram.testBasic']
    unittest.main()
    
    