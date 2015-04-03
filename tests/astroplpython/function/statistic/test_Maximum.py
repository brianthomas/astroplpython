'''
Created on Apr 3, 2015

@author: thomas
'''
import unittest

from astroplpython.function.statistic.Maximum import Maximum 
from astroplpython.data.Measurement import x_y

class TestMaximumMeasurement(unittest.TestCase):


    def testMax (self):
        ''' 
        test static max method
        '''
        import logging 
        import sys
        logging.basicConfig(stream=sys.stderr)
        logging.getLogger( "astroplpython.function.signal" ).setLevel(logging.DEBUG) 

        import numpy as np
        
        # generates 10 evenly spaced points between 1 and 10
        y = np.linspace(1, 10, 10)

        # computes the sine value of each of those points
        x = np.sin(y)
        
        data = []
        i = 0
        for v in y:
#            print (str(x[i]) + " "+ str(v))
            data.append(x_y(x[i],v)) 
            i = i+1
            
        max_measurement = Maximum.calculate(data)
        print ("Maximum measurement:"+str(max_measurement))
        self.assertTrue(max_measurement.y == 8, "max measurement Y is correct") 
        self.assertTrue(round(max_measurement.x, 4) == 0.9894, "max measurement X is correct") 

if __name__ == "__main__":
    import sys; sys.argv = ['', 'Test.testMax']
    unittest.main()