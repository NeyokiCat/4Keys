import math
import csv
import secrets
import string

def main():
    # Start off interface
        # Generate
        # Search 
        # Statistics
    print()

# Patterns
# numbers = string.digits
# alpha = string.ascii_lowercase
# Alpha = string.ascii_uppercase
special = '!@#$%^&-_'

# Rules
Nonly = string.digits # Numbers Only
NaM = string.digits + string.ascii_lowercase # Numbers-lowerAlpha Mix
NAM = string.digits + string.ascii_uppercase # Numbers-upperAlpha Mix
NaAM = string.digits + string.ascii_letters # Numbers-Alpha Mix
NaAsM = NaAM + special # Numbers-Alpha-SpecialCharacter Mix

# Generate
def generate(length, rul):
    out = ' '.join(secrets.choice(rul) for i in range(length))
    return out

# Special Rules
AppleM = generate(6,NaAM) + '-' + generate(6,NaAM) + '-' + generate(6,NaAM)
MacM = generate(2,NAM) + ':' + generate(2,NAM) + ':' + generate(2,NAM) + ':' + generate(2,NAM) + ':' + generate(2,NAM) + ':' + generate(2,NAM)
TokenM = secrets.token_urlsafe()
# xkcdM =  # https://xkcd.com/936/

def generateRul(specRul):
    return specRul
    

# Tests 
# print(generate(12,NaAsM))
# print(generate(6,Nonly))
# print(generateRul(MacM))
# print(generateRul(TokenM))