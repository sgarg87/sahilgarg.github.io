class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        address_split = address.split('.')
        return '[.]'.join(address_split)
