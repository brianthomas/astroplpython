''' 

Timeseries. 
  
Created on Jul 11, 2014

@author: thomas
'''

class x_t (object):
        
    '''
    A measurement of X(t).
    '''
    @property
    def time(self):
        ''' return array of times '''
        return self._time
    
    @time.setter
    def time(self, v):
        self._time = v;
    
    @property
    def value(self):
        ''' return array of measurements X '''
        return self._value
    
    @value.setter
    def value(self, v):
        self._value = v
    
    def __str__( self ):
        return "x_time => x:"+str(self._value)+" t:"+str(self._time)
    
    def __init__(self, measurement, time):
        ''' Constructor '''
        self._value = float(measurement) 
        self._time = float(time) 
    
    @staticmethod
    def strToXTArray (strarr):
        ''' Convert an array of string representation to x_t[] '''
        x_t_list = []
        for v in strarr:
            v = v.replace("(","")
            v = v.replace(")","")
            vals = v.split(",")
            x = vals[0]
            t = vals[1]
            x_t_list.append(x_t(x,t))
        
        return x_t_list
