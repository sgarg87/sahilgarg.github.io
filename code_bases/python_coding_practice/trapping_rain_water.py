import numpy as np


class TrappingRainWater:
    def __init__(self):
        pass

    def max_height_from_left(self, heights):
        num_heights = heights.size
        max_height = 0
        max_heights_from_left = np.zeros(num_heights, dtype=int)

        for curr_idx, curr_height in enumerate(heights):
            max_height = max(max_height, curr_height)
            max_heights_from_left[curr_idx] = max_height

        return max_heights_from_left

    def max_height_from_right(self, heights):
        num_heights = heights.size
        max_height = 0
        max_heights_from_right = np.zeros(num_heights, dtype=int)

        for curr_idx in range(num_heights-1, -1, -1):
            curr_height = heights[curr_idx]
            max_height = max(max_height, curr_height)
            max_heights_from_right[curr_idx] = max_height

        return max_heights_from_right

    def trap(self, heights):
        max_heights_from_left = self.max_height_from_left(heights=heights)
        max_heights_from_right = self.max_height_from_right(heights=heights)
        trapped_water = 0
        for curr_idx, curr_height in enumerate(heights):
            curr_trapped_water = (min(max_heights_from_left[curr_idx], max_heights_from_right[curr_idx])-curr_height)
            assert curr_trapped_water >= 0
            trapped_water += curr_trapped_water
        return trapped_water


if __name__ == '__main__':
    inputs = np.array([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    obj = TrappingRainWater()
    trapped_water = obj.trap(heights=inputs)
    print(trapped_water)


