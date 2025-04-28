from typing import Literal
"""fish"""
class Fish:
    def __init__(self, allele1: Literal["g","r","y"], allele2: Literal["g","r","y"]):
        self.allele1=allele1
        self.allele2=allele2
    
    @property
    def phenotype(self):
        if "g" in [self.allele1, self.allele2]: return "g"
        if self.allele1 == self.allele2: return self.allele1
        return "o"