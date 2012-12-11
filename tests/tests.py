import unittest
import glob

import sys
sys.path.append("../")

from pynxc import python_to_nxc

class TextConversion(unittest.TestCase):

    def test_directories(self):
        inputs = glob.glob('./in/*.py')
        
        for input in inputs:
            nxc_filename = input.replace('.py', '.nxc') 
            python_to_nxc(input, nxc_filename)
            
            testfile = nxc_filename.replace('./in/', './out/')
            
            print("Testing %s" % input)
            self.assertEqual(open(nxc_filename, 'r').read(), 
                                open(testfile, 'r').read())


if __name__ == '__main__':
    unittest.main()

