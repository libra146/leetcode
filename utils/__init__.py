import ast

from utils.TreeNode import TreeNode


def create_tree(node_list):
    if isinstance(node_list, str):
        node_list = ast.literal_eval(node_list.replace('null', 'None'))
    if not node_list:
        return TreeNode()
    if len(node_list) == 1:
        return TreeNode(node_list[0])
    index = 1
    root = TreeNode(node_list[0])
    q = [root]
    while q:
        if index >= len(node_list):
            break
        r = q.pop(0)
        r.left = TreeNode(val=node_list[index]) if node_list[index] else None
        index += 1
        if index >= len(node_list):
            break
        r.right = TreeNode(val=node_list[index]) if node_list[index] else None
        index += 1
        if r.left:
            q.append(r.left)
        if r.right:
            q.append(r.right)
    return root


if __name__ == '__main__':
    # create_tree('[1,null,2]')
    # print(create_tree('[3,9,20,null,null,15,7]'))
    # print(create_tree('[1,2,3,4,5,6,null,null,null,7,8]'))
    # print(create_tree('[1,3,2,null,6,4,5,null,null,null,null,8,7]'))
    print(create_tree('[1,null,2,2]'))
