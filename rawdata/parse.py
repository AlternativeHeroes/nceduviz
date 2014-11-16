#!/bin/python

import csv
import json

files = ['2006-07freereduced.txt', '2007-08freereduced.txt', '2008-09freereduced.txt', '2009-10freereduced.txt', '2010-11freereduced.txt', '2011-12freereduced.txt', '2012-13freereduced.txt']


def betterNumParse(num):
    return int(num.strip().replace(',', ''))

def percentParse(num):
    return float(num.strip().replace('%', '')) / 100.0

def gradeParse(grade):
    return grade.split()

def parseRow(row):
    datum = {}
    datum['SponsorName'] =                row[1]
    datum['SiteName']    =                row[3]
    datum['ADM']         = betterNumParse(row[4])
    datum['ReducedApp']  = betterNumParse(row[5])
    datum['FreeApp']     = betterNumParse(row[6])
    datum['NeedyP']      =   percentParse(row[7])
    datum['GradeLevel']  =     gradeParse(row[8])
    return datum

def fileToDict(filename):
    f = open(filename, 'r')
    f.readline()
    reader = csv.reader(f, delimiter='\t')
    #
    data = []
    for row in reader:
        row = row[0:9]
        if '' in row:
            continue
        data += [row]
    #
    points = {}
    for row in data:
        try:
            points[int(row[0].strip() + row[2].strip())] = parseRow(row)
        except ValueError:
            pass
    #
    return points
    f.close()

def doAllFiles():
    for filename in files:
        f = open(filename + ".json", "w")
        json.dump(fileToDict(filename), f)
        f.flush()
        f.close()


if __name__ == '__main__':
    doAllFiles()

