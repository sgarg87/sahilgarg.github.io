import collections


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        level_val_count_map = collections.defaultdict(list)

        queue = list()
        queue.append((root, 0))
        del root

        while queue:
            node, depth = queue.pop(0)
            if not level_val_count_map[depth]:
                level_val_count_map[depth] = [0, 0]

            level_val_count_map[depth][0] += node.val
            level_val_count_map[depth][1] += 1

            if node.left is not None:
                queue.append((node.left, depth+1))

            if node.right is not None:
                queue.append((node.right, depth+1))

            del node, depth

        averages = []
        for depth in sorted(level_val_count_map.keys()):
            average = float(level_val_count_map[depth][0])/level_val_count_map[depth][1]
            averages.append(average)

        return averages
