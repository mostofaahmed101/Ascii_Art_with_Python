#!/bin/python
import pyfiglet


t = input("Type your text --> ")

with open("fontList.txt") as filef:
    fonts = filef.read().splitlines()

for f in fonts:
    try:
        print("Trying Font --> "+ f +"\n")
        out = pyfiglet.figlet_format(text=t,font=f)
        print(out)
    except Exception:
        continue

