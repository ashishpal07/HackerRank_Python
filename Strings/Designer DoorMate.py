#Designer Door Mate

# Enter your code here. Read input from STDIN. Print output to STDOUT
N,M = map(int,input().split()) # inputs

for i in range(1,N,2):         # for upper traingle
    print((i*'.|.').center(M,'-'))

print('WELCOME'.center(M,'-'))  # for middle WELCOME

for i in range(N-2,-1,-2):     # for lower traingle
    print((i*'.|.').center(M,'-'))
