def mymin(x,y):
    if(x<=y):
        return x
    else:
        return y

def Least_moves(x):
    dp=[0]*(x+1)
    dp[1]=0
    for i in range(2,x+1):
        if(i%2==0):
            dp[i]=mymin(dp[i-1],dp[int(i/2)])+1
        else:
            dp[i]=dp[i-1]+1
    return dp[x]

if __name__ == '__main__':
    x=int(input())
    ret=Least_moves(x)
    print(ret)
