'''
Created on Jul 16, 2014

@author: thomas
'''
import unittest
import logging

from astroplpython.function.signal.LSPeriodogram import LSPeriodogram
from astroplpython.data.TimeMeasurement import x_t

class TestLSPeriodogramTestCase (unittest.TestCase):

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_basic (self):
        
        logging.getLogger( "astroplpython.proc" ).setLevel(logging.DEBUG)   
        
        data = []
        data.append(x_t(0,0))
        data.append(x_t(0,1))
        data.append(x_t(0,2))
        
        pgram = LSPeriodogram.calculate(data,0.1,10.0,4)
        ' use debugging logging for tests '
#        lsp.debug()
        
#        pgram = lsp.pgram(0.1,10,4)
        self.assertEqual(12, len(pgram), "Output PGram has correct number of data points")

if __name__ == "__main__":
    import sys; sys.argv = ['', 'TestLSPeriodogram.testBasic']
    unittest.main()
    
    