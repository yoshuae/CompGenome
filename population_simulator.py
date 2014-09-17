#function [pop,ratios] = population_simulator(subPopulations,drawFrom,ratios)
def population_simulator(subPopulations,drawFrom,ratios):
	subPopulations=array(subPopulations)
	pop = [0 for x in range(len(subPopulations.T))] 
	for i in range(len(pop)):
		pop[i] = dot(subPopulations[:,i] , ratios);
		
	return ( pop)