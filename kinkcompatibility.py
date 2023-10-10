import tkinter as tk
from tkinter import messagebox

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

entry1 = ""
entry2 = ""
'''
Calculates how compatible each person 
is for each kink by multiplying percents
for paired kinks and dividing by total
'''
def calculateCompatibility(playmates):
    print("Called")
    compatibility = 0
    n = 1

    for kink in playmates[0]:
        print("More than once")
        if kink in pairs:
            n += 1
            compatibility += playmates[0][kink] * playmates[1][pairs[kink]]

    compatibility *= 1/n

    return compatibility

def enter(entry1, entry2):
    playmate1 = entry1.get()
    playmate2 = entry2.get()

    result = calculateCompatibility([playmate1, playmate2])
    messagebox.showinfo("Compatibility Result", result)

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

    # main window
    root = tk.Tk()
    root.title("Kink Compatibility")

    window_width = int(root.winfo_screenwidth() * 0.5)
    window_height = int(root.winfo_screenheight() * 0.5)
    root.geometry(f"{window_width}x{window_height}")

    root.configure(bg="black") 

    # Create entry fields
    label1 = tk.Label(root, text="First results:")
    entry1 = tk.Entry(root)

    label2 = tk.Label(root, text="Second results")
    entry2 = tk.Entry(root)

    label1.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    entry1.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    label2.grid(row=1, column=0, padx=5, pady=5, sticky="e")
    entry2.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    # Create a button to calculate compatibility
    calculate_button = tk.Button(root, text="Calculate", command=lambda : enter(entry1, entry2))
    calculate_button.grid(row=2, columnspan=2, pady=10)

    # Start the main event loop
    root.mainloop()

if __name__ == "__main__":
    main()