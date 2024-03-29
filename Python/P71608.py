class Tree:
    def __init__(self, x):
        self.rt = x
        self.child = []

    def add_child(self, a):
        self.child.append(a)

    def root(self):
        return self.rt

    def ith_child(self, ith):
        return self.child[ith]

    def num_children(self):
        return len(self.child)

class Pre(Tree):
    def preorder(self):
        preorderList = []
        for ch in self.child:
            preorderList = preorderList + (ch.preorder())

        return [self.rt] + preorderList

