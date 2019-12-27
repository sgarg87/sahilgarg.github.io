class Node:
    def __init__(self):
        self.char_nodes_map = {}
        self.is_word_end = False


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root_node = Node()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        word_len = len(word)
        curr_trie_node = self.root_node
        for curr_char_idx, curr_char in enumerate(word):
            if curr_char not in curr_trie_node.char_nodes_map:
                new_trie_node = Node()
                curr_trie_node.char_nodes_map[curr_char] = new_trie_node
                del new_trie_node
            if curr_char_idx == (word_len-1):
                curr_trie_node.char_nodes_map[curr_char].is_word_end = True
            curr_trie_node = curr_trie_node.char_nodes_map[curr_char]

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        word_len = len(word)
        curr_trie_node = self.root_node
        for curr_char_idx, curr_char in enumerate(word):
            if curr_char not in curr_trie_node.char_nodes_map:
                return False
            else:
                if curr_char_idx == (word_len-1):
                    return curr_trie_node.char_nodes_map[curr_char].is_word_end
                else:
                    curr_trie_node = curr_trie_node.char_nodes_map[curr_char]
        raise AssertionError

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        prefix_len = len(prefix)
        curr_trie_node = self.root_node
        for curr_char_idx, curr_char in enumerate(prefix):
            if curr_char not in curr_trie_node.char_nodes_map:
                return False
            else:
                if curr_char_idx == (prefix_len-1):
                    return True
                else:
                    curr_trie_node = curr_trie_node.char_nodes_map[curr_char]
        raise AssertionError


if __name__ == '__main__':
    obj = Trie()

    obj.insert('abcd')
    obj.insert('abce')
    obj.insert('abcde')
    obj.insert('abf')
    obj.insert('fba')

    print(obj.search('abcd'))
    print(obj.search('abce'))
    print(obj.search('abcde'))
    print(obj.search('abf'))
    print(obj.search('fba'))

    print(obj.search('fbad'))
    print(obj.search('fb'))
    print(obj.search('abc'))

    print(obj.search('abcd'))
    print(obj.search('abcde'))

    print(obj.startsWith('fb'))
    print(obj.startsWith('ab'))
    print(obj.startsWith('abc'))
    print(obj.startsWith('abcd'))
