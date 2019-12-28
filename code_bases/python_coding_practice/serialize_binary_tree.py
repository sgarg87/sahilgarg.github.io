# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def _deserialize(self, data_list):
        queue_node = []
        root_val = data_list.pop(0)
        root_node = TreeNode(root_val)
        if root_val is None:
            assert not data_list
            return None
        else:
            left_val = data_list.pop(0)
            if left_val is not None:
                left_node = TreeNode(left_val)
        raise NotImplementedError

    def _serialize(self, root, serialize_str=''):
        serialize_str += str(root.val)+','

        if root.left is None:
            serialize_str += 'null,'
        else:
            serialize_str += str(root.left.val)+','

        if root.right is None:
            serialize_str += 'null,'
        else:
            serialize_str += str(root.right.val)+','

        if root.left is not None:
            serialize_str = self._serialize(root=root.left, serialize_str=serialize_str)

        if root.right is not None:
            serialize_str = self._serialize(root=root.right, serialize_str=serialize_str)

        return serialize_str

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        serialize_str = self._serialize(root=root)
        serialize_str = '['+serialize_str+']'

        return serialize_str

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
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

        root_node = self._deserialize(data_list=data_list)

        return root_node
