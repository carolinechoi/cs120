#################
#               #
# Problem Set 0 #
#               #
#################


#
# Setup
#
class BinaryTree:
    def __init__(self, root):
        self.root: BTvertex = root
 
class BTvertex:
    def __init__(self, key):
        self.parent: BTvertex = None
        self.left: BTvertex = None
        self.right: BTvertex = None
        self.key: int = key
        self.size: int = None

#
# Problem 1a
#

# Input: BTvertex v, the root of a BinaryTree of size n
# Output: Up to you
# Side effect: sets the size of each vertex n in the
# ... tree rooted at vertex v to the size of that subtree
# Runtime: O(n)
def calculate_sizes(v):
    if v == None:
        return 0
    elif v.left == v.right == None:
        v.size = 1
    else:
        v.size = calculate_sizes(v.left) + calculate_sizes(v.right) + 1
    return v.size 

#
# Problem 1c
#

# Input: BTvertex r, the root of a size-augmented BinaryTree T
# ... of size n and height h
# Output: A BTvertex that, if removed from the tree, would result
# ... in disjoint trees that all have at most n/2 vertices
# Runtime: O(h)
def find_vertex(r): 

    ## STAGE 1: identifying phi(r)  
    def calculate_phi(k):          
        phi_list = []

        if k.left is not None:
            phi_list.append(k.left.size) 
        
        if k.right is not None:
            phi_list.append(k.right.size)

        phi_list.append(r.size - k.size)

        return max(phi_list)       

    ## STAGE 2: comparing phi(r) to phi(r.left) and phi(r.right)
    def compare_phi(m):
        phi_coll = []

        phi_coll.append(calculate_phi(m))

        if m.left is not None:
            left_phi = calculate_phi(m.left)
            phi_coll.append(left_phi)
        else: 
            left_phi = None 

        if m.right is not None:
            right_phi = calculate_phi(m.right)
            phi_coll.append(right_phi)
        else: 
            right_phi = None

        phi_coll.sort()

        if left_phi == phi_coll[0]:
            return compare_phi(m.left)
        elif right_phi == phi_coll[0]:
            return compare_phi(m.right)
        else:
            return m
        
    return compare_phi(r)