import heapq


class Solution(object):
    def extract_info_from_log(self, log):
        i = log.index(':')
        f_id = int(log[:i])
        log = log[i+1:]

        if log.startswith('start:'):
            is_start = True
            log = log.strip('start:')
        elif log.startswith('end:'):
            is_start = False
            log = log.strip('end:')
        else:
            raise AssertionError
        time = int(log)

        return f_id, time, is_start

    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """

        et = [0]*n
        f_stack = list()
        last_f_end_time = None

        for x in logs:
            f_id, time, is_start = self.extract_info_from_log(log=x)
            print(f_id, time, is_start, last_f_end_time)

            if is_start:
                if f_stack:
                    prv_f_id = f_stack[-1][0]
                    et[prv_f_id] += (time - f_stack[-1][1])
                f_stack.append((f_id, time))
            else:
                assert f_stack[-1][0] == f_id
                if (last_f_end_time is None) or (last_f_end_time < f_stack[-1][1]):
                    assert et[f_id] == 0
                    et[f_id] = time-f_stack[-1][1]
                else:
                    assert last_f_end_time > f_stack[-1][1]
                    et[f_id] += (time - last_f_end_time)

                last_f_end_time = time
                f_stack.pop()

            print(et)

        assert not f_stack

        return et
