import math
import csv
import random

def main():
    # Start off interface
        # Generate
        # Search 
        # Statistics
    print()

# Patterns
numbers = ['0','1','2','3','4','5','6','7','8','9']
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
special = ['!','@','#','$','%','^','&','-','_']

# Rules
Nonly = numbers # Numbers Only
NaM = Nonly + alpha # Numbers-lowerAlpha Mix
NAM = Nonly + Alpha # Numbers-upperAlpha Mix
NaAM = NaM + Alpha # Numbers-Alpha Mix
NaAsM = NaAM + special # Numbers-Alpha-SpecialCharacter Mix

# Generate
def generate(length, rul):
    out = ""
    for i in range(length):
        out += random.choice(rul)
    return out

# Special Rules
AppleM = generate(6,NaAM) + '-' + generate(6,NaAM) + '-' + generate(6,NaAM)
MacM = generate(2,NAM) + ':' + generate(2,NAM) + ':' + generate(2,NAM) + ':' + generate(2,NAM) + ':' + generate(2,NAM) + ':' + generate(2,NAM)

def generateRul(specRul):
    return specRul
    

# Tests 
# print(generate(12,NaAsM))
# print(generate(6,Nonly))
# print(generateRul(MacM))