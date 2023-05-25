def prim(n):
    for i in range(2,n):
        if(n%2 == 0):
            return False
s = int(input('Start:'))
e = int(input ('End :')) 
prime=[]
for m in range(s,e+1):
    if(prim(m) != False): 
        prime.append(m)  
print(prime)   
