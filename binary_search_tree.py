class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def print_tree_structure(root, space=0, num_spaces=5):
    if root is None:
        return
    space += num_spaces
    print_tree_structure(root.right, space)
    print()
    for i in range(num_spaces, space):
        print(end=" ")
    print(root.val)
    print_tree_structure(root.left, space)

# Ödev dizisi
elemanlar = [7, 5, 1, 8, 3, 6, 0, 9, 4, 2]
root = Node(elemanlar[0])

for eleman in elemanlar[1:]:
    insert(root, eleman)

print("Binary Search Tree Yapısı (Yatay Görünüm):")
print("-" * 45)
print_tree_structure(root)