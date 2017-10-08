class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        s_s = [list((map(lambda x:''.join(sorted(x)), x))) for x in strs]
        print(s_s)
        dic_pair = dict()
        print(len(s_s))
        for i in range(len(s_s)):
            if s_s[i] not in dic_pair.keys():
                dic_pair[s_s[i]] = strs[i]
            else:
                dic_pair[s_s[i]].append(strs[i])

        new_dic = dict()
        for key in dic_pair:
            new_dic[len(dic_pair[key])] = dic_pair[key]

        result = []
        for key in sorted(new_dic.keys()):
            result.append(new_dic[key])

        return result

if __name__ == "__main__":
    a = ["eat","tea","tan","ate","nat","bat"]

    b = Solution()
    b.groupAnagrams(a)