''' Lomb-Scargle Periodogram calculator.
 
Created on Jul 11, 2014

@author: thomas
'''

from astroplpython.data.PowerFrequencyMeasurement import p_f
from astroplpython.data.TimeMeasurement import x_t
import logging
import scipy.signal as sp 
import numpy as np

class LSPeriodogram(object):
    
    TWO_PI = np.pi * 2.0
    
    @staticmethod
    def calculate (x_t_list, f_low = 0.01, f_high = 10.0, f_over = 4):
        ''' 
        Lomb Scargle Periodogram implementation using scipy. 
        '''
            
        #import sys
        #logging.basicConfig( stream=sys.stderr )
        log = logging.getLogger( "astroplpython.function.signal" )   
        #log.setLevel (logging.WARN)
         
        log.debug("LSPeriodogram.calculate() called")
        
        log.debug("Prepare the data; convert x_t[] to python.numpy and scale");
        x = []
        t = []
        for v in x_t_list:
            x.append(v.time)
            t.append(v.value)
            
        # capture values as ndarray and scale
        x_arr = np.asarray(x)
        x_arr = (x_arr-x_arr.mean())/x_arr.std()
        
        # capture times as ndarray 
        t_arr = np.asarray(t)
            
        'TODO: calculate this value ??'
        #f_low = 0.01 
        'TODO: calculate this value ??'
        #f_high = 10. 
        
        log.debug("calculate list of frequencies to use")
        num_out = f_over * len(x)
        log.debug(" Number of frequency bins out:"+str(num_out))
        f_bins = np.linspace(f_low, f_high, num_out)
        
        log.debug("Do pgram calculation")
        pgram = sp.lombscargle(x_arr, t_arr, f_bins)
        
        log.debug("convert result to form we may use in db, p_f[]"); 
        p_f_list = []
        for i in range (0, num_out): 
            p_f_list.append(p_f(pgram[i]/LSPeriodogram.TWO_PI,f_bins[i]))
            
        #log.debug("PGRAM shape:"+str(pgram.shape))
        
        return p_f_list
    
        
                             
        
