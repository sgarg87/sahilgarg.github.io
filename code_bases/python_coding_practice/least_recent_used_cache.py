class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prv = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.key_val_map = {}
        self.begin_node = Node(None, None)
        self.end_node = Node(None, None)
        self.number_nodes = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.key_val_map:
            return -1

        val = self.key_val_map[key].val

        if self.end_node.prv.key != key:
            self._remove(key=key)
            self.put(key=key, value=val)

        return val

    def _remove(self, key):
        assert key in self.key_val_map

        val_node = self.key_val_map[key]
        self.key_val_map.pop(key)

        prv_node = val_node.prv
        assert prv_node is not None
        next_node = val_node.next
        assert next_node is not None

        prv_node.next = next_node
        next_node.prv = prv_node
        val_node.prv = None
        val_node.next = None
        del val_node

        self.number_nodes -= 1

    def _remove_first_node(self):

        assert self.begin_node.next is not None
        first_node = self.begin_node.next
        self.begin_node.next = first_node.next
        first_node.next.prv = self.begin_node
        first_node.next = None
        first_node.prv = None

        assert first_node.key in self.key_val_map
        self.key_val_map.pop(first_node.key)
        del first_node

        self.number_nodes -= 1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key not in self.key_val_map:
            if self.number_nodes == self.capacity:
                self._remove_first_node()

            val_node = Node(key=key, val=value)
            self.key_val_map[key] = val_node

            if self.end_node.prv is None:
                # empty doubly linked list
                assert self.begin_node.next is None
                self.begin_node.next = val_node
                self.end_node.prv = val_node
                val_node.next = self.end_node
                val_node.prv = self.begin_node
            else:
                # add at the end of the linked list
                last_node = self.end_node.prv
                last_node.next = val_node
                val_node.prv = last_node
                val_node.next = self.end_node
                self.end_node.prv = val_node
                del last_node, val_node
            self.number_nodes += 1
        else:
            self._remove(key=key)
            self.put(key=key, value=value)
