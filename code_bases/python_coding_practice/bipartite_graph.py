class Solution(object):
    def dfs_color(self, graph, node, node_colors):
        if not graph[node]:
            return False

        neighbor_node_color = 1-node_colors[node]

        for neighbor in graph[node]:
            if neighbor not in node_colors:
                node_colors[neighbor] = neighbor_node_color
                is_bipartite = self.dfs_color(graph, neighbor, node_colors)
                if not is_bipartite:
                    return False
            elif node_colors[neighbor] != neighbor_node_color:
                return False
            else:
                pass

        return True

    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        # number of nodes
        n = len(graph)
        # two colors, 0 and 1
        for curr_node in range(n):
            if not graph[curr_node]:
                return False
            else:
                node_colors = {curr_node: 0}
                return self.dfs_color(graph=graph, node=curr_node, node_colors=node_colors)

