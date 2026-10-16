# test_krakenrelay.py
"""
Tests for KrakenRelay module.
"""

import unittest
from krakenrelay import KrakenRelay

class TestKrakenRelay(unittest.TestCase):
    """Test cases for KrakenRelay class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = KrakenRelay()
        self.assertIsInstance(instance, KrakenRelay)
        
    def test_run_method(self):
        """Test the run method."""
        instance = KrakenRelay()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
