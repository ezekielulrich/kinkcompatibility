'''
FEATURES TO ADD:
Calculate compatibility from link or from pasted results
UI
Shows most compatible kinks
'''
import tkinter as tk
from tkinter.simpledialog import askstring

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

intro = '''
Welcome to the kink compatibility calculator!
To begin, please paste the bdsmtest.org results
of at least two people in the text box.
'''

'''
Calculates how compatible each person 
is for each kink by multiplying percents
for paired kinks and dividing by total
'''

def show_number(number):
    print("You compatibility score is", number, "%")

    popup = tk.Tk()
    popup.title("Number Display")

    label = tk.Label(popup, text=f"You are {number} % compatible!", font=("Arial", 12))
    label.pack(padx=10, pady=10)

    popup.mainloop()

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

    num = 0
    response = ""
    playmates = []

    print(intro)

    root = tk.Tk()
    root.withdraw() 

    while response != "c" and response != "q":

        response = askstring("Input", "Paste results here.\n")

        if response == "c":
            if num > 1:
                show_number(round(100 * calculateCompatibility(playmates), 2))
            else:
                print("You need at least two people to calculate compatibility")
                response = "try your left hand"
        elif response == "q" or response == None:
            print("Thanks for playing! ;)")
            break
        else: 
            try:
                playmates.append(stripText(response))
                num += 1
            except:
                print("That's not a valid response, please try again")

        

    
        
if __name__ == "__main__":
    main()