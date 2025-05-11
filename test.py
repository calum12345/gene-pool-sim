import unittest
import genepool
import fish
import random

class TestFish(unittest.TestCase):
    def testPhenotype(self):
        self.assertEqual(fish.Fish("g","g").phenotype, "g")
        self.assertEqual(fish.Fish("g","r").phenotype, "g")
        self.assertEqual(fish.Fish("g","y").phenotype, "g")
        self.assertEqual(fish.Fish("r","r").phenotype, "r")
        self.assertEqual(fish.Fish("y","y").phenotype, "y")
        self.assertEqual(fish.Fish("r","y").phenotype, "o")

class TestGenePool(unittest.TestCase):
    def testGenPool(self):
        length = random.randint(1,999999)
        self.assertEqual(len(genepool.genNewPool(length)),length)
    def testGenPop(self):
        example = fish.Fish("r","y")
        pool = ["r", "y"]
        self.assertEqual(example.phenotype, genepool.genPopulation(pool)[0].phenotype)
    def test_getCount(self):
        example = [fish.Fish("g","r"), fish.Fish("r","r"), fish.Fish("y","r")]
        self.assertEqual(genepool.getCount(example, "g"),1)
        self.assertEqual(genepool.getCount(example, "o"),1)
        self.assertEqual(genepool.getCount(example, "r"),1)
        self.assertEqual(genepool.getCount(example, "y"),0)

if __name__ == '__main__':
    unittest.main()