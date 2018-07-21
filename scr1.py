import csv
def data_year(year):
    with open('./data/WorldCupMatches.csv') as wcm:
        readCSV = csv.reader(wcm,delimiter=',')
        match=[]
        stage=[]
        for row in readCSV:
            if row[0]==year:
                match.append(row)
                if row[2] not in stage:
                    stage.append(row[2])

        group=[[] for i in range(0,len(stage))]
        for i in range(0,len(match)):
            group[stage.index(match[i][2])].append(match[i])
        si=0
        for i in group:
            print(stage[si])
            si+=1
            for j in i:
                result=""
                if int(j[6])==int(j[7]):result="Draw"
                elif int(j[6])>int(j[7]):result=j[5]+" won"
                elif int(j[6])<int(j[7]):result=j[8]+" won"
                print(j[5]+" vs "+j[8]+": "+result)

def data_vs(team1,team2):
    print(team1+" VS "+team2)
    team1i=""
    team2i=""
    vs=[]
    with open('./data/WorldCupMatches.csv') as wcm:
        readCSV = csv.reader(wcm,delimiter=',')
        for row in readCSV:
            if (row[5]==team1 and row[8]==team2) or (row[5]==team2 and row[8]==team1):
                    vs.append(row)

    if vs[0].index(team1)==5:
        team1i=vs[0][18]
        team2i=vs[0][19]
    else:
        team1i=vs[0][19]
        team2i=vs[0][18]
    for i in vs:
        print("For detail enter: "+str(vs.index(i)))
        result=""
        if int(i[6])==int(i[7]):result="Draw "
        elif int(i[6])>int(i[7]):result=i[5]+" won "
        elif int(i[6])<int(i[7]):result=i[8]+" won "
        print("Fifa "+i[0]+": "+"Date:"+i[1]+" "+i[2]+" Stadium: "+i[3]+","+i[4]+result+i[6]+"-"+i[7])

    md=input("For details of match enter no. else enter N:")
    if md != 'N':
        team1p = []
        team2p = []
        matchid=vs[int(md)][17]
        roundid=vs[int(md)][16]
        with open('./data/WorldCupPlayers.csv') as wcp:
            readCSV2=csv.reader(wcp,delimiter=',')
            for row in readCSV2:
                if roundid==row[0] and matchid==row[1]:
                    if row[2]==team1i:
                        team1p.append(row)
                    else:
                        team2p.append(row)
            print(team1+"("+team1i+") coach: "+team1p[0][3])
            for i in team1p:
                if i[4] =='N':
                    print(i[6]+" "+i[7]+"(substitute)")
                else:
                    print(i[6]+" "+i[7])
            print("Goal by "+team1+":")
            for i in team1p:
                if i[8] !='':
                    g=i[8].split(' ')
                    for k in g:
                        if k[0]=='G':
                            print(i[6]+" "+i[8])
            
            print("\n"+team2+"("+team2i+") coach: "+team2p[0][3])
            for i in team2p:
                if i[4] =='N':
                    print(i[6]+" "+i[7]+"(substitute)")
                else:
                    print(i[6]+" "+i[7])
            print("Goal by "+team2+":")
            for i in team2p:
                if i[8] !='':
                    g=i[8].split(' ')
                    for k in g:
                        if k[0]=='G':
                            print(i[6]+" "+i[8])

def data_team(team):
    with open('./data/WorldCupMatches.csv') as wcm:
        readCSV = csv.reader(wcm,delimiter=',')
        matchs=[]
        for i in readCSV:
            if i[5]==team or i[8]==team:
                matchs.append(i)

        won=0
        draw=0
        loss=0
        for j in matchs:
            if int(j[6])==int(j[7]):result="Draw"
            elif int(j[6])>int(j[7]):result=j[5]
            elif int(j[6])<int(j[7]):result=j[8]
            if result==team:won+=1
            elif result=="Draw":draw+=1
            else :loss+=1
            print("Fifa "+j[0]+": "+"Date:"+j[1]+" "+j[5]+" VS "+j[8]+" "+j[2]+" Stadium: "+j[3]+","+j[4]+" result: "+result+" "+j[6]+"-"+j[7])
        print("Toal matches played:"+str(won+draw+loss)+", won:"+str(won)+", draw:"+str(draw)+", loss:"+str(loss))

def data_player(player):
    with open("./data/WorldCupPlayers.csv") as wcp:
        readCSV = csv.reader(wcp,delimiter=',')
        goal=[]
        for i in readCSV:
            if i[6]==player and i[8] !='':
                goal.append(i)
        #print(goal)
        with open("./data/WorldCupMatches.csv") as wcm:
            readCSV2 = csv.reader(wcm,delimiter=',')
            go=0
            og=0
            m=0
            for i in readCSV2:
                for j in goal:
                    if j[0]==i[16] and j[1]==i[17]:
                        m+=1
                        g=j[8].split(" ")
                        for k in g :
                            if k[0]=='O' and k[1]=='G':
                                og+=1
                                if int(i[6])==int(i[7]):result="Draw "
                                elif int(i[6])>int(i[7]):result=i[5]+" won "
                                elif int(i[6])<int(i[7]):result=i[8]+" won "
                                print("Fifa "+i[0]+": "+"Date:"+i[1]+" "+i[5]+" VS "+i[8]+" "+i[2]+" Stadium: "+i[3]+","+i[4]+" result: "+result+" "+i[6]+"-"+i[7])
                                print("own goal")
                            elif k[0]=='G':
                                go+=1
                                if int(i[6])==int(i[7]):result="Draw "
                                elif int(i[6])>int(i[7]):result=i[5]+" won "
                                elif int(i[6])<int(i[7]):result=i[8]+" won "
                                print("Fifa "+i[0]+": "+"Date:"+i[1]+" "+i[5]+" VS "+i[8]+" "+i[2]+" Stadium: "+i[3]+","+i[4]+" result: "+result+" "+i[6]+"-"+i[7])
                                print("goal "+k)

    print("Matches played: "+str(m)+" Goal: "+str(go)+" Own goal :"+str(og))            

def data_team_year(team,year):
    with open("./data/WorldCupMatches.csv") as wcm:
        readCSV = csv.reader(wcm,delimiter=',')
        match=[]
        teami=""
        for i in readCSV:
            if i[0]==year and (i[5]==team or i[8]==team):
                match.append(i)
        if team==match[0][5]:
            teami=match[0][18]
        else :
            teami=match[0][19]
    players=[]
    cap=[]
    gk=[]
    with open("./data/WorldCupPlayers.csv") as wcp:
        readCSV = csv.reader(wcp,delimiter=',')
        for i in readCSV:
            for j in match:
                if i[0]==j[16] and i[1]==j[17] and i[2]==teami:
                    if i[6] not in players:
                        players.append(i[6])
                        if i[7] =='C':
                            cap.append(i[6])
                        if i[7]=="GK":
                            gk.append(i[6])
    print("The Squard for "+team+" in FIFA "+ year+":")
    for i in players:
        p=""
        if i in cap:
            p="(C)"
        elif i in gk:
            p="(GK)"
        print(i+p)




while True:
    d=input("Year data:1\nVS data:2\nTeam data:3\nPlayer data:4\nSquard members:5\n")
    print(d)
    if d=="1" :
        year = input("Enter the year for which you want informtion: ")
        data_year(year)
    elif d=="2":
        team1 = input("Enter the name of teams whose match history you want to know: ")
        team2 = input("VS ")       
        data_vs(team1,team2)
    elif d=="3":
        team = input("Enter team name: ")
        data_team(team)
    elif d=="4":
        player=input("Enter the name of player: ")
        data_player(player)
    elif d=="5":
        team = input("Enter team name: ")
        year = input("Enter the year: ")
        data_team_year(team,year)
    else :
        break
