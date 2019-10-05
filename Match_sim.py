#Player p and q have variables pgame, pset, pmatch, ptie
import random
ppoints,pgames,psets = 0,0,0
qpoints,qgames,qsets = 0,0,0
server = 0
setnum = 1
matchscore = [0,0,0,0,0,0,0,0,0,0,0,0]
matches_won = 0

def match(p,q,num):
    for matchnum in range(num):
        global matches_won
        def pointp():
            global ppoints,qpoints
            if (random.random()<=p):
                ppoints+= 1
            else:
                qpoints+=1
        def pointq():
            global ppoints,qpoints
            if (random.random()<=q):
                qpoints+= 1
            else:
                ppoints+=1
        for set in range(3):
            global ppoints,qpoints,pgames,qgames,psets,qsets,setnum,matchscore
            for game in range(12):
                global server
                while True:
                    if (server == 0):
                        pointp()
                        if (ppoints>=4 and (ppoints-qpoints)>=2):
                            ppoints,qpoints = 0,0
                            pgames += 1
                            server = 1
                            break
                        elif (qpoints>=4 and (qpoints-ppoints)>=2):
                            ppoints,qpoints = 0,0
                            qgames += 1
                            server = 1
                            break
                    elif (server == 1):
                        pointq()
                        if (ppoints>=4 and (ppoints-qpoints)>=2):
                            ppoints,qpoints = 0,0
                            pgames += 1
                            server = 0
                            break
                        elif (qpoints>=4 and (qpoints-ppoints)>=2):
                            ppoints,qpoints = 0,0
                            qgames += 1
                            server = 0
                            break
            #Check if set was won
                if (pgames>=6 and (pgames-qgames)>=2):
                    matchscore[2*setnum-2] = pgames
                    matchscore[2*setnum-1] = qgames
                    pgames,qgames = 0,0
                    psets+=1
                    setnum += 1
                    break
                elif (qgames>=6 and (qgames-pgames)>=2):
                    matchscore[2*setnum-2] = pgames
                    matchscore[2*setnum-1] = qgames
                    pgames,qgames = 0,0
                    qsets+=1
                    setnum+=1
                    break
                elif (pgames==6 and qgames==6):
                    while True:
                        if ((ppoints+qpoints)%4==0 or (ppoints+qpoints+1)%4==0):
                            pointp()
                        else:
                            pointq()
                        if ((ppoints>=7 and (ppoints-qpoints)>=2)):
                            matchscore[2*setnum+4] = ppoints
                            matchscore[2*setnum+5] = qpoints
                            ppoints,qpoints = 0,0
                            matchscore[2*setnum-2] = pgames
                            matchscore[2*setnum-1] = qgames
                            pgames,qgames = 0,0
                            psets += 1
                            setnum += 1
                            break
                        elif (qpoints>=7 and (qpoints-ppoints)>=2):
                            matchscore[2*setnum+4] = ppoints
                            matchscore[2*setnum+5] = qpoints
                            ppoints,qpoints = 0,0
                            matchscore[2*setnum-2] = pgames
                            matchscore[2*setnum-1] = qgames
                            pgames,qgames = 0,0
                            qsets += 1
                            setnum += 1
                            break
                    break
            if (psets==2):
                ppoints,pgames,psets = 0,0,0
                qpoints,qgames,qsets = 0,0,0
                setnum = 1
                server = 0
                matches_won+=1
                break
            elif (qsets==2):
                ppoints,pgames,psets = 0,0,0
                qpoints,qgames,qsets = 0,0,0
                setnum = 1
                server = 0
                break
        if (num<10):
            print("Matchscore was %i:%i(%i:%i) %i:%i(%i:%i) %i:%i(%i:%i)"
            % (matchscore[0],matchscore[1],matchscore[6],matchscore[7],matchscore[2],matchscore[3],matchscore[8],matchscore[9],matchscore[4],matchscore[5],matchscore[10],matchscore[11]))
            matchscore = [0,0,0,0,0,0,0,0,0,0,0,0]
    print("Player p won %i out of %i matches or %f percent" % (matches_won,num,100.000*matches_won/num))

invalid = True
p = input("Probability p of winning on serve [0,1]:  ")
while (invalid):
    try:
        if (float(p) >= 0 and float(p) <= 1):
            invalid = False
            p = float(p)
    except ValueError:
            p = input("Invalid entry, enter p win probability [0,1]:  ")

invalid = True
q = input("Probability q of winning on serve [0,1]:  ")
while (invalid):
    try:
        if (float(q) >= 0 and float(q) <= 1):
            invalid = False
            q = float(q)
    except ValueError:
            q = input("Invalid entry, enter q win probability [0,1]:  ")

invalid = True
num_matches = input("How many matches to be played:  ")
while (invalid):
    try:
        if (int(num_matches) >= 1):
            invalid = False
            num_matches = int(num_matches)
    except ValueError:
        num_matches = input("Invalid entry, how many matches to be played:  ")


match(p, q, num_matches)
input()
