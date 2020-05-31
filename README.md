`pip install -r requirements.txt`

1. Create a repo, add user with commit rights.
2. Set `DYNALIST_FILE_ID` of the dynalist file to be backed up from URL of dyanlist document.
Specify `DYNALIST_API_KEY`, backups `REPO_ADDRESS`, `LOCAL_PATH` for repo, `LOCAL_TARGET_FILE` name.
3. Run `python backup.py` periodically to keep dynalist up to date on github repo.
