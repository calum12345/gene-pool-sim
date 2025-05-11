import csv
import random
import sys
from fish import Fish
import config
import genepool

if __name__ == "__main__":
    # create 2000 random alleles, green dominant, and red and yellow codominant
    genePoolCurrent = genepool.genNewPool(2000)
    genePoolHistory = (genePoolCurrent,)
    for i in range (config.generationNum):
        temp = (genePoolCurrent,)
        genePoolHistory += temp

        population = genepool.genPopulation(genePoolCurrent)

        green_count = genepool.getCount(population,"g")
        orange_count = genepool.getCount(population,"o")
        red_count = genepool.getCount(population,"r")
        yellow_count = genepool.getCount(population,"y")

        print(f"green: {green_count}\norange: {orange_count}\nred: {red_count}\nyellow: {yellow_count}\n")


        # remove 10% of yellow fish
        for i in population:
            if i.phenotype == "y" and random.randint(1,100) <= config.yellowFishDeathChance: population.remove(i)

        # erase old gene pool and add all alleles from current population yellows removed
        genePoolCurrent.clear()
        for i in population:
            # if allele randomly mutates, append a random allele to the gene pool. otherwise, append the alleles of each fish
            if random.randint(1,100) <= config.mutationChance:
                genePoolCurrent.append(random.choice(["g","r","y"]))
            else:
                genePoolCurrent.append(i.allele1)
            if i != len(population)-1: 
                if random.randint(1,100) <= config.mutationChance:
                    genePoolCurrent.append(random.choice(["g","r","y"]))
                else:
                    genePoolCurrent.append(i.allele2)
