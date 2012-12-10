import unittest
import os


class TextConversion(unittest.TestCase):

    def test_directories(self):
        inputs = os.listdir('./in')
        outputs = os.listdir('./out')



if __name__ == '__main__':
    unittest.main()

