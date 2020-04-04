#!/bin/python3

'''
Author: Mallikarjunaroa Kosuri
Usage:
    download.py --name Test
'''
from drive_client import DriveClient
from file_service import FileService
from utils import logging_cfg
from mime_type import MIME_TYPES

import argparse
import os

# Don't initialize logger here, configuration requires the log filename from
# the argument parser, see the logging_cfg method
logger = None

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
    ds = DriveClient()
    ds.login(access_token, refresh_token, token_uri, client_id, client_secret)
    cred = ds.get_credentials()

    # create file services
    # https://developers.google.com/apps-script/reference/drive
    fs = FileService()
    fs.create_service(drive='drive',api_version='v3',credentials=cred)
    files = fs.list_files('Test')
    for file in files:
        print("file_id:{0}, file_name:{1}, mimeType:{2}".format(file['id'], file['name'], file['mimeType']))
    # download files
    fs.download(files)
