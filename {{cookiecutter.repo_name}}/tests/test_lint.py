#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
import os
import subprocess
import sys


class projectpath():
    def __init__(self):
        self.path = os.path.dirname(os.path.realpath(__file__))
        self.work_path = os.path.dirname(self.path)
        os.chdir(self.work_path)

    def dirpath(self):
        return (self.work_path)


def asterisks(title):

    rows, columns = os.popen('stty size', 'r').read().split()
    print(title, '*' * (int(columns) - int(len(title)) - 1) + '\n')


def motd():

    print("ANSIBLE STATIC TESTS")
    print("====================")
    print(" ")

    title = "[{{cookiecutter.repo_name}} Tests] "
    asterisks(title)


def main():

    motd()

    CROK = "\033[92m"
    CRFAIL = "\033[91m"
    CEND = "\033[0m"

    myproject = projectpath()
    work_path = myproject.dirpath()

    yamllint = subprocess.call(['which', 'yamllint'], stdout=subprocess.PIPE)

    ansiblelint = subprocess.call(['which', 'ansible-lint'],
                                  stdout=subprocess.PIPE)

    if yamllint == 0:

        title = "TASK [Testing YAMLLint]"
        asterisks(title)

        command = subprocess.call(['yamllint', work_path], stdin=None)
        if command == 0:
            print(CROK + "ok: [localhost] => (item=%s) \n" % work_path + CEND)
        else:
            print(CRFAIL + "fail: [localhost] => (item=%s) \n" % work_path +
                  CEND)
            sys.exit(1)
    else:
        print("Cannot find yamllint")

    if ansiblelint == 0:
        title = "TASK [Testing Ansible-Lint]"
        asterisks(title)

        for dirpath, dirnames, filenames in os.walk(work_path):
            for filename in filenames:
                if filename.endswith('.yml') or filename.endswith('.yaml'):
                    command = subprocess.call(
                        ['ansible-lint',
                         os.path.join(dirpath, filename)],
                        stdin=None)
                    if command == 0:
                        print(CROK + "ok: [localhost] => (item=%s) \n" %
                              os.path.join(dirpath, filename) + CEND)
                    else:
                        print(CRFAIL + "fail: [localhost] => (item=%s) \n" %
                              os.path.join(dirpath, filename) + CEND)
                        sys.exit(1)
    else:
        print("Cannot find ansible-lint")


if __name__ == '__main__':
    main()
