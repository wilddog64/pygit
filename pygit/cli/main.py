import pygit.client as Git
from pygit.core import pull, checkout, branch
import argparse
from pygit.utils import get_current_execution_path
from pygit.utils import add_bool_argument

def git():
    # create an argparse object
    optParser = argparse.ArgumentParser(prog='git',
            description='python git',
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            argument_default=argparse.SUPPRESS)

    # setup up command line arguments
    optParser.add_argument('--git-url', '-g', default='https://github.com/bigfishgames', dest='git_url')
    optParser.add_argument('--repo-path', '-p', default='/tmp', dest='repo_path')
    optParser.add_argument('--repo-name', '-n', default='', dest='repo_name')
    optParser.add_argument('--branch-name', '-b', default='deploy_branch', dest='branch_name')
    optParser.add_argument('--commit', '-c', default='', dest='commit')
    add_bool_argument(optParser, 'removerepo', default=True)

    # parse command line options
    args = optParser.parse_args()

    # assign command line options to their variables
    git_url = args.git_url
    repo_path = args.repo_path
    repo_name = args.repo_name
    branch_name = args.branch_name
    removerepo = args.removerepo
    commit = args.commit

    # print out variables
    print('git url %s' % (git_url))
    print('repo path: %s' % (repo_path))
    print('repo name: %s' % (repo_name))
    print('branch name: %s' %(branch_name))
    print('remove repo? %s' % (removerepo))

    repo_url = "%s/%s" % (git_url, repo_name)
    print('repo url %s' % (repo_url,))

    repo = "%s/%s" % (repo_path, repo_name)

    # clone repo to local if it is not exist
    Git.clone_repo_to_local(
            git_url=repo_url,
            repo_path=repo_path,
            app_name=repo_name,
            force_remove_repo=removerepo
            )

    # pull from upstream
    Git.pull(repoPath=repo)

    # remove all the untracked files
    Git.remove_repo_untrack_files(repo_path=repo)

    # delete branch if it exists then checkout it again
    if Git.branch_exists(branch_name=branch_name, repo_path=repo):
        branch(branch_name, _cwd=repo, D=True)
    checkout(commit, b=branch_name,  _cwd=repo)

if __name__ == '__main__':
    git()
