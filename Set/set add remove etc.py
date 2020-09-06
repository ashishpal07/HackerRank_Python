#Set .discard(), .remove() & .pop()

n = int(input())
s = set(map(int, input().split()))
d = {"remove":s.remove,"discard":s.discard,"pop":s.pop}
for i in range(int(input())):
    c = input().split()
    if len(c)>1:
        d[c[0]](int(c[1]))
    else:
        d[c[0]]()
print(sum(s))
