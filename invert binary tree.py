def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    def inv(root):
        while root is not None:
            temp = root.left
            root.left = root.right
            root.right = temp
            inv(root.right)
            inv(root.left)
            return root

    inv(root)
    return root