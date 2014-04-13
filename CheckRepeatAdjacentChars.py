'''
Problem:
Return True if all adjacent characters repeat at least once
ccccccooollllllllllllll -> True
cccccollll -> False
Source:
http://www.careercup.com/question?id=5636895644057600
'''
import re
def checkRepeatAdjacentChars(word):
    while len(word) != 0:
        if word[0] == word[1]:
            word = re.sub(r'^%s+' % word[0],"",word) 
        else:
            return False
    return True
print(checkRepeatAdjacentChars("lloll"))