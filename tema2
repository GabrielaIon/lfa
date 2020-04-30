import queue

def verifica_DFA(word):
    global delta, q0
    curentstate = q0
    for x in word:
        if delta[curentstate][index[x]] != -1:
            curentstate = delta[curentstate][index[x]]
        else:
            return False
    if curentstate in F:
        return True
    else:
        return False

def NFAtoDFA():
    global n, S, m, alph, index, q0, k, F, l, delta
    q = queue.Queue()
    q.put(str(q0))
    delta_r = {}
    stari_genenerate = []
    delta = {str(i): delta[i] for i in S}
    while not q.empty():
        st = q.get()
        delta_r[st] = {}
        for litera in alph:
            temp = []
            for stare in str(st):
                temp.extend(delta[stare][litera])
                temp = list(set(temp))
            if len(temp) == 0:
                delta_r[st][litera] = []
            else:
                if temp not in stari_genenerate:
                    stari_genenerate.append(temp)
                    k = ''
                    for stp in temp:
                        k += str(stp)
                    q.put(k)
                delta_r[st][litera] = temp
    for stare in delta_r.keys():
        for litera in alph:
            k = ''
            for st in delta_r[stare][litera]:
                k += str(st)
            delta_r[stare][litera] = k
    F_r = []
    for stare in delta_r.keys():
        for litera in stare:
            if int(litera) in F:
                F_r.append(stare)
    nr = len(delta_r.keys())
    Q_r = [str(i) for i in range(nr)]
    Q_r2 = [str(i) for i in range(nr)]
    stari_inlocuite = {}
    for cheie in delta_r.keys():
        if cheie in Q_r:
            stari_inlocuite[cheie] = int(cheie)
            Q_r.remove(cheie)
    for cheie in delta_r.keys():
        if cheie not in Q_r2:
            stari_inlocuite[cheie] = int(Q_r[0])
            Q_r.pop(0)
    delta = {int(stari_inlocuite[i]): delta_r[i] for i in stari_inlocuite.keys()}
    S = [i for i in range(nr)]
    for stare in S:
        for litera in alph:
            if delta[stare][litera] in stari_inlocuite.keys():
                delta[stare][litera] = stari_inlocuite[delta[stare][litera]]
    F = []
    for stare_f in F_r:
        if stare_f in stari_inlocuite.keys():
            F.append(stari_inlocuite[stare_f])
        else:
            F.append(stare_f)
    F = list(set(F))

def DFAtoMINDFA():
    global n, S, m, alph, index, q0, k, F, l, delta, stari_posibile
    n = len(S)
    matrice = [[True] * i for i in range(n)]
    for stare_fin in S:
        for stare_nef in S:
            if stare_fin in F and stare_nef not in F and stare_fin != stare_nef:

                if stare_fin > stare_nef:
                    matrice[stare_fin][stare_nef] = False
                else:
                    matrice[stare_nef][stare_fin] = False
    for stare in delta.keys():
        for litera in alph:
            if delta[stare][litera] == '':
                delta[stare][litera] = -1
    schimbare = 0
    while schimbare == 0:
        for litera in alph:
            schimbare = 1
            for sf in S:
                for sn in S:
                    if delta[sf][litera] > delta[sn][litera]:
                        if matrice[delta[sf][litera]][delta[sn][litera]] == False:
                            if sf > sn:
                                if matrice[sf][sn] == True:
                                    schimbare = 0
                                matrice[sf][sn] = False
                            else:
                                if matrice[sn][sf] == True:
                                    schimbare = 0
                                matrice[sn][sf] = False
    groups = [{i} for i in range(n)]
    for sf in S:
        for sn in S:
            if sf > sn:
                if matrice[sf][sn] == True:
                    groups[sf] = groups[sf].union(groups[sn])
                    groups[sn] = set()
    groups_r = []
    for st in groups:
        if st:
            groups_r.append(st)
    stari_generate = []
    for gr in groups_r:
        k = ''
        for f in gr:
            k += str(f)
        stari_generate.append(k)
    stari_generate_2 = {i: [stare for stare in stari_generate if str(i) in stare] for i in S}
    delta_r = {stare: {litera: [] for litera in alph} for stare in stari_generate}
    for stare in delta_r.keys():
        for litera in alph:
            for st in stare:
                x = delta[int(st)][litera]
                if x in stari_generate_2.keys():
                    delta_r[stare][litera].extend(stari_generate_2[x])
                    delta_r[stare][litera] = list(set(delta_r[stare][litera]))
    for stare in delta_r.keys():
        for litera in alph:
            if delta_r[stare][litera] != []:
                delta_r[stare][litera] = delta_r[stare][litera][0]
    q0 = stari_generate_2[q0][0]
    F_r = []
    for stare_fin in F:
        F_r.extend(stari_generate_2[stare_fin])
    F = list(set(F_r))
    valori = []
    for stare in delta_r.keys():
        q = queue.Queue()
        q.put(stare)
        vizite = []
        if stare == q0:
            stari_posibile = [q0]
        while not q.empty():
            st = q.get()
            for litera in alph:
                if delta_r[st][litera] != []:
                    stari_posibile.append(delta_r[st][litera])
                    if delta_r[st][litera] not in vizite:
                        q.put(delta_r[st][litera])
                        vizite.append(delta_r[st][litera])
                        if delta_r[st][litera] in F_r:
                            valori.append(stare)
    stari_posibile = set(stari_posibile)
    delta_r1 = delta_r.copy()
    for stare in delta_r.keys():
        if stare not in valori:
            if stare not in F:
                del delta_r1[stare]
    for stare in delta_r1.keys():
        for litera in alph:
            if delta_r1[stare][litera] not in valori:
                if delta_r1[stare][litera] not in F:
                    delta_r1[stare][litera] = []
    delta_r2 = delta_r1.copy()
    for stare in delta_r1.keys():
        if stare not in stari_posibile:
            del delta_r2[stare]
    stari_inlocuite = {}
    x = 0
    for stare in delta_r2.keys():
        stari_inlocuite[stare] = x
        x += 1

    delta = {stari_inlocuite[i]: delta_r2[i] for i in delta_r2.keys()}
    for stare in delta.keys():
        for litera in alph:
            if delta[stare][litera] != []:
                delta[stare][litera] = stari_inlocuite[delta[stare][litera]]
    F_r = []
    for stare in F:
        F_r.append(stari_inlocuite[stare])
    F = F_r
    S = []
    for stare in delta.keys():
        S.append(stare)
    q0 = stari_inlocuite[q0]


#citire
global n, S, m, alph, index, q0, k, F, l, delta
f = open("input.in")
n = int(f.readline())
S = [int(i) for i in range(n)]
m = int(f.readline())
alph = [x for x in f.readline().split()]
index = {}
for q in range(len(alph)):
    index[alph[q]] = q

q0 = int(f.readline())
k = int(f.readline())
F = [int(x) for x in f.readline().split()]
l = int(f.readline())
delta = {i: {x: [] for x in alph} for i in range(n)}

for x in range(l):
    x, st, y = f.readline().split()
    if delta[int(x)][st] == [-1]:
        delta[int(x)][st] = [int(y)]
    else:
        delta[int(x)][st].append((int(y)))

NFAtoDFA()
DFAtoMINDFA()

n = len(S)
print(n)
print(m)
print(alph)
print(q0)
k = len(F)
print(k)
print(F)
l = 0
for stare in delta.keys():
    for litera in alph:
        if delta[stare][litera] != []:
            l += 1
print(l)
for stare in delta.keys():
    for litera in alph:
        if delta[stare][litera] == '':
            delta[stare][litera] = []
for stare in delta.keys():
    for litera in alph:
        if delta[stare][litera] != []:
            print("{} {} {}".format(stare, litera, delta[stare][litera]))


