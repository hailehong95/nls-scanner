#!/usr/bin/env python

import os
import time
import shutil
import logging
import traceback
import subprocess

from scanner.info import info_task
from scanner.setting import TEMP_DIR
from scanner.s3 import bzc_upload_file
from scanner.utils import zip_list_file, data_clean
from scanner.setting import NLS_REPORT, NLS_SCAN_EXE


def nls_scan_on_windows():
    try:
        nls_scan_cmd = [NLS_SCAN_EXE]
        nls_scan_output = subprocess.run(nls_scan_cmd, stdout=subprocess.PIPE)
        time.sleep(2)
    except Exception as e:
        logging.error(traceback.format_exc())


def nls_files_task():
    try:
        nls_scan_on_windows()
        time.sleep(1)
        info_task()
        zip_path = zip_list_file(NLS_REPORT, TEMP_DIR)
        object_name = '/'.join(['report', os.path.basename(zip_path)])
        if bzc_upload_file(zip_path, 'dfir', object_name):
            print('Successful send report')
        else:
            print('Failed to send report. Please contact Administrator/Helpdesk.')
        data_clean([NLS_REPORT, zip_path])
    except Exception as e:
        logging.error(traceback.format_exc())
    return zip_path
