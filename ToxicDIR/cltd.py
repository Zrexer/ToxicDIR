#!/usr/bin/env python3
# *-* coding: utf-8 *-*
"""
Command line script

Created BY: host1let
"""

import os
import sys

fileList = []
folderList = []

def usage():
    return """usage: python3 cltd.py [-h / --help] [-p / --path] #<file name>
windows: python3 cltd.py -p C:\\Users\\sysName
linux: python3 cltd.py -p ../../usr/bin"""

def search_files_and_folders(drive_name):
    os.chdir(drive_name)
    for root, dirs, files in os.walk(".", topdown=False):
        for nameX in files:
            dataFile = (os.path.join(root, nameX))
            fileList.append(dataFile)
        for name in dirs:
            dataFolder = (os.path.join(root, name))
            folderList.append(dataFolder)


if "-h" in sys.argv:
    print(usage())

if "--help" in sys.argv:
    print(usage())

if "-p" in sys.argv:
    path = sys.argv[sys.argv.index('-p')+1]
    search_files_and_folders(path)
    print(f"\nfiles: \n\n\n{fileList}\n\n\nfolders: \n\n\n{folderList}")
    
if "--path" in sys.argv:
    path = sys.argv[sys.argv.index('--path')+1]
    search_files_and_folders(path)
    print(f"\nfiles: \n\n\n{fileList}\n\n\nfolders: \n\n\n{folderList}")
    
if len(sys.argv) <= 1:
    print(usage())