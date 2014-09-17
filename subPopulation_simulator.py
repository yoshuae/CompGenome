

def subPopulation_simulator(n,k):
		w = math.log(k);
		sample= [math.exp(w*random.random()-w) for x in range(n)]
		return(sample)
    
    




