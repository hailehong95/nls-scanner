#!/usr/bin/env python

from utils.crypto import secure_string_random
from utils.setting import PY_LAUNCHER_NAME, EXE_LAUNCHER_NAME
from utils.setting import RELEASE_DIR, PACKER_DIR

import os
import time
import logging
import platform
import traceback
import PyInstaller.__main__


def build_task():
    try:
        print("[TASK] Build NLS Scanner.")
        os_platform = platform.system().lower()
        tiny_aes_key = secure_string_random(16)
        if os_platform == 'windows':
            upx_packer = os.path.join(PACKER_DIR, 'upx_win64')
            PyInstaller.__main__.run(['--clean', '--uac-admin', '--icon', 'NONE', '--onefile', '--name', EXE_LAUNCHER_NAME, '--add-data', 'bin;bin',
                                     '--distpath', RELEASE_DIR, '--upx-dir', upx_packer, '--key', tiny_aes_key, PY_LAUNCHER_NAME])
        else:
            print("[-] Platform does not support!\n")
        time.sleep(0.5)
    except Exception as e:
        logging.error(traceback.format_exc())
