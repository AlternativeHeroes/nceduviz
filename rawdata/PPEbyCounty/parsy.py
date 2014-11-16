for year in range(2004, 2014):

    i = open('Ranking_no_CN' + str(year) + '.txt', 'r')
    o = open('clean' + str(year) + '.txt', 'a')

    titles = i.readline().split('\t')
    # ignoring the first column
    numCol = len(titles) - 1

    o.write('\t'.join(titles[1:]))

    for line in i:
        entry = line.split('\t')[1:]
        if (len(entry) != numCol):
            print 'panic!!!'

        fail = False
        for x in range(0, numCol-1):
            if len(entry[x]) == 0:
                fail = True
                break
            if x >= 0:
                entry[x] = entry[x].replace(',','').replace('\"','')
                entry[numCol-1] = entry[numCol-1].replace('\r\n', '')

        if fail:
            # print 'panic\t' + str(entry)
            continue

        o.write("\t".join(entry) + '\n')

    i.close()
    o.close()
# with open('Ranking_no_CN2004.txt', 'r') as i:
#     print(i.readline().split('\t'))
