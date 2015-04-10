''' Lomb-Scargle Periodogram Module.
 
Created on Jul 11, 2014

@author: thomas
'''


import logging

from astroplpython.data.PowerFrequencyMeasurement import p_f
from astroplpython.data.TimeMeasurement import x_t
from astroplpython.exception.ListException import EmptyListException

import numpy as np
from pycuda import *
import scipy.signal as sp 


class LSPeriodogram(object):
    
    ''' 
    Various Lomb-Scargle calculations 
    '''
    
    @staticmethod
    def __checkargs(x_t_list):
        
        if (len(x_t_list) == 0):
            raise EmptyListException("Can't calculate LSP with empty x(t) list") 
    
    @staticmethod
    def calculate (x_t_list, f_low = 0.01, f_high = 10.0, f_bins = 1000):
        ''' 
        Lomb-Scargle Periodogram implementation using scipy. 
        
        Expects a time-ordered (ascending) list of X(t) measurements.
        '''

        log = logging.getLogger("astroplpython.function.signal")   
        log.debug("LSPeriodogram.calculate() called")
        
        LSPeriodogram.__checkargs (x_t_list)
        
        log.debug("Prepare the data; convert x_t[] to python.numpy and scale");
        xt = x_t.asTupleNumpyArrays(x_t_list) 
            
        # capture values as ndarray and scale
        x_arr = np.asarray(xt.values)
        
        # scale the magnitude values
        x_arr = (x_arr-x_arr.mean())/x_arr.std()
        
        # capture times as ndarray 
        t_arr = np.asarray(xt.times)
             
        log.debug("calculate list of frequencies to use")
        freqs = np.linspace(f_low, f_high, f_bins)
        
        log.debug("Do pgram calculation")
        pgram = sp.lombscargle(t_arr, x_arr, freqs)
        log.debug("PGRAM shape:"+str(pgram.shape))
        
        log.debug("convert result to form we may use in db, p_f[]"); 
        p_f_list = []
        for i in range (0, f_bins): 
            p_f_list.append(p_f(pgram[i], freqs[i]))
            
        return p_f_list
   
    @staticmethod
    def gpuCalculate (x_t_list, f_low = 0.01, f_high = 10.0, f_bins = 1000):
        
        ''' 
        Lomb-Scargle Periodogram implementation using culsp/pycuda. 
        
        Expects a time-ordered (ascending) list of X(t) measurements.
        '''
        
        import pycuda.driver as cuda
        import pycuda.autoinit
        from pycuda.compiler import SourceModule
       
        log = logging.getLogger("astroplpython.function.signal")   
        log.debug("LSPeriodogram.gpuCalculate() called")
        
        LSPeriodogram.__checkargs (x_t_list)
        log.debug("Prepare the data; convert x_t[] to python.numpy arrays");
        xt = x_t.asTupleNumpyArrays(x_t_list) 
       
        log.debug("Do pgram calculation on GPU")
        mod = _CULSP() 
        pgram = mod.calculate(xt, f_high, f_bins)
        
        # TODO
        
        p_f_list = []
        log.debug("convert result to form we may use in db, p_f[]"); 
        # TODO
        return p_f_list 
    
    
class _CULSP (object):
    
    ''' Implementation of Townsend 2010 LSP kernel '''
    
    def calculate (self, data, f_high, f_bins):
        
        import pycuda.driver as driver
        import pycuda.compiler as compiler
        import pycuda.autoinit
        
        log = logging.getLogger("astroplpython.function.signal")   
        log.debug("CULSP.calculate() called")
        
        log.debug("Orig Data:"+str(data)) 
        
        log.debug(" TODO: Calculate blocksize")

        log.debug("set up GPU, allocate memory for working")
        a_gpu = driver.mem_alloc(data.size * data.dtype.itemsize)
        
        log.debug("push data into GPU memory")
        driver.memcpy_htod(a_gpu, data)
        
        log.debug("compile and run the culsp_kernel on data in the GPU")
        culsp_func = compiler.SourceModule(self._kernelStr).get_function("culsp_kernel") 
        culsp_func (a_gpu, block=(4,4,1))

        log.debug("pull data from GPU back into main memory")
        result = np.empty_like(data)
        driver.memcpy_dtoh(result, a_gpu)
        
        log.debug("return result") 
        return result

    def __init__(self):
        import pkg_resources
        self._kernelStr =  pkg_resources.resource_string(__name__, "culsp_kernel.cu")
        
        
