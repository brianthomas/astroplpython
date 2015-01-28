''' Lomb-Scargle Periodogram calculator.
 
Created on Jul 11, 2014

@author: thomas
'''

from astroplpython.data.Periodogram import p_f
from astroplpython.data.Timeseries import x_t
import scipy.signal as sp 
import numpy as np
import logging

class LSPeriodogram(object):
    
    '''
    Lomb Scargle Periodogram implementation using scipy.
    '''
    def pgram (self):
            
        log = logging.getLogger( "astroplpython.proc" )
        ''' TODO: calculate the periodogram here..
            for now, we will simply mirror back the 
            timeseries information
        '''
        log.debug("pgram() called")
        p_f_list = []
        
        'TODO: calculate this value'
        f_low = 0.01 
        'TODO: calculate this value'
        f_high = 10. 
        
        print("calculate nout")
        nout = self._f_over * len(self._x)
       
        'calculate a list of frequencies'
        print("calculate list of freq")
        f = np.linspace(f_low, f_high, nout)
        
        'calculate our periodogram'
        print("calculate periodogram")
#        pgram = sp.lombscargle(self._x, self._y, f)
        
        'convert back to form we may use'
       # i = 0
       # while (i < len(pgram)): 
       #     p_f_list.append(p_f(pgram[i],f[i]))
            
        return p_f_list
    
    def __init__(self, x_t_list, f_high=2, f_over=4):
        '''
        Constructor
        '''
        
#        import sys
        
#        logging.basicConfig( stream=sys.stderr )
#        log = logging.getLogger( "astroplpython.proc" )
        
        logging.error("construct LSPERIODOGRAM")
        
        print("construct lsp")
        
        ' TODO: validate input parameters'
        self._f_high = f_high
        self._f_over = f_over
        x = []
        y = []
        for v in x_t_list:
            x.append(v.time)
            y.append(v.value)
            
 #       self._x = np.array(x, dtype=float) 
 #       print ("X size is:"+len(self._x))
        #normval = self._x.shape[0]
        #self._y = np.array(y, dtype=float) 
        w = 1.
        phi = 0.5 * np.pi
 #       self._y = 10.0 * np.sin(w*x+phi)
 #       print ("Y size is:"+len(self._y))
                             
        