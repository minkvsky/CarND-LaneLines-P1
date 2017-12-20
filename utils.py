# not in use
def getnewlines(lines, std_line=10,ymax=540,xmax =960):
    newlines = list(lines)
    for line in lines:
        line = line[0]
        if metric(line) > std_line:
            if line[1] != line[3]:
                x = (line[0] - line[2])*(ymax - line[1]) /(line[1] - line[3]) + line[0]
                if x >= 0 and x <= xmax:
                    newlines.append(np.array([[line[0], line[1], int(x), ymax]]))
    return(newlines)
    
def tonewlines(lines):
    htable = {}
    for line in lines:
        htable[tuple(line[0])] = rateV(line[0])

    hhtable = {}
    for t in htable:
        if htable[t] not in hhtable:
            hhtable[htable[t]] = []
        hhtable[htable[t]].append((t[0],t[1]))
        hhtable[htable[t]].append((t[2],t[3]))        

    newlines = []
    for key in hhtable:
        linegroup = hhtable[key]
        newline = np.array([max(linegroup, key=lambda x:x[0]),
             min(linegroup, key=lambda x:x[0])]).reshape(-1,)
        newlines.append([newline])
    newlines = np.array(newlines)

    return(newlines)
# weighting
def rateV(line):
    rate = (line[0] - line[2]) / float(line[1] - line[3])
    return round(rate, 4)
    
def twoweightedlines(lines):
    htableplus = {}
    htableminus = {}
    for line in lines:
        line = line[0]
        if krate(line) > 0:
            htableplus[tuple(line)] = [rateV(line), metric(line)]
        if krate(line) < 0:
            htableminus[tuple(line)] = [rateV(line), metric(line)]
    newlines = []
    lineplus = minweigteddiff(htableplus)
    lineminus = minweigteddiff(htableminus)
    return(lineplus, lineminus)

def minweigteddiff(htableplus):
    # the line which is most close to the average
    averageweitght = np.average([htableplus[x][0] for x in htableplus],
                               weights=[htableplus[x][1] for x in htableplus])
    return(min(htableplus, key=lambda x: abs(htableplus[x][0] - averageweitght)))

def twoaveragelines(lines):
    htableplus = {}
    htableminus = {}
    for line in lines:
        line = line[0]
        if krate(line) > 0:
            htableplus[tuple(line)] = rateV(line)
        if krate(line) < 0:
            htableminus[tuple(line)] = rateV(line)
    newlines = []
    lineplus = mindiff(htableplus)
    lineminus = mindiff(htableminus)
    return(lineplus, lineminus)

def mindiff(htableplus):
    # the line which is most close to the average
    return(min(htableplus, key=lambda x: abs(htableplus[x] - np.mean(list(htableplus.values())))))
