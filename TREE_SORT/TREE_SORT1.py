
class TreeNode:
    value = None
    leftNode = None
    rightNode = None

def tree(iList: list[int]) -> TreeNode:
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
                checkTree = checkTree.rightNode
            else:
                checkTree = checkTree.leftNode

        if i >= lastPresentNode.value: # Writing reference to the last tree node in a correct branch 
            lastPresentNode.rightNode = treeNode
        else:
            lastPresentNode.leftNode = treeNode
       
    return firstNode


# Easy recursive tree traversal without keeping order of elements. Direct traversal.

outputList = []

def tree_traversal_direct(node: TreeNode):

    if node == None:
        return
    
    outputList.append(node.value)

    tree_traversal_direct(node.leftNode)
    
    tree_traversal_direct(node.rightNode)


def tree_traversal_inorder(node: TreeNode):

    if node == None:
        return
    
    tree_traversal_inorder(node.leftNode)
    
    outputList.append(node.value)

    tree_traversal_inorder(node.rightNode)
    

def tree_traversal_postorder(node: TreeNode):

    if node == None:
        return
    
    tree_traversal_postorder(node.leftNode)
    
    tree_traversal_postorder(node.rightNode)
    
    outputList.append(node.value)


#Iterative inorder traversal

def tree_traversal_iterative_inorder(node: TreeNode):
    stack = Stack()
    while (not stack.isEmpty() or node != None):
        if (node != None):
            stack.push(node)
            node = node.leftNode
        else:
            node = stack.pop()
            outputList.append(node.value)
            node = node.rightNode


class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
    
