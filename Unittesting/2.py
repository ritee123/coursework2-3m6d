import unittest
from unittest.mock import patch, MagicMock
import requests

# Assuming the dir_search_check function is defined here
def dir_search_check(m_url):
    try:
        r = requests.get(m_url)
        if not 399 < r.status_code < 500:
            d1.append(f'{m_url}       #{r.status_code}')
            print(f'{m_url}       #{r.status_code}')
            return True
        else:
            return False
    except Exception as e:
        pass

class TestDirSearchCheck(unittest.TestCase):

    @patch('requests.get')
    def test_directory_exists(self, mock_get):
        global d1
        d1 = []  
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        m_url = 'http://example.com/testdir'

        result = dir_search_check(m_url)

        self.assertTrue(result)
        self.assertIn(f'{m_url}       #200', d1)

    @patch('requests.get')
    def test_directory_does_not_exist(self, mock_get):
        global d1
        d1 = []  
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        m_url = 'http://example.com/nonexistentdir'

        result = dir_search_check(m_url)
        self.assertFalse(result)
        self.assertNotIn(f'{m_url}       #404', d1)

if __name__ == '__main__':
    unittest.main()
