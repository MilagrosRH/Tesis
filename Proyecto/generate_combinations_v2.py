from itertools import combinations, permutations,product
import pandas as pd
import pickle
import sys

def main(args):
	data=pd.read_csv(args[1], delimiter=';')
	l=len(data[data.columns[0]])
	levels=[0,1,2]
	alimentos=[]
	for i in data[data.columns[0]]:
		alimento=[]
		for n in levels:
			alimento.append((i,n))
		alimentos.append(alimento)
		
	productcartesian=product(*alimentos)

	solutions=[]

	for i in productcartesian:
	    solutions.append(i)
		
	names=args[1].split('.')
	name= names[0]
	name=name + '.p'
	pickle.dump(solutions, open( name, "wb" ))


if __name__ == "__main__":
    main(sys.argv)