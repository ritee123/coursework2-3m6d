import unittest
from unittest.mock import patch, MagicMock
import socket

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(portscan_socket_timeout)
        sock.connect((target, port))
        sock.close()
        return True
    except OSError:
        return False

class TestPortScan(unittest.TestCase):

    @patch('socket.socket')
    def test_port_open(self, mock_socket):
        global portscan_socket_timeout, target
        portscan_socket_timeout = 1  
        target = '127.0.0.1' 
        mock_socket_instance = mock_socket.return_value
        mock_socket_instance.connect.return_value = None

        result = portscan(80)
        self.assertTrue(result)

    @patch('socket.socket')
    def test_port_closed(self, mock_socket):
        global portscan_socket_timeout, target
        portscan_socket_timeout = 1 
        target = '127.0.0.1' 

        mock_socket_instance = mock_socket.return_value
        mock_socket_instance.connect.side_effect = OSError

        result = portscan(80)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
