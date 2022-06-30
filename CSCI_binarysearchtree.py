class Binary_Search_Tree:

  class __BST_Node:

    def __init__(self, value):
      self.value = value
      self.left = None
      self.right = None
      self.height = 1

  def __init__(self):
    self.__root = None

# insert method
  def insert_element(self, value):
    self.__root = self.__insert(value, self.__root)

  def __insert(self, value, subroot):
    if subroot is not None and value == subroot.value:
      raise ValueError
    if subroot is None:
      subroot = self.__BST_Node(value)
    else:
      if value < subroot.value:
        subroot.left = self.__insert(value, subroot.left)
      if value > subroot.value:
        subroot.right = self.__insert(value, subroot.right)
    subroot.height = self.__height(subroot)
    return self.__balance(subroot)

# remove method
  def remove_element(self, value):
    self.__root = self.__remove(value, self.__root)

  def __remove(self, value, subroot):
    if subroot is None:
      raise ValueError
    if value < subroot.value:
      subroot.left = self.__remove(value, subroot.left)
    if value > subroot.value:
      subroot.right = self.__remove(value, subroot.right)
    elif value == subroot.value:
      if subroot.left is None and subroot.right is None:
        subroot = None
        return subroot
      elif subroot.left is None and subroot.right is not None:
        keeper = subroot.right
        subroot = None
        return keeper
      elif subroot.left is not None and subroot.right is None:
        keeper = subroot.left
        subroot = None
        return keeper
      elif subroot.left is not None and subroot.right is not None:
        keeper = self.__minNode(subroot.right)
        subroot.value = keeper.value
        subroot.right = self.__remove(keeper.value, subroot.right)
    subroot.height = self.__height(subroot)
    return self.__balance(subroot)

  def __minNode(self, subroot):
    cur = subroot
    while cur.left is not None:
      cur = cur.left
    return cur

# inorder method
  def in_order(self):
    if self.__root is None:
      return "[ ]"
    else:
      string = "[ " + self.__in_order(self.__root) + " ]"
      return string

  def __in_order(self, subroot):
    if subroot.left is None and subroot.right is None:
      return str(subroot.value)
    elif subroot.left is None and subroot.right is not None:
      return str(subroot.value) + ", " + self.__in_order(subroot.right)
    elif subroot.left is not None and subroot.right is None:
      return self.__in_order(subroot.left) + ", " + str(subroot.value)
    elif subroot.left is not None and subroot.right is not None:
      return self.__in_order(subroot.left) + ", " + str(subroot.value) + ", " + self.__in_order(subroot.right)

# preorder method
  def pre_order(self):
    if self.__root is None:
      return "[ ]"
    else:
      string = "[ " + self.__pre_order(self.__root) + " ]"
      return string

  def __pre_order(self, subroot):
    if subroot.left is None and subroot.right is None:
      return str(subroot.value)
    elif subroot.left is None and subroot.right is not None:
      return str(subroot.value) + ", " + self.__pre_order(subroot.right)
    elif subroot.left is not None and subroot.right is None:
      return str(subroot.value) + ", " + self.__pre_order(subroot.left)
    elif subroot.left is not None and subroot.right is not None:
      return str(subroot.value) + ", " + self.__pre_order(subroot.left) + ", " + self.__pre_order(subroot.right)

# postorder method
  def post_order(self):
    if self.__root is None:
      return "[ ]"
    else:
      string = "[ " + self.__post_order(self.__root) + " ]"
      return string

  def __post_order(self, subroot):
    if subroot.left is None and subroot.right is None:
      return str(subroot.value)
    elif subroot.left is None and subroot.right is not None:
      return self.__post_order(subroot.right) + ", " + str(subroot.value)
    elif subroot.left is not None and subroot.right is None:
      return self.__post_order(subroot.left) + ", " + str(subroot.value)
    elif subroot.left is not None and subroot.right is not None:
      return self.__post_order(subroot.left) + ", " + self.__post_order(subroot.right) + ", " + str(subroot.value)

# height method
  def get_height(self):
    if self.__root is None:
      return 0
    else:
      height = self.__height(self.__root)
      return height

  def __height(self, subroot):
    if subroot.left is None and subroot.right is None:
      return 1
    elif subroot.left is None and subroot.right is not None:
      return subroot.right.height + 1
    elif subroot.left is not None and subroot.right is None:
      return subroot.left.height + 1
    elif subroot.left is not None and subroot.right is not None:
      return 1 + max(subroot.left.height, subroot.right.height)

  def __str__(self):
    return self.in_order()

# balance method
  def __balance(self, subroot):
    root_balance = self.__get_balance(subroot)
    left_balance = self.__get_balance(subroot.left)
    right_balance = self.__get_balance(subroot.right)
    if root_balance == 2 and right_balance >= 0:
      return self.__rotate_left(subroot)
    if root_balance == -2 and left_balance <= 0:
      return self.__rotate_right(subroot)
    if root_balance == 2 and right_balance <= 0:
      subroot.right = self.__rotate_right(subroot.right)
      return self.__rotate_left(subroot)
    if root_balance == -2 and left_balance >= 0:
      subroot.left = self.__rotate_left(subroot.left)
      return self.__rotate_right(subroot)
    return subroot

# helper methods left and right
  def __rotate_left(self, subroot):
    new_root = subroot.right
    floater = new_root.left
    new_root.left = subroot
    subroot.right = floater
    subroot.height = self.__height(subroot)
    new_root.height = self.__height(new_root)
    return new_root

  def __rotate_right(self, subroot):
    new_root = subroot.left
    floater = new_root.right
    new_root.right = subroot
    subroot.left = floater
    subroot.height = self.__height(subroot)
    new_root.height = self.__height(new_root)
    return new_root

  def __get_balance(self, subroot):
    if subroot is None:
      return 0
    if subroot.left is None and subroot.right is None:
      return 0
    elif subroot.left is None and subroot.right is not None:
      return (subroot.right.height)
    elif subroot.left is not None and subroot.right is None:
      return (0 - subroot.left.height)
    elif subroot.left is not None and subroot.right is not None:
      return (subroot.right.height - subroot.left.height)

# to list method
  def to_list(self):
    if self.__root is None:
      empty_list = []
      return empty_list
    else:
      return self.__list(self.__root)

  def __list(self, subroot):
    my_list = []
    if subroot.left is not None:
      for i in self.__list(subroot.left):
        my_list.append(i)
    my_list.append(subroot.value)
    if subroot.right is not None:
      for i in self.__list(subroot.right):
        my_list.append(i)
    return my_list

#if __name__ == '__main__':
#unit tests make the main section unnecessary.
#pass

