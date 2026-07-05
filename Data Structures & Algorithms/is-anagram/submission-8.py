#Prüfen ob gleich lang sind. Wenn nicht direkt false. 
#Prüfen ob erster Buchstabe auch im zweiten vorhanden ist. 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        HashMapS, HashMapT = {}, {}

        for i in range(len(s)):
            HashMapS[s[i]] = HashMapS.get(s[i],0) + 1
            HashMapT[t[i]] = HashMapT.get(t[i],0) + 1
        for c in HashMapS:
            if HashMapS[c] != HashMapT.get(c,0):
                return False
        return True

 