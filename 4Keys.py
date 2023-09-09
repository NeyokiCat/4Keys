import math
import pandas as pd
import os
import secrets
import string

#inits
PATH = os.path.dirname(__file__)
PATH_to_keys = PATH+'/Keys'
startOff = '''Welcome to 4Keys\nGenerate a new key(1), Search for a key (2), Show key statistics (3), Quit(0)    '''

# Patterns
# numbers = string.digits
# alpha = string.ascii_lowercase
# Alpha = string.ascii_uppercase
special = '!@#$%^&*+<>?-'

# Rules
NM = string.digits # Numbers Only
NaM = string.digits + string.ascii_lowercase # Numbers-lowerAlpha Mix
NAM = string.digits + string.ascii_uppercase # Numbers-upperAlpha Mix
NaAM = string.digits + string.ascii_letters # Numbers-Alpha Mix
NaAsM = NaAM + special # Numbers-Alpha-SpecialCharacter Mix

# Generate
def generate(length, rul):
    out = ''.join(secrets.choice(rul) for i in range(length))
    return out

# Special Rules
AppleM = generate(6,NaAM) + '-' + generate(6,NaAM) + '-' + generate(6,NaAM)
MacM = generate(2,NAM) + ':' + generate(2,NAM) + ':' + generate(2,NAM) + ':' + generate(2,NAM) + ':' + generate(2,NAM) + ':' + generate(2,NAM)
TokenM = secrets.token_urlsafe()
# xkcdM =  # https://xkcd.com/936/

def generateRul(specRul):
    return specRul
    
# Search
def search():
    for (root, dirs, k) in os.walk(PATH_to_keys):
        # print(root)
        root += '/'
        # print(dirs)
        for f in k:
            f = root + f
            #print(f)
            if '.csv' in f:
                return [f,'csvFile']
            else:
                try:
                    open(f, 'r',encoding = 'utf-8' )
                    return [f,'txtFile']
                except:
                    None
        
def choice(c):
    while True:
        if c == '0':
            break
        # Generate
        if c == '1':
            c += input('Create key using pattern(1) / Embedded rules(2)    ')
            
        if c == '11':
            rul = input('NM,NaM,NAM,NaAM,NaAsM    ')
            leng = int(input('Length?    '))
            if rul == 'NM':
                key = generate(leng,NM)
            if rul == 'NaM':
                key = generate(leng,NaM)
            if rul == 'NAM':
                key = generate(leng,NAM)
            if rul == 'NaAM':
                key = generate(leng,NaAM)
            if rul == 'NaAsM':
                key = generate(leng,NaAsM)
            c = '10'
            
        if c == '12':
            rul = input('AppleM, MacM, TokenM    ')
            if rul == 'AppleM':
                key = generateRul(AppleM)
            if rul == 'MacM':
                key = generateRul(MacM)
            if rul == 'TokenM':
                key = generateRul(TokenM)
            c = '10'
            
        if c== '10':
            print('New Key:\n' + key+'\n')
            res = search()
            print('find ' + res[1] + ' at \'' + res[0] + '\'')
            if input('continue (1), choose another path (2)    ') == '1':
                sv = input('Save the key? Yes(1) / No(2)    ')
                if sv == '1':
                    break
                if sv == '2':
                    break
            else:
                break
            
        # Search 
        if c == '2':
            res = search()
            print('find ' + res[1] + ' at \'' + res[0] + '\'')
            c += input('continue (1), choose another path (2)    ')
        
        if c == '21':
                if res[1] == 'csvFile':
                    with open(res[0], newline='') as csvfile:
                        df = pd.read_csv(csvfile)
                        keyword = input('Search for keyword:')
                    for row in df:
                        print(df.loc[df[row] == keyword])
                else:
                    print('Error, KeyFile type not supported')
                    break
                
        if c == '22':
            break
        
        # Statistics
        if c == '3':
            break
    
  
    
def main(ans = ''):
    # Start-off interface
    if ans != '':
        choice(ans)
    else:
        main(input(startOff))
    

# Tests 
# print(generate(12,NaAsM))
# print(generate(6,Nonly))
# print(generateRul(MacM))
# print(generateRul(TokenM))
# print(search()[1])

main()