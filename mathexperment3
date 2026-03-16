import csv, math
from collections import Counter

r = list(csv.reader(open("play_tennis.csv")))
d, a = r[1:], r[0][:-1]

def e(x):
    c = Counter(i[-1] for i in x)
    return sum(-(v/len(x))*math.log2(v/len(x)) for v in c.values())

def id3(x, a):
    l = [i[-1] for i in x]
    if l.count(l[0]) == len(l): 
        return l[0]
    if not a: 
        return Counter(l).most_common(1)[0][0]
    g = [e(x) - sum(len(s := [i for i in x if i[j] == v]) / len(x) * e(s)
         for v in set(i[j] for i in x)) for j in range(len(a))]
    b = g.index(max(g))
    return {a[b]: {v: id3([i[:b] + i[b+1:] for i in x if i[b] == v], a[:b] + a[b+1:])
                   for v in set(i[b] for i in x)}}

def c(t, a, x):
    return t if isinstance(t, str) else c(t[k := next(iter(t))][x[a.index(k)]], a, x)

# Pretty-print function
def print_tree(tree, indent=""):
    if isinstance(tree, str):
        print(indent + "-> " + tree)
    else:
        root = next(iter(tree))
        print(indent + root)
        for v, subtree in tree[root].items():
            print(indent + f" [{v}]")
            print_tree(subtree, indent + "   ")

t = id3(d, a)
print("Decision Tree:")
print_tree(t)

print("\nPrediction:", c(t, a, ['Sunny','mild','High','Strong']))
