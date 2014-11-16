#!/bin/python

import csv

files = ['2006-poor-bydistrict.csv', '2006-rich-bydistrict.csv', '2007-poor-bydistrict.csv', '2007-rich-bydistrict.csv', '2008-poor-bydistrict.csv', '2008-rich-bydistrict.csv', '2009-poor-bydistrict.csv', '2009-rich-bydistrict.csv', '2010-poor-bydistrict.csv', '2010-rich-bydistrict.csv', '2011-poor-bydistrict.csv', '2011-rich-bydistrict.csv', '2012-poor-bydistrict.csv', '2012-rich-bydistrict.csv']


def jsonToCSV(filename):
    read  = open(filename, 'r')
    write = open(filename[0:filename.rfind('.')] + '-fips.csv', 'w')
    reader = csv.reader(read)
    writer = csv.writer(write)
    for row in reader:
        LEA = int(row[0])
        if (LEA % 10 != 0):
            continue
        writer.writerow([int((LEA/10)*2 - 1), row[1]])
    read.close()
    write.flush()
    write.close()

def doAllFiles():
    for filename in files:
        print("Converting file: " + filename)
        jsonToCSV(filename)

if __name__ == '__main__':
    doAllFiles()

