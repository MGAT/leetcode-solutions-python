"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:

    All inputs will be in lowercase.
    The order of your output does not matter.
"""


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans, res, ret = [], {}, []
        for s in strs:
            temp = list(s)
            temp.sort()
            ans.append("".join(temp))
        for i in range(len(ans)):
            if ans[i] not in res:
                res[ans[i]] = []
            res[ans[i]].append(strs[i])
        for key in res:
            ret.append(res[key])
        return ret
	

s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))