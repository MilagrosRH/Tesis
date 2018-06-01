

from itertools import combinations, permutations,product, dropwhile
x=['a','b','c','d']
y=[1,2,3]
z= list(product(x,y))

g=list(combinations(z,4))
#print g
sol=[]

for i in g:
    nova =False
    for n in i:
        c,p=n
        for k in  [(m,n) for (m,n) in i if (m,n)!=(c,p)]:
            ci,pi=k
            if (c==ci):
                nova=True
                break
    if nova==False:
       sol.append(i)

print sol
print len(sol)


h= [('a', 1), ('b', 1), ('c', 1), ('d', 1)]
soluciones=[]
soluciones.append(h)
for j in h:
    c,p=j
    s= [(m,n) for (m,n) in h if (m,n)!=(c,p)]    
    for a in range(2):
        d=s[:]
        d.append((c,p+a+1))

        soluciones.append(d)
    
#print soluciones