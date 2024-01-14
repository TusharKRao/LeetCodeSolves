def maxDepth(self, root: Optional[TreeNode]) -> int:

    def dive(root):
        if root is None:
            return 0
        left = 1 + dive(root.left)
        right = 1 + dive(root.right)
        return max(left, right)
    return dive(root)