#!/usr/bin/env python

import os

# Setting Working directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BIN_DIR = os.path.join(BASE_DIR, 'bin')
BUILD_DIR = os.path.join(BASE_DIR, 'build')
PACKER_DIR = os.path.join(BASE_DIR, 'packer')
PACKAGE_DIR = os.path.join(BASE_DIR, 'packages')
RELEASE_DIR = os.path.join(BASE_DIR, 'releases')
PY_LAUNCHER_NAME = 'nls-scanner.py'
EXE_LAUNCHER_NAME = 'nls-scanner'
