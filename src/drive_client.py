
from google.auth.exceptions import GoogleAuthError
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
        A nice video about how to get refresh token https://www.youtube.com/watch?v=hfWe1gPCnzc
        args:
            access_token: (str) must get it from https://developers.google.com/oauthplayground
            refresh_token: (str) refresh token get it from oauth play ground
            token_uri: (str) oauth token uri
            clien_id: get if from google api console
            client_scrent: get it from google api console
        returns:
            oauth credentials dictionary
        """
        try:
            credentials = google.oauth2.credentials.Credentials(
                access_token,
                refresh_token=refresh_token,
                token_uri=token_uri,
                client_id=client_id,
                client_secret=client_secret)
        except GoogleAuthError as err:
            print("GoogleAuthError: {0}".format(err))
            logger.error(str(err))
        except:
            print("Unexpected error: {0}".format(sys.exc_info()[0]))
            logger.error("Unexpected error: {0}".format(sys.exc_info()[0]))
            raise
        else:
            logger.debug("The login credentials are valid: {0}".format(credentials.valid))
            logger.debug("The credentials are details are: {0}".format(str(credentials.to_json())))
            self.credentials = credentials
    
    def get_credentials(self):
        return self.credentials

    def is_token_valid(self):
        return self.credentials.valid
    
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