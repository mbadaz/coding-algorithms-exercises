
# Given the root to a binary tree, implement serialize(root), which serializes 
# the tree into a string, and deserialize(s), which deserializes the string
# back into the tree. 

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    

def serialize(root):
    if(root == None):
        return "none"
    else:
        return root.val + " " + serialize(root.left) +  " " + serialize(root.right)

stringList = None
def deserialize(stringData):
    global stringList
    stringList = stringData.split(" ")
    return createSubTree(stringList[0])

def createSubTree(val):
    global stringList
    stringList = stringList[1:]

    if(val == "none"):
        return None
    
    return Node(
        val, 
        createSubTree(stringList[0]),
        createSubTree(stringList[0]))
    

node = Node("root", 
                Node("L", 
                    Node("L.L", 
                        Node("L.L.L"),
                        Node("L.L.R")
                        ), 
                    Node("L.R")
                    ),
                Node("R", 
                    Node("R.L", 
                        Node("R.L.L"),
                        Node("R.L.R")
                        ),
                    Node("R.R", 
                        Node("R.R.L"))
                    )
            )

assert deserialize(serialize(node)).right.left.right.val == "R.L.R"