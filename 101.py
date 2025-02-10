class Solution(object):
    def helper(self, rootA, rootB):
        if rootA is None and rootB is None:
            return True
        elif rootA is None or rootB is None:
            return False
        elif rootA.val == rootB.val:
            return self.helper(rootA.left, rootB.right) and self.helper(rootA.right, rootB.left)
        else: 
            return False

    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root is None:
            return True 
        
        return self.helper(root.left, root.right)
