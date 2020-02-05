class Solution(object):
    def is_symbol(self, x):
        if x in ['+', '-', '*', '/']:
            return True
        else:
            return False

    def read_operand_or_operator(self, s, n, i):
        if self.is_symbol(s[i]):
            return s[i], i+1, True
        else:
            j = i
            while (j < n) and (not self.is_symbol(s[j])):
                j += 1
            operand = s[i:j]
            return int(operand), j, False

    def infix_to_postfix(self, s):
        n = len(s)

        # infix to postfix
        elements_stack = list()
        postfix = list()
        i = 0
        while i < n:
            x, i, is_operator = self.read_operand_or_operator(s=s, n=n, i=i)

            if is_operator:
                if not elements_stack:
                    elements_stack.append(x)
                else:
                    while elements_stack:
                        old_x = elements_stack[-1]
                        if (x in ['*', '/']) and (old_x in ['+', '-']):
                            break
                        else:
                            postfix.append(old_x)
                            elements_stack.pop()
                    elements_stack.append(x)
            else:
                postfix.append(x)

        while elements_stack:
            old_x = elements_stack.pop()
            postfix.append(old_x)

        return postfix

    def evaluate_postfix(self, postfix):
        stack = list()
        for x in postfix:
            if self.is_symbol(x):
                assert stack
                op2 = stack.pop()
                op1 = stack.pop()
                if x == '+':
                    y = op1+op2
                elif x == '-':
                    y = op1-op2
                elif x == '*':
                    y = op1*op2
                elif x == '/':
                    y = int(op1/op2)
                else:
                    raise AssertionError
                stack.append(y)
            else:
                stack.append(x)
        assert len(stack) == 1
        return stack[-1]

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        postfix = self.infix_to_postfix(s=s)
        print postfix
        return self.evaluate_postfix(postfix=postfix)
