''' 

Measurement series. A series of X values measured
for independent variable Y. 
  
Created on Jul 11, 2014

@author: thomas
'''

class x_y (object):
        
    '''
    A measurement of X(Y).
    '''
    @property
    def y(self):
        ''' return value of y for this measurement '''
        return self._y
    
    @property
    def x(self):
        ''' return measurement X '''
        return self._x
    
    def __str__( self ):
        return "x_t(x:"+str(self._value)+" t:"+str(self._time)+")" 
    
    def __init__(self, x, y):
        ''' Constructor '''
        self._x = float(x) 
        self._y = float(y) 
    
    @staticmethod
    def dbStrToArray (strarr):
        ''' Convert a (postgres) string representation of an array of values to x_y[] '''
        return x_y._dbStrToArray(x_y, strarr)
        
    @staticmethod
    def _dbStrToArray (classToUse, strarr):
        x_y_list = []
        for v in strarr:
            v = v.replace("(","")
            v = v.replace(")","")
            vals = v.split(",")
            x = vals[0]
            y = vals[1]
            x_y_list.append(classToUse(x,y))
        
        return x_y_list
