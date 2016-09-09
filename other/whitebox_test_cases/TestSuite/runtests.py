#!/bin/python

import sys
from subprocess import Popen, PIPE, STDOUT

fname = sys.argv[1]
with open(fname) as f:
    cases = f.readlines()

for i, casefile in enumerate(cases):
  print '=== test {} ================== {}'.format(i, casefile)
  cmd = 'perl -w kddart_dal_test.pl 1 {}'.format(casefile)
  p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
  output = p.stdout.read()
  print output

