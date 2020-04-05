
from utils import logging_cfg

import google.oauth2.credentials
import io
import json
import logging
import os
import requests
import sys

logger = logging.getLogger(__name__)

class DriveClient(object):
    
    def login(self, access_token=None, refresh_token=None, token_uri='https://www.googleapis.com/oauth2/v4/token', client_id=None, client_secret=None):
        """
        Login into Google drive
        args:
            access_token: (str) must get it from https://developers.google.com/oauthplayground
            refresh_token: (str) refresh token get it from oauth play ground
            token_uri: (str) oauth token uri
            clien_id: (str) get if from google api console
            client_scrent: (str) get it from google api console
        returns:
            oauth credentials dictionary
        """
        try:
            credentials = google.oauth2.credentials.Credentials(access_token, refresh_token=refresh_token, token_uri=token_uri, client_id=client_id, client_secret=client_secret)
        except Exception as err:
            logger.error("Error occurred while accessing oauth2: {0}".format(err))
            raise
        else:
            if self.is_token_valid(credentials) and self.access_token_in_cred(credentials) and self.refresh_token_in_cred(credentials):
                self.credentials = credentials
                logger.debug("The login credentials are valid: {0}".format(credentials.valid))
                logger.debug("The credentials are details are: {0}".format(str(credentials.to_json())))
            else:
                raise Exception("Invalid tokens")

    def get_credentials(self):
        return self.credentials

    def is_token_valid(self, cred):
        return cred.valid
    
    def access_token_in_cred(self, cred):
        if 'token' in cred.to_json():
            return True
        else:
            return False

    def refresh_token_in_cred(self, cred):
        if 'refresh_token' in cred.to_json():
            return True
        else:
            return False

    def client_id_in_cred(self, cred):
        if 'client_id' in cred.to_json():
            return True
        else:
            return False

    def refresh_token(self):
        self.credentials.refresh

    def get_access_token(self):
        return self.credentials.to_json()['token']

    def get_client_secret(self):
        return self.credentials.to_json()['client_secret']

    def get_refresh_token(self):
        return self.credentials.to_json()['refresh_token']

    def get_token_uri(self):
        return self.credentials.to_json()['token_uri']

    def get_client_id(self):
        return self.credentials.to_json()['client_id']