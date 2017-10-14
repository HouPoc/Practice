class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        dic1 = dict((e, 1) for e in "qwertyuiop")
        dic2 = dict((e, 1) for e in "asdfghjkl")
        dic3 = dict((e, 1) for e in "zxcvbnm")
        lst = []
        for s in words:
            lst.append(s)
            for e in s.lower():
                if e not in dic1:
                    lst.remove(s)
                    break
            lst.append(s)
            for e in s.lower():
                if e not in dic2:
                    lst.remove(s)
                    break
            lst.append(s)
            for e in s.lower():
                if e not in dic3:
                    lst.remove(s)
                    break
        return lst