zen='Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
vowel='aeiou'

for i in zen:
  if i in vowel:
    zen=zen.replace(i,"")
print(zen)