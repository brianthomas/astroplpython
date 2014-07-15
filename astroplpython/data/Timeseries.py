''' 

Timeseries. 
  
Created on Jul 11, 2014

@author: thomas
'''

class x_t(object):
        
    '''
    A measurement of X(t).
    '''
    @property
    def t(self):
        ''' return array of times '''
        return self._t
    
    @t.setter
    def t(self, v):
        self._t = v;
    
    @property
    def x(self):
        ''' return array of measurements X '''
        return self._x
    
    @x.setter
    def x(self, v):
        self._x = v
    
    def __str__( self ):
        return "x_t => x:"+str(self._x)+" t:"+str(self._t)
    
    def __init__(self, measurement, time):
        ''' Constructor '''
        self._x = measurement
        self._t = time
    
        