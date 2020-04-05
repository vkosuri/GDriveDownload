## Google drive download
Download and search files users own Google drive.

[![Build Status](https://travis-ci.com/vkosuri/GDriveDownload.svg?branch=master)](https://travis-ci.com/github/vkosuri/GDriveDownload)

## Table Contents
1. [Prerequisites](#Prerequisites)
2. [Create Environment](#create-environment)
3. [Get OAUTH credentials](#get-oauth-credentials)
4. [Why manual inputs are required](#why-manual-inputs-are-required)
5. [Supported Features](#supported-features)
6. [Future Enhancements](#future-enhancements)
7. [Known Issues](#known-issues)
8. [Examples](#Examples)
9. [Test automation](#test-automation)
10. [Motivation](#motivation)
11. [License](#license)
12. [Better Code Hub](#better-code-hub)

## Prerequisites
1. python 3.x
2. pip
3. virtualenv
4. git
5. Google Drive API and OAUTH 2.0

## Create Environment
To use this app you need to set [python virtual environments](https://docs.python.org/3/tutorial/venv.html). The reason we are using python virtual environments it will poulte your global python packages.

``` Bash
# Install all required packages before executing example
pip install -r requirements.txt
```
See detailed instructions [setting your environment](https://github.com/vkosuri/GDriveDownload/wiki/Create-local-environment) documented in wiki page.

## Get OAUTH credentials
The next step is to create OAUTH 2.0 credential from Google console API, you should fallow certain steps to create OAUTH2.0 API. See more information about [Authorization](https://github.com/vkosuri/GDriveDownload/wiki/Authorization) wiki

Get all mandatory paramerter ``ACCESS_TOKEN``, ``CLIENT_ID``, ``CLIENT_SECRET``, ``TOKEN_URI`` and ``REFRESH_TOKEN`` to start executing this app.

Set OAUTH values as system or user environemtn variables,
1. On Linux: use ``export`` for more information visit this link https://askubuntu.com/a/58828
2. On Windows: use ``set`` for more information how to please visit this link https://superuser.com/a/79614

``` Bash
export ACCESS_TOKEN='your access token'
export CLIENT_ID='your client id'
export CLIENT_SECRET='your client secret'
export REFRESH_TOKEN='your refresh token'
export TOKEN_URI='https://www.googleapis.com/oauth2/v4/token'
```
---
**NOTE**

Never keep secrets anywhere inside your repository code tree

---

## Why manual inputs are required
OAUTH credentiaon fallows two appraoches
### Approch 1
In this approach user has to authenticate through browser by supplying his Google account information in local browser.
### Approach 2:
Get secret from your account and use [OAUTH Playground](https://developers.google.com/oauthplayground/) to get **authorization token** do  **Exchanging the authorization code for a refresh token** to get access token.

**This App uses Appraoch 2**

Detaild information described in [Getting authrization token without browser consent](https://github.com/vkosuri/GDriveDownload/wiki/Getting-authorization-token-without-browser-login) in the wiki page.

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
3. Unsupported conversion. Here are some of unsupported conversions.
```
mimeType:application/vnd.google-apps.site
mimeType:application/vnd.google-apps.map
mimeType:application/vnd.google-apps.drawing
mimeType:application/vnd.google-apps.form
```
Full list found here https://developers.google.com/drive/api/v3/ref-export-formats

## Examples
To use this API, see some exmples in [examples](./examples) directory

**NOTE:** The two steps are [Create Environment](#create-environment) and [Get OAUTH credentials](#get-oauth-credentials) mandatory to execute this example

``` Bash
python examples/download.py --name Test
```
## Test automation
1. [Credentials](./tests/credential_testplan.md)
2. [MimeTypes](./tests/mimetype_testplan.md)
3. [Adhoc](./tests/adhoc_testplan.md) These are manual tests

## Motivation
It's interview exercise from RHEL.
* Downloads your files from Google Drive OR Google contacts to the local disk
* The program should be triggered using a command line
* Write extensive tests to test your code; preferably break your code
* The scenarios that could not be automated, document them

## LICENSE
This application [LICESE](./LICENSE) under **UNLICENSE**

## Better Code Hub

The [Better Code Hub](https://bettercodehub.com) analyses how bad the code is. the compilance score is below

[![BCH compliance](https://bettercodehub.com/edge/badge/vkosuri/GDriveDownload?branch=master)](https://bettercodehub.com/)
