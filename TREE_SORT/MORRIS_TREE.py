
class TreeNode:
    value = None
    upperNode = None
    nextNode = None

def tree_morris(iList: list[int]) -> TreeNode:
    firstNode = TreeNode() #Creating first Tree Node
    firstNode.value = iList[0] # Assigning first Tree Node value
    iList = iList[1:]  # Cut list in front with the first value
    
    for i in iList:
        treeNode = TreeNode() # Creating a new node for the next element
        treeNode.value = i
        
        checkTree = firstNode
        while(checkTree != None):
            lastPresentNode = checkTree # Save the reference to last succefull result of tree traversal
            if i >= checkTree.value:
                checkTree = checkTree.nextNode
            else:
                checkTree = checkTree.upperNode

        if i >= lastPresentNode.value: # Writing reference to the last tree node in a correct branch 
            lastPresentNode.nextNode = treeNode
        else:
            lastPresentNode.upperNode = treeNode
        

    return firstNode

outputList = []
def tree_morris_traverse_inorder(node: TreeNode):

    if node.
    




import random
testList = [random.randint(0, 100) for x in range(100)]

print('Test List: ', testList)

treeNode = tree_morris(testList)


