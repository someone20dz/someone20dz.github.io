
from os import system
import argparse


def auto_push(remote : str, branch : str, msg : str) -> None:

    git_command = f'git status && git add . && git commit -m "{msg}" && git push {remote} {branch}'

    try:
        if remote == 'origin':
            system(git_command)
        elif remote != 'origin':
            system(git_command + ' -f')
    except:
        raise ValueError('Remote, Branch, commit message cannot be blank.')
    else:
        print('Your commit has successfully been added.')


parser = argparse.ArgumentParser()
parser.add_argument("msg", type=str,
                    help="your commit message")
parser.add_argument("-b", "--branch", type=str, default="main",
                    help="your branch name")
parser.add_argument("-r","--remote", type=str, default="origin",
                    help="your remote name (Default: origin)")

args = parser.parse_args()

remote_name = args.remote
branch_name = args.branch
commit_msg = args.msg

auto_push(remote_name, branch_name, commit_msg)
