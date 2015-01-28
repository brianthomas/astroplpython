'''
Created on Jul 16, 2014

@author: thomas
'''
import unittest

from astroplpython.proc.LSPeriodogram import LSPeriodogram
from astroplpython.data.Timeseries import x_t
from astroplpython.data.Periodogram import p_f

import numpy as np
import scipy.signal as sp
import logging

class TestLSPeriodogramTestCase (unittest.TestCase):
    
    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_other (self):
        
        log = logging.getLogger( "astroplpython.proc" )
        
        log.error("TestOther")
        
        data = []
        data.append(x_t(0.,0.))
        data.append(x_t(0.,1.))
        data.append(x_t(1.,2.))
        data.append(x_t(0.,3.))
        data.append(x_t(0.,4.))
        data.append(x_t(0.,5.))
        data.append(x_t(0.,6.))
        data.append(x_t(0.,7.))
        data.append(x_t(0.,8.))
        data.append(x_t(0.,9.))
                    
        ix = []
        iy = []
        for v in data:
            ix.append(v.time)
            iy.append(v.value)         
            
        x = np.array(ix, dtype=float) 
        
        log.debug("X size is:"+str(len(x)))
        #normval = self._x.shape[0]
        #self._y = np.array(y, dtype=float) 
        w = 1.
        phi = 0.5 * np.pi
        y = 10.0 * np.sin(w*x+phi)
        print ("Y size is:"+str(len(y)))
                             
                             
        p_f_list = []
        
        'TODO: calculate this value'
        f_low = 0.01 
        'TODO: calculate this value'
        f_high = 10. 
        
        print("calculate nout")
        f_over = 2
        nout = f_over * len(x)
       
        'calculate a list of frequencies'
        print("calculate list of freq")
        f = np.linspace(f_low, f_high, nout)
        
        'calculate our periodogram'
        print("calculate periodogram")
        pgram = sp.lombscargle(x, y, f)
        
        'convert back to form we may use'
#        i = 0
#        while (i < len(pgram)): 
#            p_f_list.append(p_f(pgram[i],f[i]))
        
'''        
    def test_basic (self):
    
        print ("test-basic")
        data = []
        data.append(x_t(0.,0.))
        data.append(x_t(0.,1.))
        data.append(x_t(1.,2.))
        data.append(x_t(0.,3.))
        data.append(x_t(0.,4.))
        data.append(x_t(0.,5.))
        data.append(x_t(0.,6.))
        data.append(x_t(0.,7.))
        data.append(x_t(0.,8.))
        data.append(x_t(0.,9.))
        
        print ("create lsp in test")
        lsp = LSPeriodogram(data, 2, 4)
        
        print ("get lsp.pgram in test")
        pgram = lsp.pgram()
        
        print ("PGRAM returned is:"+str(pgram))
        #self.assertEqual(3, len(pgram), "Output PGram has correct number of data points")
'''
        
if __name__ == "__main__":
    import sys; #sys.argv = ['', 'TestLSPeriodogram.testBasic']
    
    logging.basicConfig( stream=sys.stderr )
    logging.getLogger( "astroplpython.proc" ).setLevel( logging.DEBUG )
    
    unittest.main()
    
    
