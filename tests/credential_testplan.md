
This automated testplan will verify file access and oauth tokens

## Positive Tests

| Test Name          | Description                                                  | Expected | Actual |
|--------------------|--------------------------------------------------------------|----------|--------|
| user access        | check given user has access or not                           |          |        |
| Check file         | Check file available on the server not                       |          |        |
| verify download    | Verify download the successfully or not into local directory |          |        |
| User able to login | Google account exists, user should get access                |          |        |
| list files         | User able to list file with given name                       |          |        |
| download size      | Check user able to download below 10MB                       |          |        |
| Check duplicates   | Check user can download duplicate files                      |          |        |

## Negative Tests

| Test Name             | Description                             | Expected | Actual |
|-----------------------|-----------------------------------------|----------|--------|
| invalid token         | Should not accept credentials           |          |        |
| invalid client_id     | Should not accept credentials           |          |        |
| invalid client_scret  | Should not accept credentials           |          |        |
| invalid file names    | Should not accept invalid file names    |          |        |
| download size         | More than 20MB file should not download |          |        |
| invalid query         | should not accept invalid query         |          |        |
| invalid refresh token | should not accept invalid refresh token |          |        |
