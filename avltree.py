class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class AVL:
    def getHeight(self, root):
        if not root:
            return 0

        return root.height


    def insert(self, root, key):
        # Step 1 - Perform normal BST
        if not root:
            return TreeNode(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        root.height = 1 + max(self.getHeight(root.left),
                                   self.getHeight(root.right))
        return root
    def preorder(self, root):
        if root:
            print(root.val)
            self.preorder(root.left)
            self.preorder(root.right)
obj = AVL()
root = None
root = obj.insert(root, 1)
root = obj.insert(root, 2)
root = obj.insert(root, 3)
(obj.preorder(root))