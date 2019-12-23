import numpy as np
import collections


class TreeNode:
    def __init__(self, val, parent=None, depth=0):
        self.val = val
        # only the parent from which the node is traversed in the graph
        self.neighbors = []
        self.parent = parent
        self.depth = depth


class Solution(object):

    def create_pattern(self, word, index):
        pattern = word[:index] + '*' + word[index+1:]
        return pattern

    def create_neighbors_dict_per_patterns_of_words(self, wordList):
        assert wordList.size >= 1
        # length should be same for all words
        k = len(wordList[0])
        patterns_map = collections.defaultdict(list)
        for curr_word in wordList:
            for curr_index in range(k):
                curr_pattern = self.create_pattern(word=curr_word, index=curr_index)
                patterns_map[curr_pattern].append(curr_word)
                del curr_pattern
        return patterns_map

    def build_graph(self, wordList, beginWord, endWord):
        word_len = len(wordList[0])

        patterns_map = self.create_neighbors_dict_per_patterns_of_words(wordList=wordList)

        word_node_map = {}
        queue_obj = collections.deque(maxlen=wordList.size)
        root_node = TreeNode(val=beginWord, depth=1)
        queue_obj.append(root_node)
        word_node_map[beginWord] = root_node
        end_node = None

        while queue_obj:
            curr_node = queue_obj.popleft()

            for curr_char_index in range(word_len):
                curr_pattern = self.create_pattern(word=curr_node.val, index=curr_char_index)
                neighboring_words = patterns_map[curr_pattern]

                neighbor_depth = curr_node.depth+1
                for curr_neighbor_word in neighboring_words:
                    if curr_neighbor_word not in word_node_map:
                        curr_neighbor_node = TreeNode(val=curr_neighbor_word, depth=neighbor_depth, parent=curr_node)
                        word_node_map[curr_neighbor_word] = curr_neighbor_node
                        queue_obj.append(curr_neighbor_node)
                    else:
                        curr_neighbor_node = word_node_map[curr_neighbor_word]
                    curr_node.neighbors.append(curr_neighbor_node)

                    if curr_neighbor_word == endWord:
                        if end_node is None:
                            end_node = curr_neighbor_node

        return root_node, end_node

    def dfs_recursive(self, root_node, end_word, traversed=None, traversed_len=0, min_traversal_len=100000):
        if traversed_len > (root_node.depth-1):
            return [], None

        if traversed_len >= min_traversal_len:
            return [], None

        # assert root_node is not None
        # print(min_traversal_len, root_node.val)

        if traversed is None:
            traversed = []

        # creating new list
        traversed = traversed + [root_node.val]
        traversed_len += 1

        if root_node.val == end_word:
            traversed_lists = [traversed]
        else:
            traversed_lists = []
            for curr_neighbor in root_node.neighbors:

                if curr_neighbor.val not in traversed:
                    curr_traversed_lists, curr_min_traversal_len = self.dfs_recursive(
                        root_node=curr_neighbor,
                        end_word=end_word,
                        traversed=traversed,
                        traversed_len=traversed_len,
                        min_traversal_len=min_traversal_len,
                    )

                    if curr_traversed_lists and (curr_min_traversal_len <= min_traversal_len):
                        if curr_min_traversal_len < min_traversal_len:
                            # reset the list
                            traversed_lists = curr_traversed_lists
                            min_traversal_len = curr_min_traversal_len
                        else:
                            traversed_lists += curr_traversed_lists

        return traversed_lists, min_traversal_len

    def retrieve_one_path_from_leaf_node_to_root_node(self, leaf_node, root_node):
        path = []
        curr_node = leaf_node
        while curr_node is not None:
            path.append(curr_node.val)
            if curr_node.parent is None:
                assert curr_node.val == root_node.val
            curr_node = curr_node.parent
        path.reverse()
        return path

    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return []

        wordList = np.array(wordList)
        print(wordList.size)

        root_node, end_node = self.build_graph(wordList=wordList, beginWord=beginWord, endWord=endWord)
        assert root_node is not None, 'begin word not found'
        if end_node is None:
            return []

        traversed_path = self.retrieve_one_path_from_leaf_node_to_root_node(
            leaf_node=end_node, root_node=root_node,
        )
        shortest_path_len_known = len(traversed_path)
        del traversed_path
        print(shortest_path_len_known)

        traversed_lists, _ = self.dfs_recursive(
            root_node=root_node, end_word=endWord, min_traversal_len=shortest_path_len_known,
        )

        return traversed_lists
