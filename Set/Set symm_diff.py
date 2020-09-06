#Set .symmetric_difference operation

n1 = int(input())
set_n1 = set(map(int, input().split(" ")))
n2 = int(input())
set_n2 = set(map(int, input().split(" ")))
print(len(set_n1.symmetric_difference(set_n2)))
