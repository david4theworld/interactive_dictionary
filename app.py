import json
from difflib import get_close_matches as gcm

DATA = json.load(open("data/data.json"))

# search_input = input("Search for: ")

def  translate(s: str) -> str or list: 
    s = s.lower()
    if s in DATA.keys(): 
        return DATA[s]
    elif len(gcm(s, DATA.keys())) > 0:
        closest_match = gcm(s, DATA.keys())[0]
        yn = input("Did you mean '{}' instead? \n Y/N: ".format(closest_match)).upper()
        if yn == "Y": 
            return DATA[closest_match]
        elif yn == "N":
            return "The search for '{}' yielded no results. \nPlease double-check your search input.".format(s)
        else: 
            return "Error: Invalid input."
    else:
        print("The search for '{}' yielded no results. \nPlease double-check your search input.".format(s))


search_input = input("Search for: ")

output = translate(search_input)

if type(output) == list: 
    for i in output:
        print("{}".format(i), end="\n")
else: 
    print(output)