#!/usr/bin/env python

import sys
from scanner.nlsfile import nls_files_task
from scanner.utils import is_admin, internet_check_by_requests


def main():
    # Check Administrator
    if not is_admin():
        print('Require run as Administrator.')
        sys.exit(1)

    # Check internet connection
    if not internet_check_by_requests():
        print('Please check your internet connection.')
        sys.exit(2)

    # Start Scanning
    zip_report = nls_files_task()


if __name__ == '__main__':
    main()
