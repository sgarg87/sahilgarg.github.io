import collections


class Solution(object):
    def child_nodes(self, pid, ppid):
        parent_child_map = collections.defaultdict(list)
        for idx, parent_id in enumerate(ppid):
            child_id = pid[idx]
            parent_child_map[parent_id].append(child_id)
        return parent_child_map

    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        parent_child_map = self.child_nodes(pid=pid, ppid=ppid)

        all_kills = list()
        queue = list()
        queue.append(kill)
        del kill
        while queue:
            curr_p = queue.pop(0)
            curr_children = parent_child_map[curr_p]
            all_kills.append(curr_p)
            queue += curr_children
        return all_kills

