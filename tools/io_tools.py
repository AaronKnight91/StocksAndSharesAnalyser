import os

def check_directory(path):
    if not os.isdir(path):
        os.mkdir(path)
