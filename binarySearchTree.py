class node:
    def __init__(self,value=None):
        self.value=value
        self.left_child=None
        self.right_child=None

class binary_search_tree:
    def __init__(self):
        self.root=None
   
    #insert element
    def insert(self,value):
        if self.root==None:
            self.root=node(value)
        else:
            self._insert(value,self.root)

    def _insert(self,value,current_node):
        if value<current_node.value:
            if current_node.left_child==None:
                current_node.left_child=node(value)
            else:
                self._insert(value,current_node.left_child)
        elif value>current_node.value:
            if current_node.right_child==None:
                current_node.right_child=node(value)
            else:
                self._insert(value,current_node.right_child)
        else:
            print("Value already in tree")

    #print tree
    def print_tree(self):
        if self.root!=None:
            self._print_tree(self.root)

    def _print_tree(self,current_node):
        if current_node!=None:
            self._print_tree(current_node.left_child)
            print(str(current_node.value))
            self._print_tree(current_node.right_child)
    
    #get hight of tree
    def height(self):
        if self.root!=None:
            return self._height(self.root,0)
        else:
            return 0

    def _height(self,current_node,current_height):
        if current_node==None: return current_height
        left_height=self._height(current_node.left_child,current_height+1)
        right_height = self._height(current_node.right_child, current_height + 1)
        return max(left_height,right_height)

    #search element
    def search(self,value):
        if self.root!=None:
            return self._search(value,self.root)
        else:
            return False
   
    def _search(self,value,current_node):
        if value==current_node.value:
            return True
        elif value<current_node.value and current_node.left_child!=None:
            return self._search(value,current_node.left_child)
        elif value>current_node.value and current_node.right_child!=None:
            return self._search(value,current_node.right_child)

        return False

def fill_tree(tree,num_elems=50,max_int=100):
    from random import randint

    for _ in range(num_elems):
        cur_ele=randint(0,max_int)
        tree.insert(cur_ele)
    return tree


tree= binary_search_tree()
#tree= fill_tree(tree)
tree.insert(5)
tree.insert(10)
tree.insert(25)
tree.insert(9)
tree.insert(30)
tree.insert(40)

tree.print_tree()
print("Tree height: "+str(tree.height()))

print(tree.search(10))
print(tree.search(100))

