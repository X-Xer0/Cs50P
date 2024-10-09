import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    font = random.choice(figlet.getFonts())
    figlet.setFont(font=font)
elif len(sys.argv) == 3 and sys.argv[1] in ['-f', '--font']:
    if sys.argv[2] in figlet.getFonts():
        figlet.setFont(font=sys.argv[2])
    else:
        sys.exit("Error: Invalid font name.")
else:
    sys.exit("Usage: python program.py [-f FONT_NAME]")

text = input("Input: ")

print(figlet.renderText(text))
