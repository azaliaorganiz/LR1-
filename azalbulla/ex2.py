import copy
import math

text: str = "     Hello, Python!   "
print(F"1) text: {text}")
stripText = text.strip()
print(F"2) textStrip: {stripText}")
textWithQ = stripText.replace("!","?")
print(F"3) textWithQ: {textWithQ}")
upTextWithQ = textWithQ.upper()
print(F"4) uppercase: {upTextWithQ}")
lowerText = text.strip().lower()
print(F"5) lowerText: {lowerText}")