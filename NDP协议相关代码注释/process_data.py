#!/usr/bin/env python
#!python

from __future__ import print_function
import subprocess
import sys
#获取命令行参数，赋值给filename
filename = sys.argv[1]
#执行外部命令程序parse_output
subprocess.call("../../parse_output " + filename + " -ascii > " + filename+".asc", shell=True)
#打开filename.asc并赋于ifile
ifile = open(filename+".asc", "r")
#建立数组rates
rates = []
#逐行遍历ifile,将数据存入rates
for line in ifile:
    data = line.split()#字符串分割赋予data
    time = float(data[0])
    ev = data[2];
    if time == 0.2 and ev == "NDP_SINK":
        if data[9] == "Rate":
            rate = int(data[10])
            rate = rate * 8 /1000000000.0;
            rates.append(rate)
            print(rate)
ifile.close()

ofile = open(filename+".urates", "w+")
for r in rates:
    print(r, file=ofile);
ofile.close()
#排序
rates.sort()
print(rates)
ofile = open(filename+".rates", "w+")
for r in rates:
    print(r, file=ofile);
ofile.close()
    
