# test_sparkhinge.py
"""
Tests for SparkHinge module.
"""

import unittest
from sparkhinge import SparkHinge

class TestSparkHinge(unittest.TestCase):
    """Test cases for SparkHinge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SparkHinge()
        self.assertIsInstance(instance, SparkHinge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SparkHinge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
