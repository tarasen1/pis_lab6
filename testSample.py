import unittest
from classSample import Sample

class TestClassSample(unittest.TestCase):
    def setUp(self):
        self.sample = Sample(1,'a',2)

    def test_typeError(self):
        self.assertRaises(TypeError, self.sample.add, 1, 'a')
        self.assertRaises(TypeError, self.sample.sub, 'c', 'a')
        self.assertRaises(TypeError, self.sample.add, 'd', 2)

    def test_calculation(self):
        self.assertEqual(self.sample.add(2,2), 4)
        self.assertEqual(self.sample.sub(5,2), 3)

if __name__ == '__main__':
    unittest.main()
