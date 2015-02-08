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


    def test_basic (self):
        
        #logging.basicConfig( stream=sys.stderr ) 
        #log = logging.getLogger( "astroplpython.function.signal" )
        #log.setLevel (logging.DEBUG)
#        logging.getLogger( "astroplpython.function.signal" ).setLevel(logging.DEBUG) 

        import numpy as np
        
        # generates 100 evenly spaced points between 1 and 1000
        time = np.linspace(1, 1000, 100)

        # computes the sine value of each of those points
        mags = np.sin(2 * time)
        
        data = []
        i = 0
        for m in mags:
            data.append(x_t(m,time[i])) 
            i = i+1
        
        p_f_list = LSPeriodogram.calculate(data,0.1,10.0,4)
        
        # get testable 
        plist = []
        for pf in p_f_list:
            plist.append(pf.power) 
        
        pgram = np.asarray(plist)
            
        # returns the inverse of the frequence (i.e. the period) of the largest periodogram value
        # generates 1000 frequencies between 0.01 and 1
        freqs = np.linspace(0.01, 3, 3000)
#        print "1/pi" + str(1/(np.pi))
        max_freq = freqs[np.argmax(pgram)]
        print("Frequency = " + str(max_freq))

        self.assertEqual(max_freq, (1/np.pi), "Peak power freq as expected")
        
#        freqs = np.linspace(0.01, 1, 1000)
#        test = 1/freqs[np.argmax(pgram)]
#        print ("TEST: "+test)
        
        self.assertEqual(12, len(pgram), "Output PGram has correct number of data points")

if __name__ == "__main__":
    import sys; sys.argv = ['', 'TestLSPeriodogram.testBasic']
    unittest.main()
    
    