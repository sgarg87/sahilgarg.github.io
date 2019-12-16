import numpy as np


class ContainerWithMostWater:
    def __init__(self):
        pass

    def maxArea(self, heights):
        num_heights = heights.size
        left_idx = 0
        right_idx = num_heights-1
        max_area = 0

        while left_idx < right_idx:
            width = right_idx - left_idx

            left_height = heights[left_idx]
            right_height = heights[right_idx]
            min_height = min(left_height, right_height)

            area = min_height*width
            if area > max_area:
                max_area = area

            if left_height < right_height:
                left_idx += 1
            else:
                right_idx -= 1

        return max_area


if __name__ == '__main__':
    heights = np.array([1, 8, 6, 2, 5, 4, 8, 3, 7])
    cmw_obj = ContainerWithMostWater()
    max_area = cmw_obj.maxArea(heights=heights)
    print(max_area)

