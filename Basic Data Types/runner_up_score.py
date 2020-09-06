#Find the rubnner-up score

n = int(input())
l = list(map(int,input().split()))
print(sorted(set(list(l)))[-2])
