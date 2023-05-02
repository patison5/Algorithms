# Print all the nodes at the distance of K in Binary Tree
# Необходимо найти все ноды удаленные на расстояние К от заданной вершины. 
# Например, для вершины 5 с расстоянием 2 результатом будут ноды [7, 4, 1]
# Для вершины 8 с расстоянием 2: [3, 0]
# Для вершины 3 с расстоянием 3: [7, 4]

#          Example
#             3
#     5               1
# 6       2       0       8
#       7   4  
# start_node_value = 5
# rootNode = 3
# distance = 2
# result = [1, 7, 4]

# // MARK: - Classes --------------------------------------------------------------------------

class TreeNode:
    def __init__(self, value=0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right


# // MARK: - Public Variables --------------------------------------------------------------------------

parent_nodes_map = {}
already_visited_nodes = []
start_node = None

# // MARK: - Public Methods --------------------------------------------------------------------------

def CreateParentMap(node, nodeValue):
    """
    :type node: TreeNode
    :rtype: None
    """
    if node is None:
        return

    if node.value == nodeValue:
        global start_node
        start_node = node

    if not node.left is None:
        parent_nodes_map[node.left] = node

    if not node.right is None:
        parent_nodes_map[node.right] = node

    CreateParentMap(node.left, nodeValue)
    CreateParentMap(node.right, nodeValue)


def GetNodeInDistance(node, distance, current_distance, current_list):
    if node is None:
        return

    if node in already_visited_nodes:
        return
    
    already_visited_nodes.append(node)

    if current_distance == distance:
        current_list.append(node)
    GetNodeInDistance(node.left, distance, current_distance + 1, current_list)
    GetNodeInDistance(node.right, distance, current_distance + 1, current_list)
    if node in parent_nodes_map:
        parent = parent_nodes_map[node]
        GetNodeInDistance(parent, distance, current_distance + 1, current_list)
    return current_list


def GetAllNodesInDistance(rootNode, start_node_value, distance):
    """
    :type rootNode: TreeNode
    :type distance: TreeNode
    :rtype: [TreeNode]
    """
    CreateParentMap(rootNode, start_node_value)
    return GetNodeInDistance(start_node, distance, 0, [])


# // MARK: - Tests --------------------------------------------------------------------------

treeNode4 = TreeNode(4)
treeNode7 = TreeNode(7)
treeNode8 = TreeNode(8)
treeNode0 = TreeNode(0)
treeNode2 = TreeNode(2, treeNode7, treeNode4)
treeNode6 = TreeNode(6)
treeNode5 = TreeNode(5, treeNode6, treeNode2)
treeNode1 = TreeNode(1, treeNode0, treeNode8)
treeNode3 = TreeNode(3, treeNode5, treeNode1)
root = treeNode3

resultNodes = GetAllNodesInDistance(root, 3, 3)
resultValues = [el.value for el in resultNodes]
print(resultValues)