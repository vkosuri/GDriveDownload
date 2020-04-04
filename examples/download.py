#!/bin/python3

'''
Author: Mallikarjunaroa Kosuri
Usage:
    download.py --name Test
'''
from googleapiclient.http import MediaIoBaseDownload
from google.auth.exceptions import GoogleAuthError
from googleapiclient import discovery

import argparse
import google.oauth2.credentials
import io
import json
import logging
import os
import requests
import sys


# Don't initialize logger here, configuration requires the log filename from
# the argument parser, see the logging_cfg method
logger = None

def logging_cfg(filename):
    """ Create a FileHandler based logfile for logging """
    global logger

    file_path = os.path.join(os.getcwd(), filename)

    logging.basicConfig(datefmt='%H:%M:%S',
                        format='%(asctime)s.%(msecs)-03d  %(name)-12s \
                        %(levelname)-8s %(message)s',
                        filename=file_path, level=logging.NOTSET)

    logger = logging.getLogger(__name__)

def login(access_token=None, refresh_token=None, token_uri='https://www.googleapis.com/oauth2/v4/token', client_id=None, client_secret=None):
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
        logger.debug("Dir credentials: {0}".format(dir(credentials)))
        logger.debug("The login credentials are valid: {0}".format(credentials.valid))
        logger.debug("The credentials are details are: {0}".format(str(credentials.to_json())))
        return credentials

def create_service(drive='drive',api_version='v3', credentials=None):
    """
    create drive service to access the files from google drive
    NOTE: current supported API version is 3
    Args:
        drive: (str) Name of GSuite service
        api_version: (str) v3 supported
        credentials: (dict) OAUTH2 credentials dict
    returns:
        returns drive_service
    """
    drive_service = discovery.build('drive', 'v3', credentials=credentials)
    print(dir(drive_service))
    logger.debug(str(drive_service))
    return drive_service

def list_files(file_name, drive_service):
    """
    List files with give name including duplicates
    Args:
        file_name: (str) name of the file(s) to get
        drive_service: gdrive object
    See
        list of supported query operators https://developers.google.com/drive/api/v3/ref-search-terms#operators
        File serarch operations https://developers.google.com/drive/api/v3/search-files
    returns:
        list of files including duplicates
    """
    results = drive_service.files().list(q = "name contains '{0}'".format(file_name), fields="nextPageToken, files(id, name, mimeType, starred, trashed, owners)").execute()
    logger.debug(str(results))
    return results.get('files',[])

def download(drive_service, file_names):
    '''
    Downlods files using contains query
    Args:
        drive_service: drive_service object
        files: (list) list of files or file
    NOTE:
        1. Exports a Google Doc to the requested MIME type and
        returns the exported content. Please note that the exported
        content is limited to 10MB. Try it now.
        2. GSuite allows duplicate file names, to avoid we are suffix enumerate idx
        3. The supported mime types are listed here https://developers.google.com/drive/api/v3/ref-export-formats
    return:
        void, files will be download in current directory
    '''
    guess_mime_type = {
        "application/vnd.google-apps.document":"application/vnd.oasis.opendocument.text",
        "application/vnd.google-apps.spreadsheet":"application/x-vnd.oasis.opendocument.spreadsheet",
        'application/vnd.google-apps.presentation' : 'application/vnd.oasis.opendocument.presentation',
    }

    for idx, file in enumerate(file_names, start=1):
        file_id = file['id']
        mimeType= file['mimeType']
        fh = io.BytesIO()
        if mimeType in guess_mime_type:
            mimeType = guess_mime_type[mimeType]
        output_file = file['name'] + "_" + str(idx)
        print("file_id: {0}, mimeType: {1}, output_file: {2}".format(file_id, mimeType, output_file))
        logger.info("file_id: {0}, mimeType: {1}, output_file: {2}".format(file_id, mimeType, output_file))
        try:
            request = drive_service.files().export_media(fileId=file_id,mimeType=mimeType)
            downloader = MediaIoBaseDownload(fh, request)
            done = False
            while done is False:
                status, done = downloader.next_chunk()
                print("Download %d%%." % int(status.progress() * 100))
                logger.info("Download %d%%." % int(status.progress() * 100))
        except Exception as err:
            print("Error occurred: {0}".format(err))
            logger.error("Error occurred: {0}".format(err))
        # If duplicates are there suffice with enumerate idx
        with open(output_file,'wb') as out:
            out.write(fh.getvalue())
        fh.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process input arguments.')
    parser.add_argument('--name', required=True, type=str, help='please input file name to download')
    parser.add_argument('--logfile', default="drivelog.log", required=False, type=str, help='logger file')
    args = parser.parse_args()

    # Logging
    logging_cfg(args.logfile)

    # get values from environment
    access_token = os.environ.get('ACCESS_TOKEN')
    refresh_token = os.environ.get('REFRESH_TOKEN')
    token_uri = os.environ.get('TOKEN_URI')
    client_id = os.environ.get('CLIENT_ID')
    client_secret = os.environ.get('CLIENT_SECRET')

    # login to Google drive
    cred = login(access_token, refresh_token, token_uri, client_id, client_secret)
    # https://developers.google.com/apps-script/reference/drive
    drive_service = create_service('drive','v3',cred)
    files = list_files(args.name, drive_service)
    for file in files:
        print("file_id:{0}, file_name:{1}, mimeType:{2}".format(file['id'], file['name'], file['mimeType']))
    # download files
    download(drive_service, files)
