'''
Created on Feb 6, 2015

@author: thomas
'''

class Maximum (object):

    @staticmethod
    def calculate (measurement_list):
        import numpy as np
        '''
        Find the maximum measurement value for any list of 
        measured values.
        '''
        x = []
        for val in measurement_list:
            x.append(val.x)
            
        return measurement_list[np.argmax(x)]
        
