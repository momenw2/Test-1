import unittest
from unittest.mock import patch

class Solution:
    def largestRectangleArea(self, heights):
        maxArea = 0
        stack = []  # pair: (index, height)
        
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))
        
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        
        return maxArea


class SolutionTests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_largestRectangleArea(self):
        # Test case 1: heights are [2, 1, 5, 6, 2, 3]
        heights = [2, 1, 5, 6, 2, 3]
        self.assertEqual(self.solution.largestRectangleArea(heights), 10)
        
        # Test case 2: heights are [1, 1, 1, 1, 1]
        heights = [1, 1, 1, 1, 1]
        self.assertEqual(self.solution.largestRectangleArea(heights), 5)
        
        # Test case 3: heights are [2, 2, 2, 2, 2]
        heights = [2, 2, 2, 2, 2]
        self.assertEqual(self.solution.largestRectangleArea(heights), 10)
        
        # Test case 4: heights are [3, 2, 1, 1, 3]
        heights = [3, 2, 1, 1, 3]
        self.assertEqual(self.solution.largestRectangleArea(heights), 5)
        
        # Test case 5: heights are [1, 2, 3, 4, 5]
        heights = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution.largestRectangleArea(heights), 9)
    
    @patch('builtins.print')
    def test_largestRectangleArea_with_mocked_print(self, mock_print):
        # Test case: heights are [4, 2, 0, 3, 2, 4, 3, 4]
        heights = [4, 2, 0, 3, 2, 4, 3, 4]
        self.assertEqual(self.solution.largestRectangleArea(heights), 10)
        mock_print.assert_called_once_with("Max area is 10")
    
    @unittest.skip("Skipping slow test case")
    def test_largestRectangleArea_slow_test_case(self):
        # Test case: heights are large and time-consuming to calculate
        heights = [1] * 1000000
        self.assertEqual(self.solution.largestRectangleArea(heights), 1000000)
    
    @unittest.expectedFailure
    def test_largestRectangleArea_failing_test_case(self):
        # Test case: heights are [5, 4, 3, 2, 1]
        heights = [5, 4, 3, 2, 1]
        self.assertEqual(self.solution.largestRectangleArea(heights), 10)

if __name__ == '__main__':
    unittest.main()

