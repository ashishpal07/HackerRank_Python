#check subset

# Enter your code here. Read input from STDIN. Print output to STDOUT

for i in range(int(input())):
    n1 = int(input())
    a = set(map(int,input().split()))
    n2 = int(input())
    b = set(map(int,input().split()))
    print(a.issubset(b))
