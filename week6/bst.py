class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert(root, key):
    if root is None:
        return Node(key)

    if root.val == key:
        return root

    if root.val < key:
        root.right = insert(root.right, key)

    else:
        root.left = insert(root.left, key)


    return root



def inorder(root, res):
    if not root:
        return None

    inorder(root.left, res)
    res.append(root.val)
    inorder(root.right, res)


def tree_min_list(root, less):
    if not root:
        return 

    if root.left:
        tree_min_list(root.left, less)


    less.append(root.val)

    
def tree_min(root):
    if not root:
        return None

    while root.left:
        root = root.left


    return root.val


def successor(root):
    if not root:
        return None

    if root.right:
        return tree_min(root.right)

    
    successor_node = None
    cur_node = root


    while cur_node:
        if root.val < cur_node.val:
            successor_node = cur_node
            cur_node = cur_node.left

        elif root.val > cur_node.val:
            cur_node = cur_node.right

        else:
            break # found the node


    return successor_node.val


    

r = Node(15)
r = insert(r, 10)
r = insert(r, 18)
r = insert(r, 4)
r = insert(r, 11)
r = insert(r, 16)
r = insert(r, 20)
r = insert(r, 13)
res = []
inorder(r, res)
print(res)
less = []
tree_min_list(r, less)
print(less)

print(tree_min(r))



root = Node(15)
root = insert(root, 10)
root = insert(root, 18)
root = insert(root, 4)
root = insert(root, 11)
root = insert(root, 16)
root = insert(root, 20)
root = insert(root, 13)

node_10 = root.left
node_15 = root
node_18 = root.right
r = []
inorder(root, r)
print(r)
print(successor(node_15))