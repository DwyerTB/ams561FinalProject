# MorseCodeVer1.py
# Dwyer Bradley
# AMS 561

import re

# Make a class that lets us define leaves
class leaf:
    def __init__(self, value, leftChild = None, rightChild = None):
        self.value = value
        self.leftChild = leftChild
        self.rightChild = rightChild


# Build Morse Code Tree by defining leaves and their relationships

mcTreeRoot = leaf("")

# ---------------------------------------------------------------
#     mcTreeRoot
#       /     \
#      E       T

mcTreeRoot.leftChild = leaf("E")
e = mcTreeRoot.leftChild 
         
mcTreeRoot.rightChild = leaf("T")
t = mcTreeRoot.rightChild

# ---------------------------------------------------------------
#     mcTreeRoot
#       /     \
#      E       T
#     / \
#    I   A

e.leftChild = leaf("I")
i = e.leftChild

e.rightChild = leaf ("A")
a = e.rightChild

# ---------------------------------------------------------------
#     mcTreeRoot
#       /     \
#      E       T
#     / \     / \
#    I   A   N   M

t.leftChild = leaf("N")
n = t.leftChild

t.rightChild = leaf("M")
m = t.rightChild

# ---------------------------------------------------------------
#     mcTreeRoot
#       /     \
#      E       T
#     / \     / \
#    I   A   N   M
#   / \
#  S   U

i.leftChild = leaf("S")
s = i.leftChild

i.rightChild = leaf("U")
u = i.rightChild

# ---------------------------------------------------------------
#         mcTreeRoot
#        /            \
#       E              T
#     /   \           / \
#    I     A         N   M
#   / \   / \
#  S   U  R  W

a.leftChild = leaf("R")
r = a.leftChild

a.rightChild = leaf("W")
w = a.rightChild

# ---------------------------------------------------------------
#         mcTreeRoot
#        /            \
#       E              T
#     /   \           / \
#    I     A         N   M
#   / \   / \       / \ 
#  S   U  R  W     D   K

n.leftChild = leaf("D")
d = n.leftChild

n.rightChild = leaf("K")
k = n.rightChild

# ---------------------------------------------------------------
#         mcTreeRoot
#        /            \
#       E               T
#     /   \           /   \
#    I     A         N     M
#   / \   / \       / \   / \
#  S   U  R  W     D   K G   O

m.leftChild = leaf("G")
g = m.leftChild

m.rightChild = leaf("O")
o = m.rightChild

# ---------------------------------------------------------------
#          mcTreeRoot
#         /            \
#        E               T
#      /   \           /   \
#     I     A         N     M
#    / \   / \       / \   / \
#   S   U  R  W     D   K G   O
#  / \
# H   V

s.leftChild = leaf("H")
h = s.leftChild

s.rightChild = leaf("V")
v = s.rightChild

# ---------------------------------------------------------------
#            mcTreeRoot
#          /             \
#         E               T
#       /   \           /   \
#      I     A         N     M
#    /  \   / \       / \   / \
#   S    U  R  W     D   K G   O
#  / \  /
# H   V F

u.leftChild = leaf("F")
f = u.leftChild

# ---------------------------------------------------------------
#            mcTreeRoot
#          /             \
#         E               T
#       /   \           /   \
#      I     A         N     M
#    /  \   / \       / \   / \
#   S    U  R  W     D   K G   O
#  / \  /  /
# H   V F  L

r.leftChild = leaf("L")
l = r.leftChild

# ---------------------------------------------------------------
#            mcTreeRoot
#          /             \
#         E               T
#       /   \           /   \
#      I     A         N     M
#    /  \   / \       / \   / \
#   S    U  R  W     D   K G   O
#  / \  /  /  / \
# H   V F  L P   J

w.leftChild = leaf("P")
p = w.leftChild

w.rightChild = leaf("J")
j = w.rightChild

# ---------------------------------------------------------------
#            mcTreeRoot
#          /             \
#         E               T
#       /   \           /   \
#      I     A         N     M
#    /  \   / \       / \   / \
#   S    U  R  W     D   K G   O
#  / \  /  /  / \   / \
# H   V F  L P   J B   X

d.leftChild = leaf("B")
b = d.leftChild

d.rightChild = leaf("X")
x = d.rightChild

# ---------------------------------------------------------------
#             mcTreeRoot
#          /                \
#         E                  T
#       /   \            /       \
#      I     A          N         M
#    /  \   / \       /   \      / \
#   S    U  R  W     D     K    G   O
#  / \  /  /  / \   / \   / \  
# H   V F  L P   J B   X C   Y 

k.leftChild = leaf("C")
c = k.leftChild

k.rightChild = leaf("Y")
y = k.rightChild

# ---------------------------------------------------------------
#             mcTreeRoot
#          /                \
#         E                  T
#       /   \            /       \
#      I     A          N          M
#    /  \   / \       /   \       / \
#   S    U  R  W     D     K     G   O
#  / \  /  /  / \   / \   / \   / \
# H   V F  L P   J B   X C   Y Z   Q

g.leftChild = leaf("Z")
z = g.leftChild

g.rightChild = leaf("Q")
q = g.rightChild
# ---------------------------------------------------------------


# Collects the dot or dash as it moves up the tree and puts it at the front of 
# the collection list (mCode)
# Use for Encoding (English to Morse Code)
def collectDotOrDash(leaf, letter, mCode):
    if leaf == None:
        return False
    elif leaf.value == letter:
        return True
    else:
        if collectDotOrDash(leaf.leftChild, letter, mCode) == True:
            mCode.insert(0,".")
            return True
        elif collectDotOrDash(leaf.rightChild, letter, mCode) == True:
            mCode.insert(0, "-")
            return True


def decode():
    while True:
        
        inp = input("What Morse Code would you like to translate into English?\n \
    (Remember to put spaces between each letter)\n \
    (Press enter to go back)\n")

        dotsDashesAndSpaces = re.compile(r'^[ .\-]+$')
        
        if inp == "":

            print("Going back: \n")
            break

        elif dotsDashesAndSpaces.match(inp):
            currentLeaf = mcTreeRoot
            outputMessage = ""
            for char in inp:
                if char == ".":
                    currentLeaf = currentLeaf.leftChild
                elif char == "-":
                    currentLeaf = currentLeaf.rightChild
                elif char == " ":
                    outputMessage += currentLeaf.value
                    currentLeaf = mcTreeRoot
            outputMessage += currentLeaf.value
            print(outputMessage)

        else:
            print("Please enter a message containing only \
. or - characters.\n")


def encode():

    onlyLettersPattern = re.compile(r'^[a-zA-Z]+$')
    spacesAndLettersPattern = re.compile(r'^[a-zA-Z ]+$')

    while True:
        # Take input to translate into Morse Code
        inp = input("What would you like to translate into Morse Code?\n \
    (Press enter to go back)\n")

        if inp == "":
            print("Going back: \n")
            break
        
        elif spacesAndLettersPattern.match(inp):

            preppedInp = (str(inp)).upper()
            preppedInpBag = [ char for char in preppedInp]
            preppedInpBag.reverse()
            reversedInpStr = ''.join(preppedInpBag)
            newMCodeBag = []

            # Iterate over input and convert to Morse Code letter by letter
            mCode = []
            mCodeBag = []
            testBag = []

            for letter in inp:
                testBag.append([letter])
            #print('testBag:', testBag)
            
            for letter in reversedInpStr:
                if letter == " ":
                    # puts space slash sign space between words
                    mCodeJoined = " / "
                else:
                    collectDotOrDash(mcTreeRoot, letter, mCode)
                    mCodeJoined = ''.join(mCode)
                    
                mCodeBag.append([mCodeJoined])
                # puts space between each letter in morse code
                mCodeBag.append([" "])
                mCode = []

            
            mCodeBag.reverse()

            for item in mCodeBag:
                item = ''.join(item)
                newMCodeBag.append(item)

            newMCodeBagStr = "".join(newMCodeBag)

            print(newMCodeBagStr)


        else:
            print("Please enter a message containing only\
Alphabetic characters.\n")
  

def main():
    while True:
        inp = input("Hello! I can help you with Morse Code messages.\n\
Would you like to encode (English to Morse Code) \nor \
decode (Morse Code to English): \n\
    \nType 'Encode' or 'Decode' or press 'Enter' to quit.\n")

        inp = inp.upper()

        if inp == "ENCODE":
            encode()

        elif inp == "DECODE":
            decode()

        elif inp == "":
            print("Bye for now!")
            break

        else:
            print("I'm sorry; I don't understand. Please try again:\n")

main()
        


