class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict = {}
        for string in strs:
            key = tuple(sorted(string))
            dict[key] =dict.get(key,[])+ [string]
        return dict.values()
