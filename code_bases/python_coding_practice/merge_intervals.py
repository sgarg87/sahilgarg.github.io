class TreeNode:
    def __init__(self, start_time, end_time):
        assert start_time <= end_time
        self.start_time = start_time
        self.end_time = end_time
        self.left = None
        self.right = None


class Solution(object):

    def update_subtrees_for_changed_root_node(self, root_node):
        if (root_node.left is not None) and (root_node.left.end_time >= root_node.start_time):
            raise NotImplemented

    def insert_interval(self, root_node, start_time, end_time):
        while True:
            # left subtree
            if end_time < root_node.start_time:
                if root_node.left is not None:
                    root_node = root_node.left
                    continue
                else:
                    root_node.left = TreeNode(start_time=start_time, end_time=end_time)
                    break
            # right subtree
            elif start_time > root_node.end_time:
                if root_node.right is not None:
                    root_node = root_node.right
                    continue
                else:
                    root_node.right = TreeNode(start_time=start_time, end_time=end_time)
                    break
            # merge the intervals
            else:
                root_node.start_time = min(start_time, root_node.start_time)
                root_node.end_time = max(end_time, root_node.end_time)
                print(root_node.start_time, root_node.end_time)
                self.update_subtrees_for_changed_root_node(root_node=root_node)
                break

    def bfs(self, root_node):
        intervals_list = []
        queue = [root_node]
        del root_node

        while queue:
            curr_node = queue.pop(0)
            intervals_list.append([curr_node.start_time, curr_node.end_time])

            if curr_node.left is not None:
                queue.append(curr_node.left)

            if curr_node.right is not None:
                queue.append(curr_node.right)

        return intervals_list

    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []

        root_node = None
        for curr_interval in intervals:
            if root_node is None:
                root_node = TreeNode(
                    start_time=curr_interval[0],
                    end_time=curr_interval[1],
                )
            else:
                self.insert_interval(
                    root_node=root_node,
                    start_time=curr_interval[0], end_time=curr_interval[1],
                )

        new_intervals_list = self.bfs(root_node=root_node)
        return new_intervals_list
