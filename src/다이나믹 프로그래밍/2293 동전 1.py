import sys


n,k=map(int,sys.stdin.readline().split())
arr=[int(sys.stdin.readline()) for i in range(n)]

dp=[0 for i in range(k+1)]

dp[0]=1

for i in arr:
    for j in range(1,k+1):
        if j>=i:
            dp[j]+=dp[j-i]

print(dp[k])