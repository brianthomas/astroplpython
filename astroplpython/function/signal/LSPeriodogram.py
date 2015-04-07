''' Lomb-Scargle Periodogram calculator.
 
Created on Jul 11, 2014

@author: thomas
'''

import logging

from astroplpython.data.PowerFrequencyMeasurement import p_f
from astroplpython.exception.ListException import EmptyListException
import numpy as np
import scipy.signal as sp 


class LSPeriodogram(object):
    
    @staticmethod
    def calculate (x_t_list, f_low = 0.01, f_high = 10.0, f_bins = 1000):
        ''' 
        Lomb Scargle Periodogram implementation using scipy. 
        '''

        log = logging.getLogger("astroplpython.function.signal")   
         
        log.debug("LSPeriodogram.calculate() called")
        if (len(x_t_list) == 0):
            raise EmptyListException("Can't calculate LSP with empty x(t) list") 
        
        log.debug("Prepare the data; convert x_t[] to python.numpy and scale");
        x = []
        t = []
        for val in x_t_list:
            x.append(val.value)
            t.append(val.time)
            
        # capture values as ndarray and scale
        x_arr = np.asarray(x)
        
        # scale the magnitude values
        x_arr = (x_arr-x_arr.mean())/x_arr.std()
        
        # capture times as ndarray 
        t_arr = np.asarray(t)
             
        log.debug("calculate list of frequencies to use")
        freqs = np.linspace(f_low, f_high, f_bins)
        
        log.debug("Do pgram calculation")
        pgram = sp.lombscargle(t_arr, x_arr, freqs)
        log.debug("PGRAM shape:"+str(pgram.shape))
        
        log.debug("convert result to form we may use in db, p_f[]"); 
        p_f_list = []
        for i in range (0, f_bins): 
            p_f_list.append(p_f(pgram[i], freqs[i]))
            
        return p_f_list
    