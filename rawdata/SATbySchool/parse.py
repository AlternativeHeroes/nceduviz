#!/bin/python

files = ['sat2006.csv', 'sat2007.csv', 'sat2008.csv', 'sat2009.csv', 'sat2010.csv', 'sat2011.csv', 'sat2012.csv', 'sat2013.csv', 'sat2014.csv']

import csv
import json

def parseRow(row):
    datum = {}
    datum['NumTested'] =   int(row[3])
    datum['PerTested'] = float(row[4]) / 100.0
    datum['Math']      =   int(row[5])
    datum['CR']        =   int(row[6])
    datum['Writing']   =   int(row[7])
    datum['M+CR']      =   int(row[8])
    datum['M+CR+W']    =   int(row[9])
    return datum;

def fileToDict(filename):
    f = open(filename, "r")
    reader = csv.reader(f)
    #
    points = {}
    district = ""
    for row in reader:
        if (row[1] == row[0]):
            district = row[0]
        try:
            points[int(district + row[1])] = parseRow(row)
        except (ValueError, IndexError) as e:
            pass
    f.close()
    return points

def doAllFiles():
    for filename in files:
        f = open(filename + ".json", "w")
        json.dump(fileToDict(filename), f)
        f.flush()
        f.close()

if __name__ == '__main__':
    doAllFiles()


