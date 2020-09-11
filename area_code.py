#!/usr/bin/python
import re
import sys
import fileinput

listofNumbers = sys.argv[1]
phone = {}
for each_number in fileinput.input(listofNumbers):
    num = re.sub(r'\D', "", each_number)
    acode = re.match(r'^(\d{3})', num)
    print (acode.group(0))