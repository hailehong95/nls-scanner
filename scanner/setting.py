#!/usr/bin/env python

import os


# Global config
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BIN_DIR = os.path.join(BASE_DIR, 'bin')
DATA_DIR = os.path.join(BASE_DIR, 'data')
TEST_DIR = os.path.join(BASE_DIR, 'tests')
TEMP_DIR = os.getenv('Temp')
NLS_REPORT = os.path.join(TEMP_DIR, 'NLSScan')
NLS_SCAN_EXE = os.path.join(BIN_DIR, 'NLSScan.exe')
CWD_DIR = os.getcwd()
# Please change Base url (s3)
BASE_URL = 'https://s3.example.test'
