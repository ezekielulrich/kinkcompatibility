'''
FEATURES:
Calculate compatibility from link or from pasted results
Supports group compatibility testing
UI
'''

def calculateCompatibility(playmates):
    for playmate in playmates:
        pass

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
        percentage = int(percentage.replace("%", "").strip())
        results[kink] = percentage
    
    return results

def stripLink():
    pass

def main():
    string = '''== Results from bdsmtest.org == 
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
http://bdsmtest.org/r/unZzJWNm'''
    print(stripText(string))

if __name__ == "__main__":
    main()