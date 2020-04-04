## Basic Usage
To execute this sample app, export all secrets as environment variables

1. For Linux: use ``export`` for more information visit this link https://askubuntu.com/a/58828
2. For Windows: use ``set`` for more information how to please visit this link https://superuser.com/a/79614


``` Bash

(venv) vkosuri@vkosuri:~/github/GDriveDownload$ python examples/download.py -h
usage: download.py [-h] --name NAME [--logfile LOGFILE]

Process input arguments.

optional arguments:
  -h, --help         show this help message and exit
  --name NAME        please input file name to download
  --logfile LOGFILE  logger file

(venv) vkosuri@vkosuri:~/github/GDriveDownload$ python examples/download.py --name Test
file_id:1sd1v4voW1GQKgzjKPYFD5ZfMEo7G3X-Ord4EdQ4_bA, file_name:Test
file_id:1sdf99J_1U_fP_VfE-80QS-zHgl5BgKn6Hi8IjaeWFK5A, file_name:Test

```
