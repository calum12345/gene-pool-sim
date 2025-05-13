import random
from fish import Fish

def genNewPool(length: int) -> list[str]:
    """
    create new gene pool with specified length
    """
    genePool = [random.choice(["g","r","y"]) for i in range(length)]
    return genePool


def genPopulation(pool: list[str]) -> list:
    """
    create new population based on gene pool

    will probably break if you input a genepool with an odd number of alleles so dont do that please :)
    """
    population = []
    for i in range(0,len(pool)+1,2):
        fish = Fish(pool[i],pool[i+1])
        population.append(fish)
        if i >= len(pool)-2: break
    return population

def getCount(population: list[Fish], phenotype: str) -> int:
    return sum(1 for f in population if f.phenotype == phenotype)

def killPhenotype(population: list[Fish], phenotype: str) -> list[Fish]:
    """
    returns the population argument sans all fish with the given phenotype
    """
    population2 = population.copy() # it works just dont question it
    for i in population2:
        if i.phenotype == phenotype:
            population2.remove(i)
    return population2
