#check strict superset

# Enter your code here. Read input from STDIN. Print output to STDOUT

a = set(map(int,input().split()))
n = int(input())
check = True
for i in range(n):
    s = set(map(int,input().split()))
    if(a&s != s) or (s == a):
       check = False
       break
print(check)
