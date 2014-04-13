'''
Problem:
Write code to generate all possible case combinations of a given lower-cased string
"0ab" -> ["0ab", "0aB", "0Ab", "0AB"])
Source:
http://www.careercup.com/question?id=5761652767064064
'''
class Node:
    def __init__(self,val,next):
        self._val = val
        self._next = next
    def setVal(self, val):
        self._val = val
    def getVal(self):
        return self._val
    def setNext(self, next):
        self._next = next
    def getNext(self):
        return self._next

def allPossiCaseCombos(str):
    curr = Node(0,None)
    root = Node(0,curr)
    l = []
    for c in str:
        if c.isnumeric():
            curr.setNext(Node(c, None))
        else:
            l.append(Node(c,None))
            if c.istitle():
                l.append(Node(c.lower(),None))
            else:
                l.append(Node(c.upper(),None))
            curr.setNext(Node(l,None))
            l = []
        curr = curr.getNext()
    return root

curr = allPossiCaseCombos("ab6cd").getNext().getNext()
def go(curr,str):
    if curr.getNext() == None:
        if isinstance(curr.getVal(),list):
            for n in curr.getVal():
                print(str+n.getVal())
        else:
            print(str+curr.getVal())
        return
    if isinstance(curr.getVal(),list):
        for n in curr.getVal():
            go(curr.getNext(),str+n.getVal())
    else:
        go(curr.getNext(),str+curr.getVal())
go(curr,"")