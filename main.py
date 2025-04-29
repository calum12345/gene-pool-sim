import csv
import random
import sys
from fish import Fish
import config

if __name__ == "__main__":
    # create 2000 random alleles, green dominant, and red and yellow codominant
    genePoolCurrent = [random.choice(["g","r","y"]) for i in range(2000)]
    genePoolHistory = (genePoolCurrent,) # temporary fix for before i loop it
    for i in range (config.generationNum):
        temp = (genePoolCurrent,)
        genePoolHistory += temp

        population = []

        # create population of fish based on gene pool
        for i in range(0,len(genePoolCurrent)+1,2):
            fish = Fish(genePoolCurrent[i],genePoolCurrent[i+1])
            population.append(fish)
            if i >= len(genePoolCurrent)-2: break

        green_count = sum(1 for f in population if f.phenotype == 'g')
        orange_count = sum(1 for f in population if f.phenotype == 'o')
        red_count = sum(1 for f in population if f.phenotype == 'r')
        yellow_count = sum(1 for f in population if f.phenotype == 'y')

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
                    