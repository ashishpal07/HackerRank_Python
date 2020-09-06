#Lists

n = int(input())
l = []
for row in range(n):
    s = input().split()
    if len(s) == 1:
        op = s[0]
    if len(s) == 2:
        op = s[0]
        e = int(s[1])
    if len(s) == 3:
        op = s[0]
        i = int(s[1])
        e = int(s[2])     
    if op == 'insert':
        l.insert(i,e)
    elif op == 'print':
        print(l)
    elif op == 'remove':
        l.remove(e)
    elif op == 'append':
        l.append(e)
    elif op == 'sort':
        l.sort()
    elif op == 'pop':
        if len(l) != 0:
            l.pop()
    elif op == 'reverse':
        l.reverse()
