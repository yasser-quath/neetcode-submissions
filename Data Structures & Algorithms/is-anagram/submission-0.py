class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd = {}
        td = {}
        for i in s:
            if i not in sd:
                sd[i] = 1
            else:
                sd[i] += 1
        for j in t:
            if j not in td:
                td[j] = 1
            else:
                td[j] += 1
        return td == sd
            
        