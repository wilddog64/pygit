import pygit.client as Git
import argparse
from pygit.utils import get_current_execution_path

def git():
    optParser = argparse.ArgumentParser(prog='git',
            description='python git',
            formatter_class=argparse.ArgumentDefaultHelpFormatter,
            argument_default=argparse.SUPRESS)
    optParser.add_argument('--repo-path', '-p', default='/tmp')
    optParser.add_argument('--repo-name', '-n', default='')

    optParser.add_argument('--branch-name', '-b', default='deploy_branch')
    optParser.add_argument('--remove-repo', '-r', action='store_true')
