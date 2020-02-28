import sys
sys.path.append('../queue_and_stack')



class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        p = self
        if value < p.value:
            if p.left != None:
                p.left.insert(value)
            else:
                p.left = BinarySearchTree(value)
        else:
            if p.right != None:
                p.right.insert(value)
            else:
                p.right = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        elif target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False
    # Return the maximum value found in the tree
    def get_max(self):
        m = self.value
        if not self.right:
            return m
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.right:
            self.right.for_each(cb)
        if self.left:
            self.left.for_each(cb)
    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            self.in_order_print(node.left)
        print(node.value)
        if node.right: 
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    # def bft_print(self, node):
    #     q = Queue()
    #     q.enqueue(node)
    #     while q.len() > 0:
    #         t = q.dequeue()
    #         print(t.value)
    #         if t.left:
    #             q.enqueue(t.left)
    #         if t.right:
    #             q.enqueue(t.right)

    # # Print the value of every node, starting with the given node,
    # # in an iterative depth first traversal
    # def dft_print(self, node):
    #     s = Stack()
    #     s.push(node)
    #     while s.len() > 0:
    #         t = s.pop()
    #         print(t.value)
    #         if t.right:
    #             s.push(t.right)
    #         if t.left:
    #             s.push(t.left)


    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)
        if node.left:
            self.pre_order_dft(node.left)
        if node.right:
            self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left:
            self.post_order_dft(node.left)
        if node.right:
            self.post_order_dft(node.right)
        print(node.value)
