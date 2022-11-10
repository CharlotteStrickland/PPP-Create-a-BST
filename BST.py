#Part 1: Create a BSTNode class
class BSTNode:
  def __init__(self, data = None, left = None, right = None):
    self.data = data
    self.left = left 
    self.right = right

  def __str__(self):
    return str(self, data)
  def __repr__(self) -> str:
    return str(self, data)



#Part 2: Create a BST class

class BST:
  def __init__(self, root = None) -> None:
    self.root = root
    self.content = []

  def __str__(self) -> str:
    if self.root == None:
      return "The tree is empty"
    else:
      self.output = ""
      self.print_tree(node=self.root)
      return self.output

  def __repr__(self) -> str:
    return BST.__str__(self)

  def print_tree(self, node, level=0):
    if node != None:
      self.print_tree(node.right, level + 1)
      self.output += ' ' * 4 * level + '-> ' + str(node.data) + ''
      self.print_tree(node.left, level + 1)

  def add(self, node):
    if type(node) != int and type(node) != BSTNode:
      raise ValueError("You must only use ints or BSTNodes here, special one")

    if type(node) == int:
      node = BSTNode(node)

    if node.data in self.content:
      return

    if self.root == None:
      self.root = node
      self.content.append(node.data)

    self.add_node(self.root, node)

  def add_node(self, cur_node, new_node):
    if new_node.data > cur_node.data:
      if cur_node.right == None:
        cur_node.right = new_node
        self.content.append(new_node.data)
        return
    else:
        self.add_node(new_node.data)
    else:
        if cur_node.left == None:

  

  #Part 3: Add functionality to your BST class

  def main():
  