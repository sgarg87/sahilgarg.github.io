# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        print('Serialize')
        if root is None:
            return '[]'

        queue = [root]
        del root

        serialize_str = ''
        while queue:
            curr_node = queue.pop(0)

            if curr_node is None:
                print(curr_node)
                serialize_str += 'null,'
            else:
                print(curr_node.val)
                serialize_str += str(curr_node.val)+','
                queue.append(curr_node.left)
                queue.append(curr_node.right)

        serialize_str = '['+serialize_str+']'

        print(serialize_str)

        return serialize_str

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        print('Deserialize ...')
        print(data)

        if data == '[]':
            return None

        data = data.strip('[')
        data = data.strip(']')
        data = data.split(',')
        print(data)

        data_list = []
        for x in data:
            x = x.strip()
            if not x:
                continue
            if x == 'null':
                data_list.append(None)
            else:
                data_list.append(int(x))
        print(data_list)
        del data

        root_val = data_list.pop(0)
        if root_val is None:
            return None

        root_node = TreeNode(root_val)
        del root_val
        queue_of_nodes = [root_node]

        while queue_of_nodes:
            curr_node = queue_of_nodes.pop(0)
            assert curr_node is not None
            print(curr_node.val)

            left_val = data_list.pop(0)
            if left_val is not None:
                left_node = TreeNode(left_val)
                curr_node.left = left_node
                queue_of_nodes.append(left_node)
                del left_node
            del left_val

            right_val = data_list.pop(0)
            if right_val is not None:
                right_node = TreeNode(right_val)
                curr_node.right = right_node
                queue_of_nodes.append(right_node)
                del right_node
            del right_val

            del curr_node

        assert not data_list

        print('returning', root_node.val)

        return root_node


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
