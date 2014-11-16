#!/bin/python

files = ['clean2004.txt', 'clean2005.txt', 'clean2006.txt', 'clean2007.txt', 'clean2008.txt', 'clean2009.txt', 'clean2010.txt', 'clean2011.txt', 'clean2012.txt', 'clean2013.txt']

import csv
import json

# def leadZeros(data, num):
#    return int(((len(data) - num) * "0") + data)

def parseRow(row):
    datum = {}
    datum['StatePPE']    = float(row[2])
    datum['StateRank']   =   int(row[3])
    datum['FederalPPE']  = float(row[4])
    datum['FederalRank'] =   int(row[5])
    datum['LocalPPE']    = float(row[6])
    datum['LocalRank']   =   int(row[7])
    datum['TotalPPE']    = float(row[8])
    datum['TotalRank']   =   int(row[9])
    return datum

def fileToDict(filename):
    f = open(filename, "r")
    f.readline()
    reader = csv.reader(f, delimiter='\t')
    #
    data = []
    for row in reader:
        row = row[0:10]
        if '' in row:
            continue
        data += [row]
    #
    points = {}
    for row in data:
        try:
            points[int(row[0])] = parseRow(row)
        except ValueError:
            pass
    #
    return points

def doAllFiles():
    for filename in files:
        f = open(filename + ".json", "w")
        json.dump(fileToDict(filename), f)
        f.flush()
        f.close()

if __name__ == '__main__':
    doAllFiles()



