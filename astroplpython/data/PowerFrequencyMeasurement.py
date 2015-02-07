'''
Created on Jul 11, 2014

@author: thomas
'''
from astroplpython.data.Measurement import x_y

class p_f(x_y):
    ''' 
    An individual measurement of Power P at frequency f; P(f) 
    '''
    
    @property
    def power(self):
        return self.x
    
    @property
    def frequency (self):
        return self.y 
    
    def __str__( self ):
        return "p_f(p:"+str(self.power)+" f:"+str(self.frequency)+")" 
    
    def __init__(self, power, frequency):
        ''' Constructor '''
        super().__init__(power, frequency)
        
    @staticmethod
    def dbStrToArray (strarr):
        ''' Convert a (postgres) string representation of an array of values to x_t[] '''
        return x_y._dbStrToArray(p_f, strarr)
    
    