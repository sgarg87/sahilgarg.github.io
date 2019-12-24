import numpy as np


class Pixel:
    def __init__(self, color, sr, sc):
        self.color = color
        self.sr = sr
        self.sc = sc


class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        num_rows = len(image)
        num_cols = len(image[0])

        queue = []
        visited = set()

        old_color = image[sr][sc]

        pixel = Pixel(color=old_color, sr=sr, sc=sc)
        queue.append(pixel)
        visited.add((sr, sc))
        del pixel

        while queue:
            pixel = queue.pop(0)
            # change the color
            image[pixel.sr][pixel.sc] = newColor

            neighbor_pixel_choices = [
                (pixel.sr-1, pixel.sc), (pixel.sr+1, pixel.sc),
                (pixel.sr, pixel.sc-1), (pixel.sr, pixel.sc+1),
            ]

            for curr_neighbor_pixel in neighbor_pixel_choices:
                row_idx, col_idx = curr_neighbor_pixel
                print(curr_neighbor_pixel)

                # valid neighbor
                if (0 <= row_idx < num_rows) and (0 <= col_idx < num_cols):

                    curr_color = image[row_idx][col_idx]
                    print(curr_color)

                    # selecting neighbors with same color as the starting pixel
                    if curr_color != old_color:
                        continue

                    if curr_neighbor_pixel in visited:
                        continue

                    visited.add(curr_neighbor_pixel)

                    curr_neighbor_pixel_obj = Pixel(
                        color=curr_color,
                        sr=row_idx,
                        sc=col_idx,
                    )
                    queue.append(curr_neighbor_pixel_obj)
                    del curr_neighbor_pixel_obj

        return image

