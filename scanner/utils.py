#!/usr/bin/env python

import os
import json
import time
import shutil
import socket
import ctypes
import urllib
import logging
import zipfile
import platform
import requests
import traceback


from scanner.crypto import secure_string_random
from scanner.setting import BASE_DIR, NLS_REPORT


# Ref: https://stackoverflow.com/a/1026626
def is_admin():
    try:
        return os.getuid() == 0
    except AttributeError:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0


# Ref: https://stackoverflow.com/a/28950776
def get_primary_ip_without_internet(host='10.255.255.255', port=1):
    sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sk.connect((host, port))
        primary_ip = sk.getsockname()[0]
    except Exception:
        primary_ip = '127.0.0.1'
    finally:
        sk.close()
    return primary_ip


# Ref: https://stackoverflow.com/a/28950776
def get_primary_ip_with_internet(host='www.google.com', port=80, timeout=5):
    sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sk.settimeout(timeout)
        sk.connect((socket.gethostbyname(host), port))
        primary_ip = sk.getsockname()[0]
    except:
        primary_ip = '127.0.0.1'
    finally:
        sk.close()
    return primary_ip


# Ref: https://stackoverflow.com/a/50558001
def internet_check_by_urllib(url='http://www.google.com/', timeout=5):
    try:
        _ = urllib.request.urlopen(url, timeout=timeout)
        return True
    except:
        pass
    return False


# Ref: https://stackoverflow.com/a/24460981
def internet_check_by_requests(url='http://www.google.com/', timeout=5):
    try:
        _ = requests.head(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        pass
    return False


# Ref: https://stackoverflow.com/a/33117579, https://gist.github.com/7h3rAm/a4c3de8e502f755a7253
def internet_check_by_socket(host="8.8.8.8", port=53, timeout=5):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except:
        pass
    return False


# Ref: https://www.geeksforgeeks.org/python-difference-between-json-dump-and-json-dumps/
def write_dicts_to_json_file(dict_data, file_name):
    try:
        with open(os.path.join(NLS_REPORT, file_name), 'w') as fout:
            json.dump(dict_data, fout, sort_keys=False, indent=4)
    except Exception as e:
        logging.error(traceback.format_exc())


# Ref: https://stackoverflow.com/a/1855118
def zip_list_file(src_dir, dst_dir):
    try:
        if os.path.exists(src_dir):
            os.chdir(src_dir)
        all_files = os.listdir(src_dir)
        zip_name = '-'.join([platform.node(), secure_string_random(6) + '.zip'])
        zip_path = os.path.join(dst_dir, zip_name)
        with zipfile.ZipFile(zip_path, 'w') as zipObj:
            for file_ in all_files:
                zipObj.write(file_)
    except Exception as e:
        logging.error(traceback.format_exc())
    finally:
        os.chdir(BASE_DIR)
    return zip_path


# Ref: https://stackoverflow.com/a/6996628
def data_clean(list_delete):
    try:
        for item in list_delete:
            if os.path.isdir(item):
                shutil.rmtree(item, ignore_errors=True)
                time.sleep(1)
            elif os.path.isfile(item):
                os.remove(item)
                time.sleep(1)
        return True
    except Exception as e:
        logging.error(traceback.format_exc())
    return False
