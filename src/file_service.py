
from googleapiclient import discovery
from googleapiclient.http import MediaIoBaseDownload
from mime_type import MIME_TYPES
from utils import logging_cfg

import logging
import io

logger = logging.getLogger(__name__)

class FileService(object):    
    def create_service(self, drive='drive',api_version='v3', credentials=None):
        """
        create drive service to access the files from google drive
        NOTE: current supported API version is 3
        Args:
            drive: (str) Name of GSuite service
            api_version: (str) v3 supported
            credentials: (dict) OAUTH2 credentials dict
        """
        self.drive_service = discovery.build('drive', 'v3', credentials=credentials)
        # print(dir(drive_service))
        logger.debug(dir(self.drive_service))
        logger.debug(str(self.drive_service))

    def get_drive_service(self):
        return self.drive_service

    def list_files(self, file_name):
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
        self.query_results = self.drive_service.files().list(
                q = "name contains '{0}'".format(file_name), fields="nextPageToken, files(id, name, mimeType, starred, trashed, owners)"
            ).execute()
        logger.debug(str(self.query_results))
        if self.query_results.get('files'):
            return self.query_results.get('files')
        else:
            raise Exception("No files found with query contains in the drive, please check. See more information about query https://developers.google.com/drive/api/v3/reference/query-ref#fn1")

    def download(self, file_names):
        '''
        Download list files
        Args:
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
        is_download = False
        for idx, file in enumerate(file_names, start=1):
            file_id = file['id']
            mimeType= file['mimeType']
            if mimeType in MIME_TYPES:
                mimeType = MIME_TYPES[mimeType]
            else:
                print("The requested conversion is not supported.")
                logger.debug("The requested conversion is not supported.")
                continue
            output_file = str(idx) + "_" + file['name']
            print("file_id: {0}, mimeType: {1}, output_file: {2}".format(file_id, mimeType, output_file))
            logger.info("file_id: {0}, mimeType: {1}, output_file: {2}".format(file_id, mimeType, output_file))
            if mimeType == 'text/plain':
                request = self.drive_service.files().get_media(fileId=file_id)
            else:
                request = self.drive_service.files().export_media(fileId=file_id,mimeType=mimeType)

            fh = io.BytesIO()
            self.download_file(request, fh, output_file)
            fh.close()
            is_download = True
        return is_download

    def download_file(self, request, fh, output_file):
        try:
            downloader = MediaIoBaseDownload(fh, request)
            done = False
            while done is False:
                status, done = downloader.next_chunk()
                print("Download %d%%." % int(status.progress() * 100))
                logger.info("Download %d%%." % int(status.progress() * 100))
        except Exception as err:
            print("Error occurred: {0}".format(err))
            logger.error("Error occurred while downloading: {0}".format(err))
        # If duplicates are there suffice with enumerate idx
        with open(output_file,'wb') as out:
            out.write(fh.getvalue())