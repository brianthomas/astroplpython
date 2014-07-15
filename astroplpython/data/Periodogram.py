'''
Created on Jul 11, 2014

@author: thomas
'''

class p_f(object):
    ''' 
    An individual measurement of Power P at frequency f; P(f) 
    '''
    
    @property
    def power(self):
        return self._power
    
    @power.setter
    def power(self, p):
        self._power = p
        
    @property
    def frequency (self):
        return self._frequency
    
    @frequency.setter
    def frequency (self, f):
        self._frequency = f
        
    def __str__( self ):
        return "p_f => p:"+str(self._power)+" f:"+str(self._frequency)
    
    def __init__(self, power, frequency):
        ''' Constructor '''
        self._power = power
        self._frequency  = frequency
        
        