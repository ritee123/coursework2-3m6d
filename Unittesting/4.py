import unittest
from unittest.mock import patch, MagicMock
from collections import deque
import re

# Define scrap_emails within the test file, or paste the provided function here.
def scrap_emails():
    # ... (function code here) ...

    class TestScrapEmails(unittest.TestCase):
     @patch('builtins.open', new_callable=unittest.mock.mock_open())
     @patch('builtins.print')  # Suppress print statements during testing
     def test_scrap_emails(self, mock_print, mock_open):
        # Set up the global variables here for testing
        global a1
        a1 = 'http://example.com'
        global argument
        argument = '2'
        
        # Mock the requests.get call within scrap_emails
        with patch('requests.get') as mock_get:
            mock_get.return_value.text = "contact@example.com"

            # Mock the re.findall call within scrap_emails
            with patch('re.findall') as mock_findall:
                mock_findall.return_value = ['contact@example.com']

                # Call the scrap_emails function
                scrap_emails()
                
                # Check if emails were found and written to the file
                emails_file_handle = mock_open().write.call_args_list
                self.assertIn('contact@example.com', emails_file_handle[0][0][0])
                
                # Check if links were collected and written to the file
                links_file_handle = mock_open().write.call_args_list
                self.assertIn('http://example.com', links_file_handle[1][0][0])

if __name__ == '__main__':
    unittest.main()
