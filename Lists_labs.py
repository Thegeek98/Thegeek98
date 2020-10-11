
def cmp(ll1, ll2):
    for i in range(len(ll1)):
        if ll1[i] != ll2[i]:
            return 0

    return 1


list = ['physics', 'chemistry', 1997, 2000]
l2 = ['Zin KO', 12.7]

print('element at index -2 is ', list[:2])

for i in range(len(list)):
    print(i, end="-")
    print(list[i])

print(cmp(l2, l2))

if cmp(l2, list):
    print('Same List')
else:
    print('Different List')


