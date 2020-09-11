#!/usr/bin/python

import re
import sys
import fileinput
import json

gtf_file= sys.argv[1]
data = [ ]
genome={}
for each_line_of_text in fileinput.input(gtf_file):
    gene=re.findall(r'^.*?\t.*?\t(gene)\t', each_line_of_text, re.I)
    geneName=re.findall(r'gene_name "(.*?)"', each_line_of_text, re.I)
    chrNumber = re.findall(r'(^.*?)\t', each_line_of_text, re.I)
    startPos = re.findall(r'^.*?\t.*?\t.*?\t(.*?)\t', each_line_of_text, re.I)
    endPos=re.findall(r'^.*?\t.*?\t.*?\t.*?\t(.*?)\t', each_line_of_text, re.I)
  
    if gene:
        one = {"geneName":geneName[0],"chr":chrNumber[0],"startPos":startPos[0],"endPos":endPos[0]}
        data.append(one) 
        js = json.dumps(data)
        print(js)
