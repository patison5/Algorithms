# 222. [Medium] Count Complete Tree Nodes

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def countNodes(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    current_left_node = root
    left_height = 0
    while current_left_node:
    	current_left_node = current_left_node.left
    	left_height += 1

    current_right_node = root
    right_height = 0
    while current_right_node:
    	current_right_node = current_right_node.right
    	right_height += 1

    if left_height == right_height:
    	return 2 ** left_height - 1

    return 1 + countNodes(root.left) + countNodes(root.right)


t5 = TreeNode(5)
t4 = TreeNode(4)
t3 = TreeNode(3, t6)
t2 = TreeNode(2, t4, t5)
t1 = TreeNode(1, t2, t3)
print(countNodes(t1))