#!/usr/bin/env python3
# *-* coding: utf-8 *-*
"""
Simple script

Created BY: host1let
"""

import os

fileList = []
folderList = []

def search_files_and_folders(drive_name):
    os.chdir(drive_name)
    for root, dirs, files in os.walk(".", topdown=False):
        for nameX in files:
            dataFile = (os.path.join(root, nameX))
            fileList.append(dataFile)
        for name in dirs:
            dataFolder = (os.path.join(root, name))
            folderList.append(dataFolder)

path = str(input('Enter your path: '))
search_files_and_folders(path)
print(f"\nfiles: \n\n\n{fileList}\n\n\nfolders: \n\n\n{folderList}")