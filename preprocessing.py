import csv, math, random

# Read data
with open("preprocessing.csv") as f:
    h, *d = csv.reader(f)

X = [r[:-1] for r in d]   
y = [1 if r[-1] == "Yes" else 0 for r in d]  


ci, ai, si = [h.index(c) for c in ["Country","Age","Salary"]]


def mean(c):
    v = [float(x) for x in c if x]
    return sum(v) / len(v)

am, sm = mean([r[ai] for r in X]), mean([r[si] for r in X])


for r in X:
    r[ai] = float(r[ai]) if r[ai] else am
    r[si] = float(r[si]) if r[si] else sm


def mode(c):
    return max(set(c), key=c.count)

cm = mode([r[ci] for r in X if r[ci]])
for r in X:
    r[ci] = r[ci] or cm


def scale(v):
    m = sum(v) / len(v)
    s = (sum((x - m) ** 2 for x in v) / len(v)) ** 0.5
    return [(x - m) / s if s else 0 for x in v]

A, S = scale([r[ai] for r in X]), scale([r[si] for r in X])


C = sorted(set(r[ci] for r in X))
c2i = {c: i + 1 for i, c in enumerate(C)}


dataset = [[c2i[r[ci]], round(A[i], 2), round(S[i], 2), y[i]] for i, r in enumerate(X)]


random.seed(42)  
random.shuffle(dataset)

split_ratio = 0.8  
split_index = int(len(dataset) * split_ratio)

train_set = dataset[:split_index]
test_set = dataset[split_index:]

print("\nTrain Set:")
for row in train_set:
    print(row)

print("\nTest Set:")
for row in test_set:
    print(row)
