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

def get_special_paths(dir):
  """
  returns a list of the absolute paths of the special files in the given directory
  """
  dir = os.path.abspath(dir)
  # Get list of files in the dir
  filenames = os.listdir(dir)
  #print dir
  #print filenames
  special_filenames = []

  # Loop list and run regular expression matches into new list
  for filename in filenames:
    match = re.search(r'__\w+__', filename)
    if match:
      #print os.path.join(dir, filename) # the problem lies here
      special_filenames.append(os.path.join(dir, filename))

  return special_filenames

def copy_to(paths, dir):
  """
  given a list of paths, copies those files into the given directory
  """
  for path in paths:
    #print path
    shutil.copy(path, dir)

def zip_to(paths, zippath):
  """
  given a list of paths, zip those files up into the given zipfile
  """

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
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  special_paths = []
  for dir in args:
    special_paths += get_special_paths(dir)
    #print special_paths

  #print(special_paths)
  #sys.exit(0)
  copy_to(special_paths, todir)

  if tozip != '':
    #print 'to zip!'
    zip_to(special_paths, tozip)
  
if __name__ == "__main__":
  main()
