import collections


class TrieNode:
    def __init__(self):
        self.char_nodes_map = collections.defaultdict()
        self.end_word = None


class Solution(object):
    def _init_trie(self):
        self.root_trie = TrieNode()

    def add_product_to_trie(self, product):
        curr_trie_node = self.root_trie
        for curr_char in product:
            # print(curr_char+' '),
            if curr_char not in curr_trie_node.char_nodes_map:
                curr_trie_node.char_nodes_map[curr_char] = TrieNode()
            curr_trie_node = curr_trie_node.char_nodes_map[curr_char]
        # print('\n')
        curr_trie_node.end_word = product

    def build_trie(self, products):
        self._init_trie()
        for curr_product in products:
            self.add_product_to_trie(curr_product)

    def search_words_for_prefix(self, prefix):
        # print('...........')
        # print(prefix)
        curr_trie_node = self.root_trie
        for curr_char in prefix:
            if curr_char not in curr_trie_node.char_nodes_map:
                return []
            curr_trie_node = curr_trie_node.char_nodes_map[curr_char]

        # enumerate all words starting from this node
        queue = [curr_trie_node]
        del curr_trie_node
        searched_products = []
        while queue:
            curr_trie_node = queue.pop(0)
            if curr_trie_node.end_word is not None:
                # print(curr_trie_node.end_word)
                searched_products.append(curr_trie_node.end_word)
                # if len(searched_products) == 3:
                #     return searched_products

            for curr_suffix_char in sorted(curr_trie_node.char_nodes_map.keys()):
                # print(curr_suffix_char+' '),
                queue.append(curr_trie_node.char_nodes_map[curr_suffix_char])
            # print('\n')

        return searched_products

    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        if not products:
            return []

        if not searchWord:
            return products

        self.build_trie(products=products)

        suggestions = []

        prefix = ""
        for curr_char in searchWord:
            prefix += curr_char
            curr_prefix_suggestions = self.search_words_for_prefix(prefix=prefix)
            curr_prefix_suggestions.sort()
            curr_prefix_suggestions = curr_prefix_suggestions[:3]
            suggestions.append(curr_prefix_suggestions)

        return suggestions

