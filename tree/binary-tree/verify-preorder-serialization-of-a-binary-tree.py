class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        q = []
        for node in preorder.split(','):
            q.append(node)
            while len(q) >= 3 and q[-1] != '#' and q[-2] == '#' and q[-3] == '#':
                if q[-1] == '#':
                    return False
                q.pop()
                q.pop()
                q.pop()
                q.append('#')
        return len(q) == 1 and q[0] == '#'


class Solution2:
    # 入度：有多少个节点指向它；
    # 出度：它指向多少个节点。
    # 我们知道在树（甚至图）中，所有节点的入度之和等于出度之和。可以根据这个特点判断输入序列是否为有效的！
    #
    # 在一棵二叉树中：
    # 每个空节点（ "#"）会提供 0 个出度和 1 个入度。
    # 每个非空节点会提供 2 个出度和 1 个入度（根节点的入度是 0）。
    # 我们只要把字符串遍历一次，每个节点都累加 diff = 出度 - 入度。在遍历到任何一个节点的时候，要求diff >= 0，原因是还没遍历到该节
    # 点的子节点，所以此时的出度应该大于等于入度。当所有节点遍历完成之后，整棵树的 diff == 0
    #
    # 这里解释一下为什么下面的代码中 diff 的初始化为 1。因为，我们加入一个非空节点时，都会对 diff 先减去 1（入度），再加上 2（出度）。但
    # 是由于根节点没有父节点，所以其入度为 0，出度为 2。因此 diff 初始化为 1，是为了在加入根节点的时候，diff 先减去 1（入度），再加上 2
    # （出度），此时 diff 正好应该是2.
    def isValidSerialization(self, preorder: str) -> bool:
        diff = 1
        for node in preorder.split(','):
            diff -= 1
            if diff < 0:
                return False
            if node != '#':
                diff += 2
        return diff == 0
