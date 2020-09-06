#Set Mutations

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
s1 = set(map(int,input().split()))
k = int(input())
for i in range(k):
    c = input().split()
    op = c[0]
    s2 = set(map(int,input().split()))
    # conditions
    if op == 'update':
        s1.update(s2)
    elif op == 'intersection_update':
        s1.intersection_update(s2)
    elif op == 'difference_update':
        s1.difference_update(s2)
    elif op == 'symmetric_difference_update':
        s1.symmetric_difference_update(s2)

print(sum(s1))
