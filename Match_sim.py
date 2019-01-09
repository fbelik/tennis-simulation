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

match(0.5,0.5,1)
i = input()
