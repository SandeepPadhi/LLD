"""
Key Highlights for Reference:

Basic Comparisons: assertEqual, assertNotEqual, assertTrue, assertFalse.
Object Identity: assertIs, assertIsNot.
Null Checks: assertIsNone, assertIsNotNone.
Containment: assertIn, assertNotIn.
Type Checking: assertIsInstance, assertNotIsInstance.
Exceptions: assertRaises, assertRaisesRegex.
Floating-Point: assertAlmostEqual, assertNotAlmostEqual.
Collections: assertCountEqual, assertListEqual, assertTupleEqual, assertSetEqual, assertDictEqual.
Regex: assertRegex, assertNotRegex.
File system: os.path.exists() and file reading.
Remember context managers: with self.assertRaises(...) is very useful.


"""


import unittest
import os

class TestFixtureAndAssertionExamples(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Called once before any tests in this class."""
        cls.shared_resource = "Shared Resource Setup"  # Example class-level setup
        print("setUpClass: Shared resource initialized.")

    @classmethod
    def tearDownClass(cls):
        """Called once after all tests in this class."""
        print("tearDownClass: Shared resource cleaned up.")

    def setUp(self):
        """Called before each test method."""
        self.test_list = [1, 2, 3]  # Example per-test setup
        print("setUp: Test list initialized.")

    def tearDown(self):
        """Called after each test method."""
        print("tearDown: Test list cleaned up.")

    def test_basic_assertions(self):
        """Example of basic assertion methods."""
        print("test_basic_assertions")
        self.assertEqual(2 + 2, 4)
        self.assertTrue(True)
        self.assertIn(2, self.test_list)

    def test_exception_assertions(self):
        """Example of exception assertion methods."""
        print("test_exception_assertions")
        with self.assertRaises(ValueError):
            int("abc")

    def test_float_assertions(self):
        """Example of float assertion methods."""
        print("test_float_assertions")
        self.assertAlmostEqual(3.14159, 3.14158, places=5)

    def test_collection_assertions(self):
        """Example of collection assertion methods."""
        print("test_collection_assertions")
        self.assertListEqual([1, 2, 3], self.test_list)

    def test_regex_assertions(self):
        """Example of regex assertion methods."""
        print("test_regex_assertions")
        self.assertRegex("hello world", "hello")

    def test_file_assertions(self):
        """Example of file system assertions."""
        print("test_file_assertions")
        with open("test_file.txt", "w") as f:
            f.write("test content")
        self.assertTrue(os.path.exists("test_file.txt"))
        with open("test_file.txt", "r") as f:
            self.assertEqual("test content", f.read())
        os.remove("test_file.txt")

    def test_shared_resource(self):
        """Example using shared resource from setUpClass."""
        print("test_shared_resource")
        self.assertEqual(self.shared_resource, "Shared Resource Setup")

if __name__ == '__main__':
    unittest.main()
