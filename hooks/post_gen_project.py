#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import subprocess
import sys


def main():
    command = subprocess.call(
        ['ansible-galaxy', 'install', '-r', 'roles/requirements.yml'],
        stdin=None,
        stderr=subprocess.PIPE)
    if command != 0:
        sys.exit(1)


if __name__ == '__main__':
    main()
