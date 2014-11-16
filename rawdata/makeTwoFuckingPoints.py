#!/bin/python

import json

parent = 'aggregate'

files = ['aggregate-2006.json', 'aggregate-2007.json', 'aggregate-2008.json', 'aggregate-2009.json', 'aggregate-2010.json', 'aggregate-2011.json', 'aggregate-2012.json']


def collapseIntoDistricts(schoolJson):
    dists = {}
    for school in schoolJson.keys():
        if school[:-3] in dists.keys():
            dists[school[:-3]] += [schoolJson[school]]
        else:
            dists[school[:-3]]  = [schoolJson[school]]
    return dists

def parseIntoThrees(data):
    # District IDs to three points
    collapsed = collapseIntoDistricts(data)
    maxSATPPE = 0.0
    minSATPPE = 240000.0
    poorMetrics = {}
    richMetrics = {}
    for district in collapsed.keys():
        poorNum = 0
        richNum = 0
        poorSum = 0.0
        richSum = 0.0
        for datum in collapsed[district]:
            ratio = datum['SAT']['M+CR'] / (datum['PPE']['TotalPPE'] + 0.)
            if (ratio < minSATPPE):
                minSATPPE = ratio
            if (ratio > maxSATPPE):
                maxSATPPE = ratio
            if datum['FnR']['NeedyP'] > 0.4:
                poorSum += ratio
                poorNum += 1
            else:
                richSum += ratio
                richNum += 1
        if poorNum != 0:
            poorMetrics[district] = poorSum / poorNum;
        if richNum != 0:
            richMetrics[district] = richSum / richNum;
    return {'Rich': richMetrics, 'Poor': poorMetrics, 'Range': [minSATPPE, maxSATPPE]}

def doOneFile(filename, year):
    f = open(filename, 'r')
    outPoor = open(str(year) + '-poor-bydistrict', 'w')
    outRich = open(str(year) + '-rich-bydistrict', 'w')
    yearly = json.load(f)
    metrics = parseIntoThrees(yearly)
    json.dump({'Data': metrics['Rich'], 'Range': metrics['Range']}, outRich)
    json.dump({'Data': metrics['Poor'], 'Range': metrics['Range']}, outPoor)
    f.close()
    outPoor.flush()
    outRich.flush()
    outPoor.close()
    outRich.close()

def parseAllFiles():
    for i in range(0, 7):
        print("Parsing year: " + str(2006 + i))
        doOneFile(parent + '/' + files[i], 2006 + i)

if __name__ == '__main__':
    parseAllFiles()

