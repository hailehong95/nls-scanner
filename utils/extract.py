#!/usr/bin/env python

from utils.setting import BIN_DIR, PACKAGE_DIR
from utils.utils import unzip_file

import os
import time
import shutil
import logging
import platform
import traceback


# Extract Task: unzip/copy binaries dependencies to 'bin' directory.
def extract_task():
    try:
        print("[TASK] Extracting NLS Scanner.")
        if not os.path.isdir(BIN_DIR):
            os.mkdir(BIN_DIR)
        os_platform = platform.system().lower()
        if os_platform == "windows":
            print("[+] Platform is: {}".format("Windows"))
            print("[+] Copy NLSScan file: " + 'NLSScan.exe')
            shutil.copyfile(os.path.join(PACKAGE_DIR, 'NLSScan.exe'), os.path.join(BIN_DIR, 'NLSScan.exe'))
            time.sleep(0.5)
            print("[+] Done!\n")
    except Exception as e:
        logging.error(traceback.format_exc())
