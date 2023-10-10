import tkinter as tk

'''
FEATURES TO ADD:
Calculate compatibility from link or from pasted results
Supports group compatibility testing
UI
Shows most compatible kinks
'''

pairs = {
    'Rigger' : 'Rope bunny',
    'Sadist' : 'Masochist',
    'Dominant' : 'Submissive',
    'Brat tamer' : 'Brat',
    'Daddy/Mommy' : 'Boy/Girl',
    'Primal (Hunter)' : 'Primal (Prey)',
    'Master/Mistress' : 'Slave',
    'Degrader' : 'Degradee', 
    'Owner' : 'Pet',

    'Switch' : 'Switch', 
    'Vanilla' : 'Vanilla',
    'Experimentalist' : 'Experimentalist',
    'Exhibitionist' : 'Exhibitionist',
    'Voyeur' : 'Voyeur',
    'Ageplayer' : 'Ageplayer',
    'Non-monogamist' : 'Non-monogamist'
}

'''
Calculates how compatible each person 
is for each kink by multiplying percents
for paired kinks and dividing by total
'''
def calculateCompatibility(playmates):
    compatible = 0
    n = 0

    for kink in playmates[0]:
        if kink in pairs:
            n += 1
            compatible += playmates[0][kink] * playmates[1][pairs[kink]]

    compatible *= 1/n

    return compatible

'''
Extracts dictionary of kinks and their percentages
from text results presented at conclusion of test
'''
def stripText(textResults):
    lines = textResults.strip().split('\n')
    results = {}
    
    for line in lines[1:26]:
        percentage, kink = line.split(" ", 1)
        kink = kink.strip()
        percentage = int(percentage.replace("%", "").strip()) / 100
        results[kink] = percentage
    
    return results

'''
Extracts dictionary of kinks and their percentages
from link presented at conclusion of test
'''
'''
def stripLink(url):
    results = {}

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    response = requests.get(url, headers=headers)

    return results
'''
def main():
    p1 = '''
== Results from bdsmtest.org == 
100% Ageplayer 
0% Brat 
100% Exhibitionist 
100% Voyeur 
100% Switch 
0% Slave 
100% Sadist 
0% Rope bunny 
100% Rigger 
0% Primal (Prey) 
100% Primal (Hunter) 
100% Owner 
100% Non-monogamist 
100% Master/Mistress 
0% Masochist 
0% Boy/Girl 
0% Degradee 
100% Brat tamer 
100% Experimentalist 
0% Pet 
100% Degrader 
100% Daddy/Mommy 
0% Submissive 
100% Dominant 
100% Vanilla 
    '''

    p2 = '''
== Results from bdsmtest.org == 
100% Ageplayer 
100% Brat 
100% Exhibitionist 
100% Voyeur 
100% Switch 
100% Slave 
0% Sadist 
100% Rope bunny 
0% Rigger 
100% Primal (Prey) 
0% Primal (Hunter) 
0% Owner 
100% Non-monogamist 
0% Master/Mistress 
100% Masochist 
100% Boy/Girl 
100% Degradee 
0% Brat tamer 
100% Experimentalist 
100% Pet 
0% Degrader 
0% Daddy/Mommy 
100% Submissive 
0% Dominant 
100% Vanilla 
    '''

    ar = [stripText(p1), stripText(p2)]
    print(calculateCompatibility(ar))

if __name__ == "__main__":
    main()