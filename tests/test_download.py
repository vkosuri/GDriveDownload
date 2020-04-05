
import json
import mock
import unittest2 as unittest
from file_service import FileService

class TestDownload(unittest.TestCase):
    def test_file_download(self):
        pass

    def test_raise_site_conversion(self):
        fs = FileService()
        file_list = {'files': [{'id': '0', 'name': 'Test', 'mimeType': 'mimeType:application/vnd.google-apps.site', 'starred': False, 'trashed': False, 'owners': [{'kind': 'drive#user', 'displayName': 'Malliarjunarao Kosuri', 'me': True, 'permissionId': '123', 'emailAddress': 'rhelvkosuri@gmail.com'}]}]}
        assert fs.download(file_list['files']) == False

    def test_raise_map_conversion(self):
        fs = FileService()
        file_list = {'files': [{'id': '0', 'name': 'Test', 'mimeType': 'mimeType:application/vnd.google-apps.map', 'starred': False, 'trashed': False, 'owners': [{'kind': 'drive#user', 'displayName': 'Malliarjunarao Kosuri', 'me': True, 'permissionId': '123', 'emailAddress': 'rhelvkosuri@gmail.com'}]}]}
        assert fs.download(file_list['files']) == False

    def test_raise_drawing_conversion(self):
        fs = FileService()
        file_list = {'files': [{'id': '0', 'name': 'Test', 'mimeType': 'mimeType:application/vnd.google-apps.drawing', 'starred': False, 'trashed': False, 'owners': [{'kind': 'drive#user', 'displayName': 'Malliarjunarao Kosuri', 'me': True, 'permissionId': '123', 'emailAddress': 'rhelvkosuri@gmail.com'}]}]}
        assert fs.download(file_list['files']) == False

    def test_raise_form_conversion(self):
        fs = FileService()
        file_list = {'files': [{'id': '0', 'name': 'Test', 'mimeType': 'mimeType:application/vnd.google-apps.form', 'starred': False, 'trashed': False, 'owners': [{'kind': 'drive#user', 'displayName': 'Malliarjunarao Kosuri', 'me': True, 'permissionId': '123', 'emailAddress': 'rhelvkosuri@gmail.com'}]}]}
        assert fs.download(file_list['files']) == False

if __name__ == '__main__':
    unittest.main()
