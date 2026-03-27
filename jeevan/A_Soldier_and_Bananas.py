k,n,w = map(int,input().split())
x = k*(w*(w+1)/2)
print(int(abs(min(n-x,0))))
