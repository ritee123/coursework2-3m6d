import unittest
from unittest.mock import patch, MagicMock
import json

# Define the way_back_url function here
def way_back_url():
    # ... (the function's code goes here) ...
    pass

class TestWayBackUrl(unittest.TestCase):
    @patch('requests.get')  # Mock the requests.get call
    @patch('builtins.open', new_callable=unittest.mock.mock_open())  # Mock the open function
    @patch('builtins.print')  # Mock the print function to suppress output during the test
    def test_way_back_url(self, mock_print, mock_open, mock_get):
        # Set up the global variables
        global a1
        a1 = 'http://example.com'

        global urls
        urls = []

        # (Continue with your test setup and assertions)

if __name__ == '__main__':
    unittest.main()
