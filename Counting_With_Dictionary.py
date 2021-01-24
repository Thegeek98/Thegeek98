counts = dict()
names = ['zinko','zinko','zinko','koko','koko','zinko','ko']

for name in names:
    if name not in counts:
        counts[name] = 1
    else :
        counts[name] += 1
print(counts)