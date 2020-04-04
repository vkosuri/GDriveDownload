
from drive_client import DriveClient
from utils import logging_cfg

import argparse


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
    cred = DriveClient.login(access_token, refresh_token, token_uri, client_id, client_secret)
    if not cred.valid:
        return "Login failed"
    # https://developers.google.com/apps-script/reference/drive
    drive_service = create_service('drive','v3',cred)
    files = list_files(args.name, drive_service)
    for file in files:
        print("file_id:{0}, file_name:{1}, mimeType:{2}".format(file['id'], file['name'], file['mimeType']))
    # download(files)
