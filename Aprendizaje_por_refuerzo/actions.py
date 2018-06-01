from itertools import combinations, permutations,product
import pandas as pd
import pickle
import sys

def main(args):
	sintomas=pd.read_csv(args[1], delimiter=';')
	l=len(sintomas[sintomas.columns[0]])
	levels=[0,1,2]
	productcartesian=list(product(sintomas[sintomas.columns[0]],levels))
	productcartesian

	g=list(combinations(productcartesian,l))
	solutions=[]

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
	        solutions.append(i)
	names=args[1].split('.')
	name= names[0]
	name=name + '.p'
	pickle.dump(solutions, open( name, "wb" ))


if __name__ == "__main__":
    main(sys.argv)