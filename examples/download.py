#!/bin/python3

'''
Author: Mallikarjunaroa Kosuri
Usage:
    download.py -name Test
'''
from googleapiclient.http import MediaIoBaseDownload
from google.auth.exceptions import GoogleAuthError
from googleapiclient import discovery

import argparse
import google.oauth2.credentials
import io
import json
import os
import requests
import sys

'''
export ACCESS_TOKEN='ya29.a0Ae4lvC21ganpclkqIIs7bop8vZLp4rQUQGBO3YWKpOSsEDr1_gdEYpbXRN1Nsc12p8v7HTH1u0CE0mI1P2gqZ-JL8qYPMJFn8GeAC1nYvETeK6BppDebxuWJoHigSkt0o904-o4M_Tr5w1Cprt2hn_MFumZ7t8dSTSo'
export CLIENT_ID='184040109443-mqqsa5f2egrfcsubnj27sfd1212f0j2i.apps.googleusercontent.com'
export CLIENT_SECRET='Yd1KvAN0XuSERWhJ674-opGd'
export REFRESH_TOKEN='1//04xnISQinw7YwCgYIARAAGAQSNwF-L9IrT9jJXiNcygxEB_uFQOUpZXADwHxLKhRhhgAPkPv6wnraVKnEp4zvxjkTGXcIZGIBgFg'
export TOKEN_URI='https://www.googleapis.com/oauth2/v4/token'
'''

def login(access_token=None, refresh_token=None, token_uri='https://www.googleapis.com/oauth2/v4/token', client_id=None, client_secret=None):
    """
    Login into google drive
    A nice video about how to access token, refresh token https://www.youtube.com/watch?v=hfWe1gPCnzc
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
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
    else:
        return credentials

def create_service(drive='drive',api_version='v3', credentials=None):
    """
    create drive service to access the files from google drive
    NOTE: current supported API version is 3
    Args:
        drive: (str) Name of GSuite service
        api_version: (str) v3 supported
        credentials: (dict) OAUTH2 credentials dict
    """
    access_token = os.environ.get('ACCESS_TOKEN')
    refresh_token = os.environ.get('REFRESH_TOKEN')
    token_uri = os.environ.get('TOKEN_URI')
    client_id = os.environ.get('CLIENT_ID')
    client_secret = os.environ.get('CLIENT_SECRET')
    cred = login(access_token, refresh_token, token_uri, client_id, client_secret)
    drive_service = discovery.build('drive', 'v3', credentials=cred)
    return drive_service

def get_files(drive_service, file_name):
    """
    Get files from drive service
    Args:
        drive_service: drive_service
        file_name: name of the file download
    See 
        list of supported query operators https://developers.google.com/drive/api/v3/ref-search-terms#operators
        File serarch operations https://developers.google.com/drive/api/v3/search-files
    """
    results = drive_service.files().list(q = "name = '{0}'".format(file_name), fields="nextPageToken, files(id, name, mimeType, starred, trashed, owners)").execute()
    return results.get('files',[])

def download(files):
    '''
    Download list files
    Args:
        files: list of files
    NOTE:
        1. Exports a Google Doc to the requested MIME type and
        returns the exported content. Please note that the exported
        content is limited to 10MB. Try it now. 
        2. GSuite allows duplicate file names, to avoid we are suffix enumerate idx 
        3. The supported mime types are listed here https://developers.google.com/drive/api/v3/ref-export-formats
    '''
    guess_mime_type = {
        "application/vnd.google-apps.document":"application/vnd.oasis.opendocument.text",
        "application/vnd.google-apps.spreadsheet":"application/x-vnd.oasis.opendocument.spreadsheet"
    }

    for idx, file in enumerate(results.get('files',[]), start=1):
        file_id = file['id']
        mimeType= file['mimeType']
        if mimeType in guess_mime_type:
            mimeType = guess_mime_type[mimeType]
        output_file = file['name'] + "_" + str(idx)
        print("file_id: {0}, mimeType: {1}, output_file: {2}".format(file_id, mimeType, output_file))
        try:
            request = driveService.files().export_media(fileId=file_id,mimeType=mimeType)
            fh = io.BytesIO()
            downloader = MediaIoBaseDownload(fh, request)
            done = False
            while done is False:
                status, done = downloader.next_chunk()
                print("Download %d%%." % int(status.progress() * 100))
        except Exception as err:
            print("Error occured: {0}".format(err))
        # If dulicates are there replace
        with open(output_file,'wb') as out:
            out.write(fh.getvalue())
        fh.close()

if __name__ == "__main__":
