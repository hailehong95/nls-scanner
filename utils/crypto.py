#!/usr/bin/env python

import string
import random


# Ref: https://stackoverflow.com/a/2257449
def secure_string_random(n):
    return ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(n))
