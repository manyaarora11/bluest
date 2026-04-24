import unittest
from max_subarray import max_subarray_sum

class TestMaxSubarraySum(unittest.TestCase):
    
    def test_normal_case(self):
        """Test with mixed positive and negative numbers"""
        arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        self.assertEqual(max_subarray_sum(arr), 6)
    
    def test_all_positive(self):
        """Test with all positive numbers"""
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(max_subarray_sum(arr), 15)
    
    def test_all_negative(self):
        """Test with all negative numbers"""
        arr = [-1, -2, -3, -4, -5]
        self.assertEqual(max_subarray_sum(arr), -1)
    
    def test_single_element_positive(self):
        """Test with single positive element"""
        arr = [5]
        self.assertEqual(max_subarray_sum(arr), 5)
    
    def test_single_element_negative(self):
        """Test with single negative element"""
        arr = [-3]
        self.assertEqual(max_subarray_sum(arr), -3)
    
    def test_empty_array(self):
        """Test with empty array"""
        arr = []
        self.assertEqual(max_subarray_sum(arr), 0)
    
    def test_zeros(self):
        """Test with zeros"""
        arr = [0, 0, 0]
        self.assertEqual(max_subarray_sum(arr), 0)
    
    def test_mixed_with_zero(self):
        """Test with mixed numbers including zero"""
        arr = [-1, 0, 2, -1, 3]
        self.assertEqual(max_subarray_sum(arr), 4)

if __name__ == '__main__':
    unittest.main()