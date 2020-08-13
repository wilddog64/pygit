import pygit.client as Git
import argparse
from pygit.utils import get_current_execution_path
from pygit.utils import add_bool_argument

def git():
    optParser = argparse.ArgumentParser(prog='git',
            description='python git',
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            argument_default=argparse.SUPPRESS)
    optParser.add_argument('--git-url', '-g', default='github.com/bigfishgames', dest='git_url')
    optParser.add_argument('--repo-path', '-p', default='/tmp', dest='repo_path')
    optParser.add_argument('--repo-name', '-n', default='', dest='repo_name')
    optParser.add_argument('--branch-name', '-b', default='deploy_branch', dest='branch_name')
    add_bool_argument(optParser, 'removerepo', default=True)
    args = optParser.parse_args()

    print('git url %s' % (args.git_url))
    print('repo path: %s' % (args.repo_path))
    print('repo name: %s' % (args.repo_name))
    print('branch name: %s' %(args.branch_name))
    print('remove repo? %s' % (args.removerepo))

if __name__ == '__main__':
    git()
