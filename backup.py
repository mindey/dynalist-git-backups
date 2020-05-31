import os
import yaml
import dynapi
import datetime
from git import Repo


DYNALIST_FILE_ID = ''
DYNALIST_API_KEY = ''
REPO_ADDRESS = 'git@github.com:user/repo.git'
LOCAL_PATH = '/path/to/local/backups/repo/folder'
LOCAL_TARGET_FILE = os.path.join(LOCAL_PATH, '<MY_FILENAME>.yaml')


# --- (1) SPACE TO BACKUP ---
try:
    repo = Repo.clone_from(REPO_ADDRESS, LOCAL_PATH)
except:
    repo = Repo(LOCAL_PATH)

remote = repo.remote()

try:
    remote.pull()
except:
    pass

# --- (2) THINGS TO BACKUP ---
yaml.default_flow_style = False
io = dynapi.DynalistIO()
io.API_KEY = DYNALIST_API_KEY
f = io.get_file(file_id=DYNALIST_FILE_ID); datestring = datetime.datetime.utcnow().isoformat()

with open(LOCAL_TARGET_FILE, 'w') as g:
    yaml.dump(f.doc, stream=g, allow_unicode=True)

# --- (2) PROCESS TO BACKUP ---
repo.index.add([LOCAL_TARGET_FILE])
try:
    repo.git.commit(m=f'Updates: {datestring}')
    remote.push('master')
    print("made new commit")
except:
    print("nothing commited")
