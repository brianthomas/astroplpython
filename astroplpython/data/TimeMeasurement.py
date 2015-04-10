''' 
Created on Jul 11, 2014

@author: thomas
'''

import collections
from astroplpython.data.Measurement import x_y

class x_t (x_y):
        
    '''
    A measurement of property X at time T e.g. X(T).
    '''
    @property
    def time(self):
        ''' return array of times '''
        return self.y 
    
    @property
    def value(self):
        ''' return array of measurements X '''
        return self.x 
    
    def __str__(self):
        return "x_t(x:" + str(self.value) + " t:" + str(self.time) + ")" 
    
    def __init__(self, measurement, time):
        ''' Constructor '''
        super().__init__(measurement, time)
    
    @staticmethod
    def asTupleNumpyArrays (x_t_list):
        ''' Convert list of x_t[] into tuple of 2 numpy arrays for all x and t values'''
        
        xt = collections.namedtuple('xt', ['values', 'times'])
        xt.values = []
        xt.times = []
        for val in x_t_list:
            xt.values.append(val.value)
            xt.times.append(val.time)
            
        return xt
            
    @staticmethod
    def dbStrToArray (strarr):
        ''' Convert a (postgres) string representation of an array of values to x_t[] '''
        return x_y._dbStrToArray(x_t, strarr)
    
    
