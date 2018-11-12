#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
import re
import sys


def main():

    MODULE_REGEX = r'^[-_a-zA-Z][-_a-zA-Z0-9]+$'

    repo_name = '{{ cookiecutter.repo_name }}'
    sdk_role = '{{ cookiecutter.sdk_role }}'

    if not re.match(MODULE_REGEX, repo_name):
        print('ERROR: %s is not a valid Ansible Repository Name!' % repo_name)
        sys.exit(1)

    if not re.match(MODULE_REGEX, sdk_role):
        print('ERROR: %s is not a valid Ansible Role Name!' % sdk_role)
        sys.exit(1)


if __name__ == '__main__':
    main()
