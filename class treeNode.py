class treeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right= None

root = treeNode('R')
nodeA = treeNode('A')
nodeB = treeNode('B')
nodeC = treeNode('C')
nodeD = treeNode('D')
nodeE = treeNode('E')
nodeF = treeNode('F')
nodeG = treeNode('G')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeA.left = nodeG

#Test 
print("root.right.left.data:", root.right.data)