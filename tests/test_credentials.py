
from src.drive_client import DriveClient
from mock import Mock

import unittest2 as unittest
import json

class TestCredentials(unittest.TestCase):
    
    def test_default_credentials(self):
        dc = DriveClient()
        # dummy tokens
        dc.login(access_token='123',refresh_token='123',token_uri='http://dummy.com"',client_id='asdf',client_secret='hello')
        cred = dc.get_credentials()
        assert dc.is_token_valid(cred) == True
    
    def test_check_client_ids(self):
        dc = DriveClient()
        dc.login(access_token='access_token',refresh_token='r123',token_uri='http://dummy.com"',client_id='asdf',client_secret='hello')
        cred = dc.get_credentials()
        assert json.loads(cred.to_json())['token'] == 'acces_token'

    def test_check_client_ids(self):
        dc = DriveClient()
        dc.login(access_token='123',refresh_token='123',token_uri='http://dummy.com"',client_id='asdf',client_secret='hello')
        cred = dc.get_credentials()
        assert json.loads(cred.to_json())['client_id'] == 'asdf'
    
    def test_check_client_secret(self):
        dc = DriveClient()
        dc.login(access_token='123',refresh_token='123',token_uri='http://dummy.com"',client_id='asdf',client_secret='hello')
        cred = dc.get_credentials()
        assert json.loads(cred.to_json())['client_secret'] == 'hello'

    def test_check_refresh_token(self):
        dc = DriveClient()
        dc.login(access_token='123',refresh_token='123',token_uri='http://dummy.com"',client_id='asdf',client_secret='hello')
        cred = dc.get_credentials()
        assert json.loads(cred.to_json())['refresh_token'] == '123'

    def test_client_id_in_cred(self):
        dc = DriveClient()
        dc.login(access_token='123',refresh_token='123',token_uri='http://dummy.com"',client_id='asdf',client_secret='hello')
        cred = dc.get_credentials()
        assert dc.client_id_in_cred(cred) == True

if __name__ == '__main__':
    unittest.main()