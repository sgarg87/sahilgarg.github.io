

class FreqStack:

    def __init__(self):
        self.val_freq__map = {}
        self.freq_values__map = {}
        self.freq_stack = list()

    def _push_freq_stack_and_map(self, new_freq, x):
        if new_freq not in self.freq_values__map:
            new_freq_tuple = (new_freq, list())
            self.freq_stack.append(new_freq_tuple)
            self.freq_values__map[new_freq] = new_freq_tuple[1]
            del new_freq_tuple
        self.freq_values__map[new_freq].append(x)

    def push(self, x: int) -> None:
        # print('......{}........'.format(x))

        if x not in self.val_freq__map:
            self.val_freq__map[x] = 1
            self._push_freq_stack_and_map(new_freq=1, x=x)
        else:
            old_freq = self.val_freq__map[x]
            new_freq = old_freq+1
            del old_freq

            self.val_freq__map[x] = new_freq
            self._push_freq_stack_and_map(new_freq=new_freq, x=x)
            del new_freq

        # print(self.freq_stack)
        # print(self.freq_values__map)

    def pop(self) -> int:
        assert self.freq_stack
        # print('-----------------')
        while self.freq_stack:
            top_frequency, top_frequency_stack = self.freq_stack[-1]
            # print(top_frequency, top_frequency_stack)
            if not top_frequency_stack:
                self.freq_values__map.pop(top_frequency)
                self.freq_stack.pop()
                continue
            else:
                top_val = top_frequency_stack.pop()
                self.val_freq__map[top_val] -= 1
                # print(self.freq_stack)
                return top_val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
