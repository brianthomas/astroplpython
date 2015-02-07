'''
Created on Feb 6, 2015

@author: thomas
'''
import unittest


class Test(unittest.TestCase):


    def testStrArrayParsing(self):
    
        import astroplpython.data.Measurement as Measurement
        
        # test data strarr has combination of integer, floats.
        #
        strarr = ['(1,1)', '(2,2.)', '(2.1,3.)', '(2.018,4.)']
        x_y_list = Measurement.x_y.dbStrToArray(strarr)
        #print (str(x_t_list))
        
        self.assertEqual(4, len(x_y_list), "list has right number of elements")
        
        # Check class, return values. In checking values be sure
        # to check that we cast back to float
        x = [1., 2.0, 2.1, 2.018]
        t = [1.000, 2.0, 3.0, 4.0]
        i = 0
        while (i < 4): 
            #print (str(x_t_list[i]))
            #print (str(x_t_list[i].value))
            self.assertIsInstance(x_y_list[i], Measurement.x_y, "is class of Measurement.x_y")
            self.assertEquals(x[i], x_y_list[i].value) #, "x value is correct")
            self.assertEquals(t[i], x_y_list[i].time, "t value is correct")
            i += 1


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testStrArrayParsing']
    unittest.main()