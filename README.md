# GCPPD (Gource Collaborator Profile Picture Downloader)
This script automatically downloads (or attempts to download) all user avatars associated with a github repository.
Its intended usage is to make more interesting gource visualizations easier.

### Usage
1. Create a personal github access token. This can be done [here](https://github.com/settings/tokens). Your token does not need any permissions.
1. Install Python 3. You can download the latest version [here](https://www.python.org/downloads/). If you're unsure whether you have Python installed, run `python3 --version` in your terminal. If it returns a version number, you are good to go.
1. (optional but recommended) Create a new virtual environment by typing `python3 -m venv <folder name>`. If this returns an error, make sure that the python3 venv tool is installed by running `sudo apt install python3-venv`. If you decide to not create a virtual environment, continue at step 5.
1. Activate the virtual environment by typing `source <folder name>/bin/activate`.
1. Install the required dependencies by typing `python3 -m pip install -r requirements.txt`.
1. Run the script. Either provide the needed info using command line parameters or enter them when the script asks you to.

### Command line parameters
|Parameter|Short form|Usage|
|---------|----------|-----|
|`--token`|`-t`|A personal GitHub access token|
|`--user`|`-u`|The user the target repository belongs to
|`--repository`|`-r`|The target repository|

### Example
Using parameters
```
$ python3 gcppd.py --token TOKEN_HERE --user InitialPosition --repository GCPPD
Getting user instance for "InitialPosition"...
Done.
Searching for repository "GCPPD"...
Repository found.
Collecting repository collaborators...
Collected 1 user(s).
Downloading avatar for user "InitialPosition" (https://avatars0.githubusercontent.com/u/23456524?v=4)...
File download complete.
```

Without parameters
```
$ python3 gcppd.py 
GitHub Access Token: 
Repository Owner: InitialPosition
Repository Name: GCPPD
Getting user instance for "InitialPosition"...
Done.
Searching for repository "GCPPD"...
Repository found.
Collecting repository collaborators...
Collected 1 user(s).
Downloading avatar for user "InitialPosition" (https://avatars0.githubusercontent.com/u/23456524?v=4)...
File download complete.
```
