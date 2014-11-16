#!/bin/python

files = ['sat2006.csv', 'sat2007.csv', 'sat2008.csv', 'sat2009.csv', 'sat2010.csv', 'sat2011.csv', 'sat2012.csv', 'sat2013.csv', 'sat2014.csv']

import csv
import json

def parseRow(row):
    datum = {}
    datum['NumTested'] =   int(row[2])
    datum['PerTested'] = float(row[3]) / 100.0
    datum['Math']      =   int(row[4])
    datum['CR']        =   int(row[5])
    datum['Writing']   =   int(row[6])
    datum['M+CR']      =   int(row[7])
    datum['M+CR+W']    =   int(row[8])
    return datum;

def fileToDict(filename):
    f = open(filename, "r")
    reader = csv.reader(f)
    #
    points = {}
    for row in reader:
        try:
            points[int(row[0])] = parseRow(row)
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


