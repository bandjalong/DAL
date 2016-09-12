#!/bin/python

import sys
import logging
from subprocess import Popen, PIPE, STDOUT
import xml.etree.ElementTree as et

# Globals:
tags = {}
#attribs = set()

def xmlProcessElement(node):
  atts = tags.get(node.tag)
  if atts is None:
    atts = set()
  for att in node.attrib:
    atts.add(att)
  tags[node.tag] = atts
  for child in node:
      xmlProcessElement(child)

def runTest(testNum, casefile):
  print '=== test {} ================== {}'.format(testNum, casefile)
  cmd = 'perl -w kddart_dal_test.pl 1 {}'.format(casefile)
  p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
  output = p.stdout.read()
  print output
    
def handleTest(testNum, casefile):
  # If the case has Parent elements, then pop these on the stack - and remember it's done?
  xmlProcessElement(et.parse(casefile).getroot())
  #runTest(testNum, casefile)
  
def processTestCaseList(cases):
  while len(cases) > 0:
    case = cases.pop()
    handleTest(cases, casefile)

  for tag in tags:
    print '-- {} :'.format(tag)
    for att in tags[tag]:
        print '  ', att
  
def main():
  fname = sys.argv[1]
  cases = []
  with open(fname) as f:
    flines = f.readlines()
    
  # for i, line in enumerate(flines):
  #   line = line.strip()
  #   if len(line) > 1 and line[0] != '#'
  #     cases.append(line)

  # Create stack of cases, using list. Need reverse order as stack starts from the top.
  for i in range(len(flines)-1, -1, -1):
    line = cases[i].strip
    if len(line) > 1 and line[0] != '#'
      cases.append(line)

  processTestCaseList(cases)
  
        
main()

# Todo
# See if all include files have names beginning with case,
# and if they all have top level TestCase element.
