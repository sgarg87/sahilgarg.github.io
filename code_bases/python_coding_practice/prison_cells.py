import copy


class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        num_cells = len(cells)

        cell_states = list()
        # initial_cells_state = tuple(cells)
        prv_cells = tuple(cells)
        cell_states.append(prv_cells)

        cycle_len = None
        cycle_start_idx = None
        i = 0
        while (cycle_len is None) and (i < N):
            i += 1
            for j in range(num_cells):
                if 1 <= j < (num_cells-1):
                    if prv_cells[j-1] == prv_cells[j+1]:
                        cells[j] = 1
                    else:
                        cells[j] = 0
                else:
                    cells[j] = 0
            prv_cells = tuple(cells)

            if prv_cells in cell_states:
                # including initial state
                cycle_start_idx = cell_states.index(prv_cells)
                cycle_len = i-cycle_start_idx
                cell_states = cell_states[cycle_start_idx:]
                assert len(cell_states) == cycle_len
                print(i, cycle_start_idx, cycle_len)
                break
            else:
                print(i, prv_cells)
                cell_states.append(prv_cells)

        if cycle_len is None:
            return cells
        else:
            num_cyclic_days = (N+1-cycle_start_idx)
            # zero indexing
            present_idx = (num_cyclic_days % cycle_len)-1
            print(num_cyclic_days, present_idx)
            return list(cell_states[present_idx])
