# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        min_version = 0
        max_version = n

        while min_version != max_version:
            if (max_version-min_version) == 1:
                if isBadVersion(max_version) and isBadVersion(min_version):
                    return min_version
                elif isBadVersion(max_version) and (not isBadVersion(min_version)):
                    return max_version
                else:
                    return -1

            mid_version = int((min_version+max_version)/2)

            if not isBadVersion(mid_version):
                # good version
                min_version = mid_version
            else:
                # bad version
                max_version = mid_version


