from imghdr import what
from os import mkdir, rename
from os.path import isdir
from urllib.request import urlretrieve

from github import Github
from github.GithubException import UnknownObjectException, GithubException


class GithubImageDownloadConnection:

    GITHUB_CLIENT = None
    USER = None
    DOWNLOAD_LIST = []
    REPO = None

    def __init__(self, token):
        self.GITHUB_CLIENT = Github(token)

    def set_user(self, username, silent=False):
        if silent is False:
            print(f'Getting user instance for "{username}"...')

        # get the github user instance
        try:
            print('Done.')
            self.USER = self.GITHUB_CLIENT.get_user(username)

        except UnknownObjectException:
            print('User does not exist. Aborting...')
            exit(-1)

    def get_repo(self, target_repo_name):
        if self.USER is not None:
            print(f'Searching for repository "{target_repo_name}"...')

            for project in self.USER.get_repos():
                if project.name.upper() == target_repo_name.upper():
                    print('Repository found.')

                    self.REPO = project.name
                    return project

            # if we get here, we didn't find the project
            print('Repository not found. Aborting...')
            exit(-1)

    def get_project_collaborators(self, project_name):
        project = self.get_repo(project_name)

        print('Collecting repository collaborators...')

        try:
            for collaborator in project.get_collaborators():
                self.DOWNLOAD_LIST.append(collaborator)
        except GithubException as e:
            if e.status == 403:
                print('You don\'t have push rights for this repository. Falling back to repo forks...')

                for fork in project.get_forks():
                    self.DOWNLOAD_LIST.append(fork.owner)

        print(f'Collected {len(self.DOWNLOAD_LIST)} user(s).')
        self.download_all_collab_pictures()

    def download_all_collab_pictures(self):
        # create dir if it doesn't exist
        if isdir('images') is False:
            print('Creating image directory...')
            mkdir('images')

        if isdir(f'images/{self.REPO}') is False:
            print('Creating project image directory...')
            mkdir(f'images/{self.REPO}')

        for user in self.DOWNLOAD_LIST:
            print(f'Downloading avatar for user "{user.login}" ({user.avatar_url})...')

            urlretrieve(user.avatar_url, f'images/{self.REPO}/{user.login}')

            # file format handling
            file_format = what(f'images/{self.REPO}/{user.login}')
            if file_format is None:
                file_format = 'jpg'

            rename(f'images/{self.REPO}/{user.login}', f'images/{self.REPO}/{user.login}.{file_format}')

        print('File download complete.')
