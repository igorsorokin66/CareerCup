__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed in O(n)'

'''
Problem:
Given a boolean matrix,
write a code to find if an island of 0's
is completely surrounded by 1's.
Source:
http://www.careercup.com/question?id=5192952047468544
'''

def search(x, y, data):
    data[x][y] = "1"
    found_island = not (x == 0 or x == len(data)-1 or y == 0 or y == len(data[0])-1)
    if x - 1 >= 0 and data[x - 1][y] == "0":              # up
        found_island &= search(x - 1, y, data)
    if y + 1 <= len(data[x])-1 and data[x][y + 1] == "0":   # right
        found_island &= search(x, y + 1, data)
    if x + 1 <= len(data)-1 and data[x + 1][y] == "0":      # down
        found_island &= search(x + 1, y, data)
    if y - 1 >= 0 and data[x][y - 1] == "0":              # left
        found_island &= search(x, y - 1, data)
    return found_island

def test(data):
    for d in data:
        print("".join(d))
    for x in range(len(data)):
        for y in range(len(data[x])):
            if data[x][y] is "0":
                if search(x, y, data):
                    return True
    return False

data = [
    list("11111"),
    list("11011"),
    list("10001"),
    list("11011")
]
print("Result: " + str(test(data)))
print("Expect: False\n")

data = [
    list("11111"),
    list("10001"),
    list("10101"),
    list("10001"),
    list("11111")
]
print("Result: " + str(test(data)))
print("Expect: True\n")

data = [
    list("01"),
    list("11"),
]
print("Result: " + str(test(data)))
print("Expect: False\n")