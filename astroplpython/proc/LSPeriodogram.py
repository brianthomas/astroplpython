''' Lomb-Scargle Periodogram calculator.
 
Created on Jul 11, 2014

@author: thomas
'''

from astroplpython.data.Periodogram import p_f
from astroplpython.data.Timeseries import x_t

class LSPeriodogram(object):
    
    '''
    classdocs
    '''
    def pgram (self):
            
        ''' TODO: calculate the periodogram here..
            for now, we will simply mirror back the 
            timeseries information
        '''
        p_f_list = []
        for x_t in self._timeseries:
            p_f_list.append(p_f(x_t.x, x_t.t))
            
        return p_f_list
    
    def __init__(self, x_t_list, f_high=2, f_over=4):
        '''
        Constructor
        '''
        
        ''' 
        TODO: validate input parameters 
        '''
        self._f_high = f_high
        self._f_over = f_over
        self._timeseries = x_t_list
        