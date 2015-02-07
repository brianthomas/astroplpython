''' Lomb-Scargle Periodogram calculator.
 
Created on Jul 11, 2014

@author: thomas
'''

from astroplpython.data.PowerFrequencyMeasurement import p_f
from astroplpython.data.TimeMeasurement import x_t
import scipy.signal as sp 
import numpy as np
import logging

class LSPeriodogram(object):
    
    '''
    Lomb Scargle Periodogram implementation using scipy.
    '''
    @staticmethod
    def calculate (x_t_list, f_low = 0.01, f_high = 10.0, f_over = 4):
            
        import sys
        logging.basicConfig( stream=sys.stderr )
        log = logging.getLogger( "astroplpython.function" )   
        log.setLevel (logging.WARN)
         
        log.debug("LSPeriodogram.calculate() called")
        
        'Prepare the data; convert x_t[] to numpy ndarrays for lsp calc'
        x = []
        y = []
        for v in x_t_list:
            x.append(v.time)
            y.append(v.value)
            
        x_arr = np.asarray(x)
        y_arr = np.asarray(y)
            
        p_f_list = []
        
        'TODO: calculate this value ??'
        #f_low = 0.01 
        'TODO: calculate this value ??'
        #f_high = 10. 
        
        log.debug("calculate list of frequencies to use")
        num_out = f_over * len(x)
#        log.debug(" NUMBER OF BINS OUT:"+str(num_out))
        f_bins = np.linspace(f_low, f_high, num_out)
        
        log.debug("calculate pgram")
        pgram = sp.lombscargle(x_arr, y_arr, f_bins)
        
        log.debug("PGRAM type:"+str(type(pgram)))
        log.debug("PGRAM shape:"+str(pgram.shape))
        
        'convert back to form we may use'
        for i in range (0, num_out): 
            p_f_list.append(p_f(pgram[i],f_bins[i]))
            
        return p_f_list
    
''' 
    Set debugging logging on instance.
    def debug(self):
        self._log.setLevel( logging.DEBUG )
'''
        
'''
    def __init__(self, x_t_list):
        
        print ("xtlist type:"+str(type(x_t_list)))
        
        # create logger
        import sys
        logging.basicConfig( stream=sys.stderr )
        self._log = logging.getLogger( "astroplpython.function" )
        
        ' TODO: validate input parameters'
        
        ' Set instance variables'
        x = []
        y = []
        for v in x_t_list:
            x.append(v.time)
            y.append(v.value)
            
 #       self._x = np.array(x, dtype=float) 
 #       print ("X size is:"+len(self._x))
        #normval = self._x.shape[0]
        #self._y = np.array(y, dtype=float) 
 #       w = 1.
 #       phi = 0.5 * np.pi
 #       self._y = 10.0 * np.sin(w*x+phi)
 #       print ("Y size is:"+len(self._y))
 '''
                             
        
