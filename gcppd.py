
from argparse import ArgumentParser

from GithubFunctions import GithubImageDownloadConnection

from getpass import getpass

# import arguments
parser = ArgumentParser(description='This script downloads all user avatars that collaborated to a given GitHub repo.')
parser.add_argument('--token', '-t', help='A personal GitHub access token. You can generate one here: '
                                          'https://github.com/settings/tokens')
parser.add_argument('--user', '-u', help='The user the target repository belongs to')
parser.add_argument('--repository', '-r', help='The target repository')
args = parser.parse_args()

# if we don't have needed args, we get them from cli
if args.token is None:
    args.token = getpass('GitHub Access Token: ')
if args.user is None:
    args.user = input('Repository Owner: ')
if args.repository is None:
    args.repository = input('Repository Name: ')

# generate github instance
github = GithubImageDownloadConnection(args.token)

# set user instance
github.set_user(args.user)

# get collaborators for project
github.get_project_commits(args.repository)

# download all pictures from collected authors
github.download_all_collaborator_pictures()
