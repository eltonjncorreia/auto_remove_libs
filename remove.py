#!/usr/bin/bash

import sys
import subprocess


f = sys.argv[1]


def remove_lib(f):
    with open(f) as text_file:
        for text in text_file.readlines():
            subprocess.call("pip uninstall -y "+text, shell=True)


if __name__ == '__main__':
    remove_lib(f)
