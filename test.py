import unittest
import subprocess
 
# The function to be tested
from main import add
# The test case
class TestAddFunction(unittest.TestCase):
 
    def test_add_integers(self):
        self.assertEqual(add(1, 2), 3)
 
    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)
 
 
    def test_add_mixed_numbers(self):
        self.assertEqual(add(-1, 5), 4)
 
    def test_add_floats(self):
        self.assertEqual(add(1.5, 2.5), 4.0)
 
 
if __name__ == '__main__':
    # Create a test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAddFunction)
 
    # Run the tests and store the result
    result = unittest.TextTestRunner().run(suite)
 
    # Check if all tests passed
    if result.wasSuccessful():
        print("")
        subprocess.run(["echo", "All tests passed!"])
        subprocess.run(["python", "end.py"])
        subprocess.run(["python", "time_ellapsed.py"])
    else:
        print("Some tests failed. No action will be performed.")
 
