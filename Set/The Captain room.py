#The Cptain's Room

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
s = list(map(int,input().split()))
a = set()
b = set()
for i in s:
    if i not in a:
        a.add(i)
        b.add(i)
    else:
        b.discard(i)
b = list(b)
print(b[0])
