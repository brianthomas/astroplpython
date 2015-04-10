'''
Created on Jul 16, 2014

@author: thomas
'''
import logging 
import sys
import unittest
import numpy as np

from astroplpython.data.PowerFrequencyMeasurement import p_f
from astroplpython.data.TimeMeasurement import x_t
from astroplpython.exception.ListException import EmptyListException
from astroplpython.function.signal.LSPeriodogram import LSPeriodogram


class TestLSPeriodogramTestCase (unittest.TestCase):

    def setUp(self):
        
        logging.basicConfig(stream=sys.stderr)
        logging.getLogger( "astroplpython.function.signal" ).setLevel(logging.DEBUG) 
        
    def tearDown(self):
        pass
    
    def test_raise_emptylist (self):
        '''
        Test raising empty list 
        '''
        
        threw_exception = False;
        try:
            LSPeriodogram.calculate([])
        except EmptyListException:
            threw_exception = True;
            
        self.assertTrue(threw_exception, "Threw EmptyListException") 
                
    def __create_test_data (self):
        
        # generates 100 evenly spaced points between 1 and 1000
        time = np.linspace(1, 10, 100)

        # computes the sine value of each of those points
        mags = np.sin(time)
        
        data = []
        i = 0
        for t in time:
            #print (str(t)+" "+str(mags[i]))
            data.append(x_t(mags[i],t)) 
            i = i+1
            
        return data
    
        
    def test_calculate (self):
       
        ''' 
        test calculate static method
        '''

        f_low  = 0.01
        f_high = 1.01
        f_bins = 100
        
        p_f_list = LSPeriodogram.calculate(self.__create_test_data(), f_low, f_high, f_bins)
        
        # get testable array of values
        pf = p_f.asTupleNumpyArrays(p_f_list) 
        
        # calculate the periodogram, returned as list of p_f 
        self.assertEqual(f_bins, len(pf.powers), "Output PGram has correct number of data points")
        
        # returns the inverse of the frequency (i.e. the period) of the largest periodogram value
        max_period = 1 / (pf.frequencies[np.argmax(pf.powers)]) 
        
        print("Best Period = " + str(round(max_period, 3))) # + " f*2: "+str(max_freq * 2))
        self.assertEqual(round(max_period, 3), 1.00, "Peak power period as expected")
        
        
    def test_gpuCalculate (self):
        ''' 
        test calculate (backed by GPU) static method
        '''

        f_low  = 0.01
        f_high = 1.01
        f_bins = 100
        
        p_f_list = LSPeriodogram.gpuCalculate(self.__create_test_data(), f_low, f_high, f_bins)
        
        # get testable array of values
        pf = p_f.asTupleNumpyArrays(p_f_list) 
        
        # calculate the periodogram, returned as list of p_f 
        self.assertEqual(f_bins, len(pf.powers), "Output PGram has correct number of data points")
        
        # returns the inverse of the frequency (i.e. the period) of the largest periodogram value
        max_period = 1 / (pf.frequencies[np.argmax(pf.powers)]) 
        
        print("Best Period = " + str(round(max_period, 3))) # + " f*2: "+str(max_freq * 2))
        self.assertEqual(round(max_period, 3), 1.00, "Peak power period as expected")
        
    
    '''
    def test_foo (self):
       
        import pycuda.driver as cuda
        import pycuda.gpuarray as gpuarray
        import pycuda.autoinit
        from pycuda.compiler import SourceModule
        
        data = np.random.randn(4,4).astype(np.float32)
        print ("Orig Data:"+str(data)) 

        # cuda.mem_alloc = data.nbytes
        a_gpu = cuda.mem_alloc(data.size * data.dtype.itemsize)
        
        # push data into GPU memory
        cuda.memcpy_htod(a_gpu, data)
        
        mod = SourceModule("""
          __global__ void doublify(float *a)
          {
            int idx = threadIdx.x + threadIdx.y*4;
            a[idx] *= 2;
          }
          """)
        
        func = mod.get_function("doublify")
        func (a_gpu, block=(4,4,1))

        a_doubled = np.empty_like(data)
        print ("Doubled Orig:"+str(a_doubled))
        
        # pull data into main memory
        cuda.memcpy_dtoh(a_doubled, a_gpu)
        
        print ("Doubled:"+str(a_doubled))
        print ("Data:"+str(data)) 
        '''
    

if __name__ == "__main__":
#    import sys; sys.argv = ['', 'TestLSPeriodogram.testBasic']
    unittest.main()
    
    