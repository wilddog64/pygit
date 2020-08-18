import pygit.client as Git
from pygit.core import pull, checkout, branch
import argparse
from pygit.utils import get_current_execution_path
from pygit.utils import add_bool_argument

def git():
    optParser = argparse.ArgumentParser(prog='git',
            description='python git',
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            argument_default=argparse.SUPPRESS)
    optParser.add_argument('--git-url', '-g', default='https://github.com/bigfishgames', dest='git_url')
    optParser.add_argument('--repo-path', '-p', default='/tmp', dest='repo_path')
    optParser.add_argument('--repo-name', '-n', default='', dest='repo_name')
    optParser.add_argument('--branch-name', '-b', default='deploy_branch', dest='branch_name')
    optParser.add_argument('--commit', '-c', default='', dest='commit')
    add_bool_argument(optParser, 'removerepo', default=True)
    args = optParser.parse_args()

    print('git url %s' % (args.git_url))
    print('repo path: %s' % (args.repo_path))
    print('repo name: %s' % (args.repo_name))
    print('branch name: %s' %(args.branch_name))
    print('remove repo? %s' % (args.removerepo))

    repo_url = "%s/%s" % (args.git_url, args.repo_name)
    print('repo url %s' % (repo_url,))

    repo = "%s/%s" % (args.repo_path, args.repo_name)
    Git.clone_repo_to_local(
            git_url=repo_url,
            repo_path=args.repo_path,
            app_name=args.repo_name,
            force_remove_repo=args.removerepo
            )
    Git.pull(repoPath=repo)
    Git.remove_repo_untrack_files(repo_path=repo)
    if Git.branch_exists(branch_name=args.branch_name, repo_path=repo):
        branch(args.branch_name, _cwd=repo, d=True)
    checkout(args.commit, b=args.branch_name,  _cwd=repo)

if __name__ == '__main__':
    git()
