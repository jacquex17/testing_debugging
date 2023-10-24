import unittest
import bubblesort as st

class TestValue(unittest.TestCase):

    def run_sort(self, testList):
        expectedList = testList.copy()
        expectedList.sort()
        actualList = st.bubble_sort(testList)
        self.assertEqual(actualList, expectedList)

    def test_simple(self):
        testList = [4,3,2,1]
        self.run_sort(testList)

    def test_empty(self):
        testList = []
        self.run_sort(testList)

    def test_presorted(self):
        testList = [1,2,3,4]
        self.run_sort(testList)

    def test_negative(self):
        testList = [-4,-3,-2,-1]
        self.run_sort(testList)