import numpy as np


class CellLocation:
    def __init__(self, val, row_idx, col_idx, distance=None):
        self.val = val
        self.row_idx = row_idx
        self.col_idx = col_idx
        self.distance = distance
        self.children = []


class Solution(object):

    def search(self, forest, tree_height, root_node):
        print('.............................................')

        print('({},{}) S{} D{}'.format(root_node.row_idx, root_node.col_idx, forest[root_node.row_idx, root_node.col_idx], tree_height))
        visited = np.zeros(forest.shape, dtype=np.bool)

        cell_loc = self.bfs(
            root_node=root_node, tree_height=tree_height, visited=visited,
        )

        return cell_loc

    def build_graph(self, forest):

        row_idx = 0
        col_idx = 0

        nodes_map = {}
        queue = []
        cell_loc = CellLocation(val=forest[row_idx, col_idx], row_idx=row_idx, col_idx=col_idx)
        nodes_map[(cell_loc.row_idx, cell_loc.col_idx)] = cell_loc
        queue.append(cell_loc)
        del row_idx, col_idx, cell_loc

        while queue:
            cell_loc = queue.pop(0)

            move_choices = [
                (cell_loc.row_idx-1, cell_loc.col_idx), (cell_loc.row_idx+1, cell_loc.col_idx),
                (cell_loc.row_idx, cell_loc.col_idx-1), (cell_loc.row_idx, cell_loc.col_idx+1),
            ]

            for curr_move in move_choices:

                if (0 <= curr_move[0] < forest.shape[0]) and (0 <= curr_move[1] < forest.shape[1]):

                    # obstacle
                    if forest[curr_move[0], curr_move[1]] == 0:
                        continue

                    if curr_move not in nodes_map:
                        curr_neighbor_cell_loc = CellLocation(
                            val=forest[curr_move[0], curr_move[1]],
                            row_idx=curr_move[0], col_idx=curr_move[1],
                        )
                        nodes_map[curr_move] = curr_neighbor_cell_loc
                        queue.append(curr_neighbor_cell_loc)
                    else:
                        curr_neighbor_cell_loc = nodes_map[curr_move]

                    cell_loc.children.append(curr_neighbor_cell_loc)
                    del curr_neighbor_cell_loc

        return nodes_map

    def bfs(self, root_node, tree_height, visited):
        assert not visited[root_node.row_idx, root_node.col_idx],\
            'revisit [{}, {}]'.format(root_node.row_idx, root_node.col_idx)

        queue = []
        visited[root_node.row_idx, root_node.col_idx] = True
        root_node.distance = 0
        queue.append(root_node)
        del root_node

        while queue:
            cell_loc = queue.pop(0)

            if cell_loc.val == tree_height:
                return cell_loc
            else:
                for curr_child in cell_loc.children:

                    # visited
                    if visited[curr_child.row_idx, curr_child.col_idx]:
                        continue

                    visited[curr_child.row_idx, curr_child.col_idx] = True

                    curr_child.distance = cell_loc.distance+1
                    queue.append(curr_child)

        return None

    def dfs_search(self, forest, row_idx, col_idx, tree_height, distance, visited):
        assert not visited[row_idx, col_idx], 'revisit [{}, {}]'.format(row_idx, col_idx)
        assert forest[row_idx, col_idx] != 0, 'obstacle [{}, {}]'.format(row_idx, col_idx)
        visited[row_idx, col_idx] = True
        if forest[row_idx, col_idx] == tree_height:
            return distance, (row_idx, col_idx)

        min_distance = None
        tree_location = None
        move_choices = [
            (row_idx-1, col_idx), (row_idx+1, col_idx),
            (row_idx, col_idx-1), (row_idx, col_idx+1),
        ]

        # print(move_choices)
        for curr_move in move_choices:

            if (0 <= curr_move[0] < forest.shape[0]) and (0 <= curr_move[1] < forest.shape[1]):
                if forest[curr_move[0], curr_move[1]] == 0:
                    continue

                if visited[curr_move[0], curr_move[1]]:
                    continue

                curr_distance, curr_tree_location = self._search(
                    forest=forest, row_idx=curr_move[0], col_idx=curr_move[1],
                    tree_height=tree_height, distance=distance+1,
                    visited=visited,
                )

                if curr_distance is None:
                    assert curr_tree_location is None
                    continue
                else:
                    print('O({},{})  M{}, {}'.format(row_idx, col_idx, curr_move, curr_distance))
                    if min_distance is None:
                        min_distance = curr_distance
                    else:
                        min_distance = min(min_distance, curr_distance)

                    if tree_location is None:
                        tree_location = curr_tree_location
                    else:
                        assert tree_location == curr_tree_location

        return min_distance, tree_location

    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        if not forest:
            return 0

        forest = np.array(forest)
        print(forest)

        if forest[0, 0] == 0:
            return -1

        tree_heights = forest.flatten()
        trees_idx = np.where(tree_heights > 1)[0]
        tree_heights = tree_heights[trees_idx]
        del trees_idx
        tree_heights.sort()
        print(tree_heights)

        print(forest.shape)
        print(tree_heights.size)

        nodes_map = self.build_graph(forest=forest)
        print('built graph')

        row_idx = 0
        col_idx = 0
        distance = 0
        for curr_tree_height in tree_heights:
            curr_node = nodes_map[(row_idx, col_idx)]
            cell_loc_obj = self.search(forest, tree_height=curr_tree_height, root_node=curr_node)
            if cell_loc_obj is None:
                return -1
            else:
                distance += cell_loc_obj.distance
                row_idx = cell_loc_obj.row_idx
                col_idx = cell_loc_obj.col_idx

        return distance



