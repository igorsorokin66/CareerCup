__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = ''

'''
Problem:
Given two strings a and b,
find whether any anagram of string a is a substring of string b.
a = "xyz" and b = "afdgzyxksldfm" -> True
Source:
http://www.careercup.com/question?id=5389078581215232
'''
def generateHash(a):
    hash = {}
    for letter in a:
        if letter in hash.keys():
            hash[letter] += 1
        else:
            hash[letter] = 1
    return hash

def find(a, b):
    print("Searching for anagram of " + a + " in " + b)
    count = generateHash(a)
    start_pointer = 0
    while True:
        start_letter = b[start_pointer]
        if start_letter in a:
            count[start_letter] -= 1
            copy_of_count = dict(count)
            for end_pointer in range(start_pointer + 1, len(b)):
                end_letter = b[end_pointer]
                if end_letter not in count:
                    start_pointer = end_pointer + 1
                    count = dict(copy_of_count)
                    break
                count[end_letter] -= 1
                if count.values().count(0) == len(count.values()):#CAN WE IMPROVE THIS?
                    print("Start: " + str(start_pointer))
                    print("End: " + str(end_pointer))
                    return True
                if end_pointer+1 == len(b):
                    return False
                if count[end_letter] < 0:
                    count[end_letter] += 1
                    start_pointer = end_pointer - 1 #MOVES POINTER
                    break
            count[start_letter] += 1
        start_pointer += 1
        if start_pointer > len(b):
            break

print("Result: " + str(find("xyz", "yxyzx")))
print("Expect: True\n")

print("Result: " + str(find("xyyy", "yxyx")))
print("Expect: False\n")

print("Result: " + str(find("xxy", "yxyx")))
print("Expect: True\n")

print("Result: " + str(find("xyz", "afdgzyxksldfm")))
print("Expect: True\n")