# 100. [Easy] Same Tree

def isSameTree(p, q):        
    if p is None or q is None:
        return p == q
    return dfs(p, q)
    
def dfs( 
    q, 
    p
):

    if q is None or p is None:
        return q == p

    left_part = dfs(q.left, p.left)
    right_part = dfs(q.right, p.right)

    return left_part and right_part and q.val == p.val
    


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



l3 = TreeNode(3)
l2 = TreeNode(2)
l1 = TreeNode(1, l2, l3)

print(isSameTree(None, None))