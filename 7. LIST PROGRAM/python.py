def factor(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factor(n-1)

n=[2, 4, 8, 7, 5]
nn =[]
for i in n:
    k =(factor(i))
    nn.append(k)
print(nn)
