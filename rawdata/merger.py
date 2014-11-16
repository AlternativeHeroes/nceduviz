#!/bin/python

import json

# Intersecrion of All the Years:
allFiles = {}

filesFreeRed = ['2006-07freereduced.txt', '2007-08freereduced.txt', '2008-09freereduced.txt', '2009-10freereduced.txt', '2010-11freereduced.txt', '2011-12freereduced.txt', '2012-13freereduced.txt']

filesPPE = ['clean2006.txt', 'clean2007.txt', 'clean2008.txt', 'clean2009.txt', 'clean2010.txt', 'clean2011.txt', 'clean2012.txt']

filesSAT = ['sat2006.csv', 'sat2007.csv', 'sat2008.csv', 'sat2009.csv', 'sat2010.csv', 'sat2011.csv', 'sat2012.csv']

allFiles['FreeReducedLunchBySchool'] = filesFreeRed
allFiles['PPEbyCounty']              = filesPPE
allFiles['SATbySchool']              = filesSAT

for i in range(0, 7):
    freeRed = open('FreeReducedLunchBySchool/' + filesFreeRed[i] + '.json', 'r')
    fPPE    = open('PPEbyCounty/' + filesPPE[i] + '.json', 'r')
    fSAT    = open('SATbySchool/' + filesSAT[i] + '.json', 'r')
    final   = open("aggregate-" + str(2006 + i) + ".json", "w")
    #
    FnR = json.load(freeRed)
    PPE = json.load(fPPE)
    SAT = json.load(fSAT)
    #
    print("Parsing Year: " + str(2006 + i))
    points = {}
    for school in SAT.keys():
        try:
            points[school] = {"SAT": SAT[school],
                              "FnR": FnR[school],
                              "PPE": PPE[school[:-3]]}
        except KeyError:
            continue
    #
    freeRed.close()
    fPPE.close()
    fSAT.close()
    #
    json.dump(points, final)
    final.flush()
    final.close()



