class Node:
    def __init__(self, val):
        self.val = val
        self.parents = []


class Solution(object):
    def create_dependency_graph_from_prerequisites(self, prerequisites, numCourses):
        nodes_map = {}
        for curr_course in range(numCourses):
            nodes_map[curr_course] = Node(val=curr_course)

        for curr_prerequisite in prerequisites:

            curr_course_node = nodes_map[curr_prerequisite[0]]
            curr_course_dependency_node = nodes_map[curr_prerequisite[1]]

            assert curr_course_dependency_node not in curr_course_node.parents
            curr_course_node.parents.append(curr_course_dependency_node)

        return nodes_map

    def detect_cycle_with_dfs(self, nodes_map):
        under_exploration = set()
        visited = set()
        explored = set()

        for curr_course in nodes_map:
            curr_course_node = nodes_map[curr_course]
            if curr_course in visited:
                continue
            else:
                visited.add(curr_course)
            is_cycle, under_exploration, visited, explored = self._detect_cycle_with_dfs(
                curr_course_node=curr_course_node,
                under_exploration=under_exploration,
                visited=visited,
                explored=explored,
            )
            if is_cycle:
                return True

        return False

    def _detect_cycle_with_dfs(self, curr_course_node, under_exploration, visited, explored):

        if curr_course_node.val in under_exploration:
            return True, None, None, None
        else:
            under_exploration.add(curr_course_node.val)

        for curr_parent_node in curr_course_node.parents:
            visited.add(curr_parent_node.val)
            is_cycle, under_exploration, visited, explored = self._detect_cycle_with_dfs(
                curr_course_node=curr_parent_node,
                under_exploration=under_exploration,
                visited=visited,
                explored=explored,
            )
            if is_cycle:
                return True, None, None, None

        under_exploration.remove(curr_course_node.val)
        explored.add(curr_course_node.val)

        return False, under_exploration, visited, explored

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        course_nodes_map = self.create_dependency_graph_from_prerequisites(
            prerequisites=prerequisites, numCourses=numCourses,
        )

        is_cycle = self.detect_cycle_with_dfs(
            nodes_map=course_nodes_map,
        )
        return not is_cycle
