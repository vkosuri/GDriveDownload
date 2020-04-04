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
See [Create Environment](https://github.com/vkosuri/GDriveDownload/wiki/Create-local-environment) wiki

## Set OAUTH credentials
First generate OAUTH 2.0 credential for drive API.

A nice video about [Generating a refresh token for YouTube API calls using the OAuth playground](https://www.youtube.com/watch?v=hfWe1gPCnzc)

Get all the required from OAUTH playground, and export those variable into personal machine. if it is windows please ``set`` operator.

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

See more information about [Authorization](https://github.com/vkosuri/GDriveDownload/wiki/Authorization) wiki

## Manual Inputs
With current OAUTH2.0 user has to authenticate through browser by supplying his Google account information. In order to avoid browser steps **Exchanging the authorization code for a refresh token** method chosen.

More information described in [Why we are using refresh tokens](https://github.com/vkosuri/GDriveDownload/wiki/Why-we-are-using-refresh-tokens) wiki

## Supported Features
1. Download
2. Search files

## Future Enhancements
3. Upload documents
4. Delete documents

## Known Issues
1. To download document the export api functionality was used, Please note that the exported content is limited to 10MB. Try it now.
2. GSuite allows duplicate file names, to avoid we are suffix enumerate idx
3. The supported mime types are converted into Linux formated, the MIME types are listed here https://developers.google.com/drive/api/v3/ref-export-formats

## Examples
See examples in [examples](./examples) directory
``` Bash
python examples/download.py --name Test
```

## Motivation
It's interview exercise from RHEL.
* Downloads your files from Google Drive OR Google contacts to the local disk
* The program should be triggered using a command line
* Write extensive tests to test your code; preferably break your code
* The scenarios that could not be automated, document them

## LICENSE
This application [LICESE](./LICENSE) under **UNLICENSE**
