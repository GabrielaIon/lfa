def dfa(cuvant):
    global trans, q0
    curentstate = q0
    for x in cuvant:
        if trans[curentstate][index[x]] != -1:
            curentstate = trans[curentstate][index[x]]
        else:
            return False
    if curentstate in F:
        return True
    else:
        return False


f = open("lnfa.in")
n = int(f.readline())
m = int(f.readline())
alph = [x for x in f.readline().split()]
index = {}
for i in range(len(alph)):
    index[alph[i]] = i
print(index)
q0 = int(f.readline())
k = int(f.readline())
F = [int(x) for x in f.readline().split()]
l = int(f.readline())

trans = [[-1] * m for i in range(m)]

for x in range(l):
    x, st, y = f.readline().split()
    trans[int(x)][index[st]] = int(y)

x = int(f.readline())
for word in f:
    sol = []
    dfa(word.strip())
    if dfa(word.strip()):
        print(True)
    else:
        print(False)
