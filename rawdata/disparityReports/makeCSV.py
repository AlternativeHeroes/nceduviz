#!/bin/python

import json
import csv

files = ['2006-poor-bydistrict.json', '2006-rich-bydistrict.json', '2007-poor-bydistrict.json', '2007-rich-bydistrict.json', '2008-poor-bydistrict.json', '2008-rich-bydistrict.json', '2009-poor-bydistrict.json', '2009-rich-bydistrict.json', '2010-poor-bydistrict.json', '2010-rich-bydistrict.json', '2011-poor-bydistrict.json', '2011-rich-bydistrict.json', '2012-poor-bydistrict.json', '2012-rich-bydistrict.json']


def jsonToCSV(filename):
    read  = open(filename, 'r')
    write = open(filename[0:filename.rfind('.')] + '.csv', 'w')
    reader = json.load(read)
    reader = reader['Data']
    writer = csv.writer(write)
    for readKey in reader.keys():
        writer.writerow([readKey, reader[readKey]])
    read.close()
    write.flush()
    write.close()

def doAllFiles():
    for filename in files:
        print("Converting file: " + filename)
        jsonToCSV(filename)

if __name__ == '__main__':
    doAllFiles()

