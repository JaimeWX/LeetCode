# 算法总结(递归的妙用)
'''
input：
preorder = [1,2,4,7,3,5,6,8]
inorder = [4,7,2,1,5,3,8,6]
iteration1：
preorder = [1,2,4,7,3,5,6,8] rootNode:1 leftSubTree:[2,4,7] rightSubTree:[3,5,6,8]
inorder = [4,7,2,1,5,3,8,6] rootNode:1 leftSubTree:[4,7,2] rightSubTree:[5,3,8,6]
iteration2:
preorder = [2,4,7] rootNode:2 leftSubTree:[4,7] rightSubTree:None
inorder = [4,7,2]  rootNode:2 leftSubTree:[4,7] rightSubTree: None
iteration3:
preorder = [4,7] rootNode:4 leftSubTree:None rightSubTree:[7]]
inorder = [4,7]  rootNode:4 leftSubTree:None rightSubTree:[7]
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        print(self.val)


class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        if(len(preorder) == 0 or len(inorder) == 0):
            return None
        else:
            rootValue = preorder[0]
            root = TreeNode(rootValue)
            for i in inorder:
                if i == rootValue:
                    rootIndexInInorder = inorder.index(i)

            leftSubtree_values_InInorder  = inorder[:rootIndexInInorder]
            rightSubtree_values_InInorder = inorder[rootIndexInInorder+1:]


            rightSubtree_length = len(inorder) - 1 - rootIndexInInorder
            leftSubtree_length  = len(inorder) - rightSubtree_length - 1

            leftSubtree_values_InPreorder  = preorder[1:leftSubtree_length + 1]
            rightSubtree_values_InPreorder = preorder[leftSubtree_length + 1:]

        if(leftSubtree_length > 0):
            root.left  = self.buildTree(leftSubtree_values_InPreorder,leftSubtree_values_InInorder)
        if(rightSubtree_length > 0):
            root.right = self.buildTree(rightSubtree_values_InPreorder,rightSubtree_values_InInorder)

        return root
i
preorder = [1,2,4,7,3,5,6,8]
inorder = [4,7,2,1,5,3,8,6]
#preorder = [3,9,20,15,7]
#inorder = [9,3,15,20,7]
ans = Solution()
ans.buildTree(preorder,inorder)


