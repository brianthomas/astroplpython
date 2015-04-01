'''
Created on Jul 16, 2014

@author: thomas
'''
import unittest

from astroplpython.function.signal.LSPeriodogram import LSPeriodogram
from astroplpython.data.TimeMeasurement import x_t

class TestLSPeriodogramTestCase (unittest.TestCase):

    def setUp(self):
        pass


    def tearDown(self):
        pass
    
    def test_calculate (self):
       
        ''' 
        test calculate static method
        '''
        import logging 
        import sys
        logging.basicConfig(stream=sys.stderr)
        logging.getLogger( "astroplpython.function.signal" ).setLevel(logging.DEBUG) 

        import numpy as np
        
        f_low = 0.01
        f_high = 3.0
        f_over = 30
        
        # generates 100 evenly spaced points between 1 and 1000
        time = np.linspace(1, 1000, 100)

        # computes the sine value of each of those points
        mags = np.sin(time)
        
        data = []
        i = 0
        for t in time:
            data.append(x_t(mags[i],t)) 
            i = i+1
        
        p_f_list = LSPeriodogram.calculate(data, f_low, f_high, f_over)
        
        # get testable 
        plist = []
        for pf in p_f_list:
            plist.append(pf.power) 
        
        pgram = np.asarray(plist)
            
        #self.assertEqual((nr_points*f_over), len(pgram), "Output PGram has correct number of data points")
        
        # returns the inverse of the frequency (i.e. the period) of the largest periodogram value
        # generates 1000 frequencies between 0.01 and 1
#        freqs = np.linspace(f_low, f_high, 3000) #nr_points*f_over)
        freqs = np.linspace(0.01, 3.0, 3000) #nr_points*f_over)
        max_freq = freqs[np.argmax(pgram)] / np.pi
        
        print("Frequency = " + str(max_freq))
        print(" 1/pi = " + str(1/np.pi))

        self.assertEqual(round(max_freq, 4), round((1/np.pi), 4), "Peak power freq as expected")

if __name__ == "__main__":
    import sys; sys.argv = ['', 'TestLSPeriodogram.testBasic']
    unittest.main()
    
    