'''
Created on Jul 16, 2014

@author: thomas
'''
import unittest

class TestTimeseries (unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_strToXTArray (self):
        import astroplpython.data.Timeseries as t
        strarr = ['(1,1.)', '(2,2.)', '(2.1,3.)', '(2.018,4.)']
        x_t_list = t.x_t.strToXTArray(strarr)
        print (str(x_t_list))
        self.assertEqual(4, len(x_t_list), "list has right number of elements")
        
        x = [1, 2, 2.1, 2.018]
        t = [1., 2., 3., 4.]
        i = 0
        while (i < 4): 
            self.assertEquals(x[i], x_t_list[i].value) #, "x value is correct")
            self.assertEquals(t[i], x_t_list[i].time, "t value is correct")
            i += 1

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()