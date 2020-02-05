import collections


class Solution(object):
    def order_chars(self, w1, w2):
        len_w1 = len(w1)
        len_w2 = len(w2)
        n = min(len_w1, len_w2)
        for j in range(n):
            if w1[j] == w2[j]:
                continue
            else:
                return [w1[j], w2[j]]
        return None

    def topological_sort(self, node, node_children_map, chars_stack, visited, under_exploration):

        assert node not in visited
        visited.add(node)
        under_exploration.add(node)

        for curr_child in node_children_map[node]:
            if curr_child not in visited:
                is_cycle = self.topological_sort(
                    node=curr_child, node_children_map=node_children_map,
                    chars_stack=chars_stack, visited=visited,
                    under_exploration=under_exploration,
                )
                if is_cycle:
                    return True
            else:
                if curr_child in under_exploration:
                    return True

        chars_stack.append(node)
        under_exploration.remove(node)
        return False

    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words = [x for x in words if x.strip()]
        if not words:
            return ""

        nodes = set()
        for w in words:
            for c in w:
                nodes.add(c)
        nodes = list(nodes)

        node_children_map = collections.defaultdict(set)
        n = len(words)
        for i in xrange(n-1):
            w1 = words[i]
            w2 = words[i+1]
            edge = self.order_chars(w1=w1, w2=w2)
            if edge is None:
                continue
            node_children_map[edge[0]].add(edge[1])

        chars_stack = list()
        visited = set()
        under_exploration = set()
        for curr_node in nodes:
            if curr_node not in visited:
                is_cycle = self.topological_sort(curr_node, node_children_map, chars_stack, visited, under_exploration)
                if is_cycle:
                    return ""

        lexical_order = ''
        while chars_stack:
            lexical_order += chars_stack.pop()

        return lexical_order

