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
        
        import astroplpython.data.TimeMeasurement as Timeseries
        
        # test data strarr has combination of integer, floats.
        #
        strarr = ['(1,1)', '(2,2.)', '(2.1,3.)', '(2.018,4.)']
        x_t_list = Timeseries.x_t.dbStrToArray(strarr)
        #print (str(x_t_list))
        
        self.assertEqual(4, len(x_t_list), "list has right number of elements")
        
        # Check class, return values. In checking values be sure
        # to check that we cast back to float
        x = [1., 2.0, 2.1, 2.018]
        t = [1.000, 2.0, 3.0, 4.0]
        i = 0
        while (i < 4): 
            #print (str(x_t_list[i]))
            #print (str(x_t_list[i].value))
            self.assertIsInstance(x_t_list[i], Timeseries.x_t, "is class of Timeseries")
            self.assertEquals(x[i], x_t_list[i].value) #, "x value is correct")
            self.assertEquals(t[i], x_t_list[i].time, "t value is correct")
            i += 1
            
        self.assertEqual(str(x_t_list[0]), "x_t(x:1.0 t:1.0)", "String rep is correct")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()