'''
FEATURES TO ADD:
Calculate compatibility from link or from pasted results
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
    compatibility = 0
    n = len(pairs)

    for kink in pairs:
        addend = 1
        top = max(playmates, key=lambda playmate: playmate[kink])
        addend *= top[kink]
        for sub in playmates:
            addend *= sub[pairs[kink]]

        compatibility += addend

    return compatibility / n

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
100% Switch 
100% Rigger 
100% Sadist 
100% Rope bunny 
81% Masochist 
70% Exhibitionist 
67% Voyeur 
61% Dominant 
61% Submissive 
52% Vanilla 
52% Experimentalist 
43% Brat tamer 
43% Daddy/Mommy 
31% Primal (Prey) 
5% Primal (Hunter) 
4% Brat 
1% Master/Mistress 
0% Ageplayer 
0% Slave 
0% Degradee 
0% Boy/Girl 
0% Degrader 
0% Pet 
0% Owner 
0% Non-monogamist 
'''
if __name__ == "__main__":
    main()