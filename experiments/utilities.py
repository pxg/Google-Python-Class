#!/usr/bin/python

import os
import commands
import urllib

## Version that uses try/except to print an error message if the
## urlopen() fails.
def wget2(url):
  try:
    ufile = urllib.urlopen(url)
    if ufile.info().gettype() == 'text/html':
      print ufile.read()
  except IOError:
    print 'problem reading url:', url

## Given a dir path, run an external 'ls -l' on it --
## shows how to call an external program
def listdir(dir):
  cmd = 'ls -l ' + dir
  print "Command to run:", cmd   ## good to debug cmd before actually running it
  (status, output) = commands.getstatusoutput(cmd)
  if status:    ## Error case, print the command's output to stderr and exit
    sys.stderr.write(output)
    sys.exit(1)
  print output  ## Otherwise do something with the command's output

def os_experiments():
  #print 'pete test'
  help(os.listdir)

def main():
  #os_experiments()
  #listdir('~/')
  wget2('http://petegraham.co.uk/')

if __name__ == '__main__':
  main()