class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f'left:{"node" if self.left else None} | right:{"node" if self.right else None} | val:{self.val}'

    def __repr__(self):
        return self.__str__()
