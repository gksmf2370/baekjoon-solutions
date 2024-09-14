import sys
import re

text = sys.stdin.read()

text = text.replace('E-N-D', "")

words = re.findall(r'[a-zA-Z-]+', text)

if words:
    long_world = max(words, key=len).lower()
    print(long_world)