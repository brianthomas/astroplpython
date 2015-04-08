'''
Created on Jul 16, 2014

@author: thomas
'''
import unittest

class TestPowerFrequency (unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_strToXTArray (self):
        
        import astroplpython.data.PowerFrequencyMeasurement as PF
        
        # test data strarr has combination of integer, floats.
        #
        strarr = ['(1,1)', '(2,2.)', '(2.1,3.)', '(2.018,4.)']
        p_f_list = PF.p_f.dbStrToArray(strarr)
        #print (str(p_f_list))
        
        self.assertEqual(4, len(p_f_list), "list has right number of elements")
        
        # Check class, return values. In checking values be sure
        # to check that we cast back to float
        x = [1., 2.0, 2.1, 2.018]
        t = [1.000, 2.0, 3.0, 4.0]
        i = 0
        while (i < 4): 
            self.assertIsInstance(p_f_list[i], PF.p_f, "is class of PowerFrequency")
            self.assertEquals(x[i], p_f_list[i].power, " power value is correct")
            self.assertEquals(t[i], p_f_list[i].frequency, "freq value is correct")
            i += 1

        self.assertEqual(str(p_f_list[0]), "p_f(p:1.0 f:1.0)", "String rep is correct")
        
if __name__ == "__main__":
    unittest.main()