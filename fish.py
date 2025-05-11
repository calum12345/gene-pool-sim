from typing import Literal

class Fish:
    """
    is a fish

    attributes:
        allele1 (str)
        allele2 (str)
        phenotype (str): calculated based on allele1 and allele2. read only

    """
    def __init__(self, allele1: Literal["g","r","y"], allele2: Literal["g","r","y"]):
        self.allele1=allele1
        self.allele2=allele2
    
    @property
    def phenotype(self):
        if "g" in [self.allele1, self.allele2]: return "g"
        if self.allele1 == self.allele2: return self.allele1
        return "o"