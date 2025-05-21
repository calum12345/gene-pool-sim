import pytest
import genepool
import fish
import random

class TestFish:
    def test_phenotype(self):
        assert fish.Fish("g", "g").phenotype == "g"
        assert fish.Fish("g","r").phenotype == "g"
        assert fish.Fish("r","r").phenotype == "r"
        assert fish.Fish("y","y").phenotype == "y"
        assert fish.Fish("r","y").phenotype == "o"

class TestGenePool:
    def test_genPool(self):
        length = random.randint(1,999999)
        assert len(genepool.genNewPool(length)) == length

    def test_genPopulation(self):
        example = fish.Fish("r","y")
        pool = ["r", "y"]
        assert example.phenotype == genepool.genPopulation(pool)[0].phenotype
        with pytest.raises(ValueError):
            genepool.genPopulation(["r"])[0].phenotype
        with pytest.raises(ValueError):
            genepool.genPopulation(["r","y","o"])[1].phenotype

    def test_getCount(self):
        example = [fish.Fish("g","r"), fish.Fish("r","r"), fish.Fish("y","r")]
        assert genepool.getCount(example, "g") == 1
        assert genepool.getCount(example, "o") == 1
        assert genepool.getCount(example, "r") == 1
        assert genepool.getCount(example, "y") == 0
    
    def test_killPhenotype(self):
        example = [fish.Fish('g','g'), fish.Fish('r','r'), fish.Fish('y', 'y'), fish.Fish('y','r')]
        for i in ['g','o','r','y']:
            assert len(genepool.killPhenotype(example,i)) == 3
