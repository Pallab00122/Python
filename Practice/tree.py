class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BinaryTree:
    def __init__(self):
        self.root=None
    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.data, end="")
            self.inorder_traversal(node.right)
    def preorder_traversal(self, node):
        if node:
            print(node.data, end="")
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)
            
if __name__ == "__main__":
    print("Binary tree")
    bt=BinaryTree()
    bt.root=TreeNode(1)
    bt.root.left = TreeNode(2)
    bt.root.right = TreeNode(3)
    bt.root.left.left = TreeNode(4)
    bt.root.left.right = TreeNode(5)

print("Inorder Traversal:")
bt.inorder_traversal(bt.root) 
print("\nPreorder Traversal:")
bt.preorder_traversal(bt.root)