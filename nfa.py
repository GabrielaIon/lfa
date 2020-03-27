def ENFA(automata, word):
    if len(word) != 0:
        if trans[automata]['$'] != [-1]:
            for stare in trans[automata]['$']:
                ENFA(stare, word)
        if trans[automata][word[0]] == [-1]:
            sol.append(False)
        else:
            automata = trans[automata][word[0]]
            for stare in automata:
                ENFA(stare, word[1:])
    else:
        if automata in F:
            sol.append(True)
        else:
            sol.append(False)

f = open("date.in")
n = int(f.readline())
m = int(f.readline())
alph = [x for x in f.readline().split()]
alph.append('$')
q0 = int(f.readline())
k = int(f.readline())
F = [int (x) for x in f.readline().split()]
l = int(f.readline())

trans = [ {x: [-1] for x in alph} for i in range(n)]

for x in range(l):
    x, st, y = f.readline().split()
    if trans[int(x)][st] == [-1]:
        trans[int(x)][st] = [int(y)]
    else:
        trans[int(x)][st].append((int(y)))
#print(trans)

x = int(f.readline())
for word in f:
    sol = []
    automata = q0
    ENFA(automata, word.strip())
    if True in sol:
        print("TRUE")
    else:
        print("FALS")
