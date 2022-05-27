#!/usr/bin/env python

import string
import random


def secure_string_random(n):
    return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(n))
