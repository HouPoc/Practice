from collections import Counter


class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s.find('LLL') != -1 or Counter(s)['A'] > 1:
            return False
        else:
            return True
