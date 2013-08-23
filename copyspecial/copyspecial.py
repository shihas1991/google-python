#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""
def copy(fromdir,todir):
  filenames = os.listdir(os.path.abspath(fromdir))
  print filenames
  for filename in filenames:
    shutil.copy(os.path.abspath(os.path.join(fromdir,filename)),os.path.abspath(todir))
def ziip(tozip):
  filenames = os.listdir(os.path.abspath(tozip))
  cmd='zip -j zipfile '
  for filename in filenames:
    cmd=cmd+filename+' '
  print 'Command to run:',cmd
  filenames = os.listdir(os.path.abspath(tozip))
  for filename in filenames:
    print os.path.abspath(filename)
  output = commands.getoutput(cmd)

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  fromdir=''
 

 

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]
    ziip(tozip)
  elif args[0] == '--todir':
    fromdir=args[1]
    todir=args[2]
    del args[0:3]
    copy(fromdir,todir)
  ziip(tozip)
if __name__ == "__main__":
  main()
