## Google drive download
Download and search files users own Google drive.

## Prerequisites
1. python 3.x
2. pip
3. virtualenv
4. git
5. Google Drive API and OAUTH 2.0

## Create Environment
To set use [virtual environments](https://docs.python.org/3/tutorial/venv.html) it will poulte your global python packages.

``` Bash
# Install all required packages before
pip install -r requirements.txt
```
See detailed instructions [setting your environment](https://github.com/vkosuri/GDriveDownload/wiki/Create-local-environment) documented in wiki page.

## Get OAUTH credentials
To Get OAUTH 2.0 credential from Google console API, you should fallow certain steps to create OAUTH2.0 API. See more information about [Authorization](https://github.com/vkosuri/GDriveDownload/wiki/Authorization) wiki

Get all the required information from OAUTH playground

To set evironemnt variables
1. On Linux: use ``export`` for more information visit this link https://askubuntu.com/a/58828
2. On Windows: use ``set`` for more information how to please visit this link https://superuser.com/a/79614

``` Bash
export ACCESS_TOKEN='ya29.a0Ae4lvC21ganpclkqIIs7bop8vZLp4rQUQGBO3YWKpOSsEDr1_gdEYpbXRN1N'
export CLIENT_ID='1csubnj27sfd1212f0j2i.apps.googleusercontent.com'
export CLIENT_SECRET='Yd1KvAN0XuSERWhJ'
export REFRESH_TOKEN='1//04xnISQinw7YwCgYIARAAGAQSNwF-L9IrT9jJXiNcygxEB_uFQOUpZXADwHxLKhRhhgAP'
export TOKEN_URI='https://www.googleapis.com/oauth2/v4/token'
```
---
**NOTE**

Never keep secrets anywhere inside your repository code tree

---

## Manual Inputs
With current OAUTH2.0 user has to authenticate through browser by supplying his Google account information. In order to avoid browser steps **Exchanging the authorization code for a refresh token** method chosen.

More information described in [Why we are using refresh tokens](https://github.com/vkosuri/GDriveDownload/wiki/Why-we-are-using-refresh-tokens) wiki

## Supported Features
1. Download
2. Search files

## Future Enhancements
3. Upload documents
4. Delete documents
5. Download large files > 20MB
6. Download public and shared files

## Known Issues
1. To download files this APP uses [google export api](https://developers.google.com/drive/api/v3/reference/files/export), Please note that the exported content is limited to 10MB only.
2. GSuite allows duplicate file names because the file creation based on file_ids, while we are suffixing a number to avoid accidental overwrite with previous file name when download files.
3. GSuite supports many mimeTypes, however while downloading user chose based on local machine able launch, this is the reason user has convert given document into supported format, it's available here https://developers.google.com/drive/api/v3/ref-export-formats

## Examples
See raw examples in [examples](./examples) directory
``` Bash
python examples/download.py --name Test
```
## Testplan
1. [Credentials](./tests/credential_testplan.md)
2. [MimeTypes](./tests/mimetype_testplan.md)
3. [Adhoc](./tests/adhoc_testplan.md)

## Motivation
It's interview exercise from RHEL.
* Downloads your files from Google Drive OR Google contacts to the local disk
* The program should be triggered using a command line
* Write extensive tests to test your code; preferably break your code
* The scenarios that could not be automated, document them

## LICENSE
This application [LICESE](./LICENSE) under **UNLICENSE**
