#Symmetric Difference

# Enter your code here. Read input from STDIN. Print output to STDOUT

m = int(input())
m_set = set(map(int, input().split(" ")))
n = int(input())
n_set = set(map(int, input().split(" ")))
k = sorted(m_set.symmetric_difference(n_set))
for i in k:
    print(i)
