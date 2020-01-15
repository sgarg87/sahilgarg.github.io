class Solution(object):
    def __init__(self):
        self.left_right_brackets_map = {}
        self.left_right_brackets_map['{'] = '}'
        self.left_right_brackets_map['['] = ']'
        self.left_right_brackets_map['('] = ')'

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = list()
        for curr_symbol in s:
            if curr_symbol in self.left_right_brackets_map:
                stack.append(curr_symbol)
            else:
                if not stack:
                    return False
                else:
                    top_element = stack.pop()
                    if self.left_right_brackets_map[top_element] == curr_symbol:
                        continue
                    else:
                        return False
        if stack:
            return False
        else:
            return True
