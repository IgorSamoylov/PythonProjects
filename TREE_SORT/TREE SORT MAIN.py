#import TREE_SORT
from TREE_SORT1 import *

import random
testList = [random.randint(0, 100) for x in range(100)]

print('Test List: ', testList)

treeNode = tree(testList)


tree_traversal_direct(treeNode)
print('Output List Direct: ', outputList)
outputList.clear()

tree_traversal_inorder(treeNode)
print('Output List InOrder: ', outputList)
outputList.clear()

tree_traversal_postorder(treeNode)
print('Output List PostOrder: ', outputList)
outputList.clear()

tree_traversal_iterative_inorder(treeNode)
print('Output List Iterative InOrder: ', outputList)
outputList.clear()


#treeNode2 = treeNode

#while(treeNode != None):
#    print("MAX VALUES", treeNode.value)
#    treeNode = treeNode.rightNode

#treeNode = treeNode2
#while(treeNode != None):
#    print("MIN VALUES", treeNode.value)
#    treeNode = treeNode.leftNode
