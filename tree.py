'''
File: tree.py
Author: Pri Vaghela (CSC 120, 4:00 pm)
Description: The program is to create the TreeNode class that gets imported in 
phylo.py.
'''

class TreeNode:
    '''
    The class TreeNode is a representation of a node in a binary tree. 
    '''
    def __init__(self, name):
        '''
        initalizing the name (id), the left node, the right node and a set of 
        ids. 
        '''
        self._id = name
        self._left = None
        self._right = None
        self._set_id = set()

    def get_left(self):
        '''
        The method get_left returns the left node.
        '''
        return self._left

    def get_right(self):
        '''
        The method get_right returns the right node.
        '''
        return self._right

    def set_left(self, left):
        '''
        The method set_left sets the left node.
        left - this parameter takes in the left node value
        '''
        self._left = left

    def set_right(self, right):
        '''
        The method set_right sets the right node.
        right - this parameter takes in the right node value
        '''
        self._right = right

    def get_id(self):
        '''
        The method get_id returns the ID associated with a node.
        '''
        return self._id

    def set_id(self):
        '''
        The method set_id returns the set of IDs associated with a node.
        '''
        return self._set_id

    def is_leaf(self):
        '''
        The method is_leaf returns a boolean value indicating whether a node is 
        a leaf.
        '''
        return self._left is None and self._right is None

    def add_id(self, id):
        '''
        The method add_id adds an ID to the set of IDs associated with a node.
        id - this paramter takes in an id to be added
        '''
        self._set_id.add(id)

    def __str__(self):
        '''
        The method __str__ returns a string representation of a node.
        '''
        if self.is_leaf():
            return self.get_id()
        else:
            return \
                "({}, {})".format(str(self.get_left()), str(self.get_right()))
        