# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and not t2:
            return None
        if t1:
            V1, L1, R1 = t1.val, t1.left, t1.right
        else:
            V1, L1, R1 = 0, None, None

        if t2:
            V2, L2, R2 = t2.val, t2.left, t2.right
        else:
            V2, L2, R2 = 0, None, None

        node = TreeNode(V1 + V2)
        node.left = self.mergeTrees(L1, L2)
        node.right = self.mergeTrees(R1, R2)
        return node