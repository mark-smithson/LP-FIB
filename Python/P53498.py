class Tree:
    def __init__(self, x):
        self.rt = x
        self.child = []

    def addChild(self, a):
        self.child.append(a)

    def root(self):
        return self.rt

    def ithChild(self, ith):
        return self.child[ith]

    def num_children(self):
        return len(self.child)

    def __iter__(self):
        yield self.rt
        rec = self.child

        for ch in rec:
            #amplitude
            for sub_ch in range(0, ch.num_children()):
                rec.append(ch.ithChild(sub_ch))

            yield ch.root()

class Pre(Tree):
    def preorder(self):
        preorderList = []
        for ch in self.child:
            preorderList = preorderList + (ch.preorder())

        return [self.rt] + preorderList
