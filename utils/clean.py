#!/usr/bin/env python

from utils.setting import BIN_DIR, RELEASE_DIR, BUILD_DIR

import os
import time
import shutil
import logging
import traceback


# Clean Task: Remove all binaries dependencies in 'bin' directory.
def clean_task():
    try:
        print("[TASK] Clean temporary working files.")
        dirs_delete = [BIN_DIR, RELEASE_DIR, BUILD_DIR, '__pycache__']
        for dir_ in dirs_delete:
            if os.path.isdir(dir_):
                shutil.rmtree(dir_, ignore_errors=True)
                time.sleep(1)
        print("[+] Clean done!\n")
    except Exception as e:
        logging.error(traceback.format_exc())
