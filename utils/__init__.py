import ast

from utils.TreeNode import TreeNode


def create_tree(root):
    if isinstance(root, str):
        root = ast.literal_eval(root.replace('null', 'None'))
    index = 1
    layer = [root[0]]
    root_node = None
    sub_node = []
    while layer:
        # print(layer)
        if root_node is None:
            root_node = TreeNode(val=layer[0])
            sub_node.append(root_node)
        else:
            sub_node_node = []
            for i, a in enumerate(sub_node):
                left_value, right_value = layer[i * 2:i * 2 + 2]
                if left_value is None:
                    sub_node_node.append(left_value)
                else:
                    a.left = TreeNode(val=left_value)
                    sub_node_node.append(a.left)
                if right_value is None:
                    sub_node_node.append(right_value)
                else:
                    a.right = TreeNode(val=right_value)
                    sub_node_node.append(a.right)
            sub_node = sub_node_node
        layer = root[pow(2, index) - 1:pow(2, index + 1) - 1]
        index += 1
    return root_node


if __name__ == '__main__':
    # create_tree('[1,null,2]')
    create_tree('[3,9,20,null,null,15,7]')
