# GCPPD (Gource Collaborator Profile Picture Downloader)
This script automatically downloads (or attempts to download) all user avatars associated with a github repository.
Its intended usage is to make more interesting gource visualizations easier.

### Usage
1. Create a personal github access token. This can be done [here](https://github.com/settings/tokens). (Your token needs the `public_repo` permission.)
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

### Known problems
- Due to GitHub API restrictions, if you don't have push permissions in the target repository, you can only fetch avatars of users that forked the main repository.
