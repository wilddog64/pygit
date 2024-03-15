from __future__ import print_function
import sh
from sh import git
import os
import shutil
import sys
import pygit.utils
import sys

def __git(subcmd, **kwargs):
    git_object = None
    if hasattr(git, subcmd):
        git_object = getattr(git, subcmd)
    return git.bake('--no-pager', subcmd, **kwargs)


def status(**kwargs):
    return __git('status', **kwargs)


def log(**kwargs):
    return  __git('log', **kwargs)()


def add(edit=None, **kwargs):
    return  __git('add', **kwargs)(edit)


def diff(*args, **kwargs):
    _diff = __git('diff', **kwargs)
    out = _diff(*args)
    return out

def commit(checkout=None, **kwargs):

    if checkout is None:
        git_commit_output = __git('commit', **kwargs)()
    else:
        git_commit_output = __git('commit', **kwargs)(checkout)

    return git_commit_output


def clone(repo_url=None, app_name=None,  **kwargs):
    git_clone_output = None
    if app_name is None:
        git_clone_output = __git('clone', **kwargs)(repo_url)
    else:
        git_clone_output = __git('clone', **kwargs)(repo_url, app_name)

    return git_clone_output

def branch(name=None, **kwargs):
    return __git('branch', **kwargs)(name)


def checkout(commit=None, **kwargs):
    if commit is None:
        return __git('checkout', **kwargs)()
    else:
        return __git('checkout', **kwargs)(commit)


def merge(head=None, **kwargs):
    return __git('merge', **kwargs)(head)


def init(repo=None, **kwargs):
    return __git('init', **kwargs)(repo)


def clean(**kwargs):
    return __git('clean', **kwargs)()


def symbolic_ref(*args, **kwargs):
    symbolic_ref = __git('symbolic-ref', **kwargs)
    output = symbolic_ref(*args)
    return output


def push(*args, **kwargs):
    push = __git('push', **kwargs)
    return push(*args)


def pull(*args, **kwargs):
    pull = __git(**kwargs)
    return pull(*args)


def rev_parse(*args, **kwargs):
    revParse = __git('rev-parse', **kwargs)
    output = revParse(*args)
    return (output.exit_code, output)


def diff_files(**kwargs):
    output = __git('diff-files',**kwargs)()
    return output.exit_code

def ls_files(*args, **kwargs):
    lsFiles = __git('ls-files', **kwargs)
    output = lsFiles(*args)

    return output

def show_ref(*args, **kwargs):
    showRef = __git('show-ref', **kwargs)
    output = showRef(*args)

    return output

def ls_remote(*args, **kwargs):
    lsRemote = __git('ls-remote', **kwargs)
    return lsRemote(*args)

def show(*args, **kwargs):
    gitShow = __git('show', **kwargs)
    return gitShow(*args)

def tag(*args, **kwargs):
    gitTag = __git('tag', **kwargs)
    return gitTag(*args)

if __name__ == '__main__':
    print("testing __git('status', s=True)")
    g_status_short = __git('status', s=True)
    out = g_status_short()
    print(out)
    print("end testing __git('status', s=True)")

    repo_url = 'git@bitbucket.org:wildwildwest64/pygit.git'
    app_name = 'pygit'
    print("testing clone(%s, %s, _cwd='/tmp' ) % (repo_url, app_name)")
    repo_path = '/tmp/{}'.format(app_name)
    if os.path.exists(repo_path):
        shutil.rmtree(repo_path)
    clone_output = clone(repo_url,
                         app_name,
                         _cwd='/tmp',
                         recurse_submodules=False)

    print(clone_output, end='')
    print("end testing clone(%s, %s, _cwd='/tmp' ) % (repo_url, app_name)")

    print("testing checkout(b='testing') -- git checkout -b testing")
    checkout(commit=None, b='testing', _cwd='/tmp/{}'.format(app_name))
    checkout('master', _cwd='/tmp/%s' % app_name)
    print("testing checkout(b='testing') -- git checkout -b testing")
    print("testing status(s=True) -- git status -s")
    g_status = status(s=True)()
    print(g_status, end='')
    print("end testing status(s=True) -- git status -s")

    print("testing status -- git status")
    g_status = status()
    print(g_status(), end='')
    print("end testing status -- git status")

    print("testing log(oneline=True, n=10) -- git log --oneline -10")
    log_output = log(oneline=True, n=10)
    print(log_output, end='')
    print("end testing log(oneline=True, n=10) -- git log --oneline -10")

    print("testing add('.', n=True) -- git add . -n")
    add_output = add('.', n=True)
    print(add_output, end='')
    print("end testing add('.', n=True) -- git add . -n")
    print()
    print("testing diff() -- git diff")
    diff_output = diff()
    print(diff_output, end='')
    print("end testing diff() -- git diff")

    print("testing commit(None, dry_run=True, n=True, m='testing') -- git commit -n -m 'testing', .")
    if diff_files(_cwd='.'):
        commit_output = commit(None, a=True, dry_run=True, m='testing commit')
        print(commit_output)
    print("end testing commit(None, dry_run=True, n=True, m='testing') -- git commit -n -m 'testing', .")
    print()
    print('--- testing rev_parse ---', file=sys.stderr)
    print('checking branch existenance')
    return_code = (rev_parse('git-client', _cwd='.', quiet=True, verify=True, _ok_code=[0, 1]))[0]
    print('check_branch return code is: %d' % return_code)
    print('checking if a given project is a git repo', file=sys.stderr)
    return_code = (rev_parse(_cwd='/tmp', is_inside_work_tree=True, quiet=True, _ok_code=[0, 128]))[0]
    print('return code for check project is git repo is %d' % return_code)
    print('--- end testing rev_parse ---', file=sys.stderr)
    print()
    print('-- test diff_files ---')
    rc = diff_files(_cwd='/tmp/{}'.format(app_name), q=True)
    print('is workspace dirty %d' % rc)
    print('-- end test diff_files ---')
    print()
    print('--- testing ls_files() ---')
    output = ls_files(_cwd='.', other=True)
    if output:
        print('return code is %d' % output.exit_code)
        print('found untracked files in current repo %s' % output, file=sys.stderr)

    print('--- test show-ref ---')
    output = show_ref(dereference=True)
    if output:
        print(output)
    print('--- end test show-ref')

    print('--- test ls-remote')
    output = ls_remote('origin', get_url=True)
    print(output)
    print('--- end test ls-remote')
    print(' test show')
    print('--- test git show ---')
    print(show())
    print('--- end test git show')
