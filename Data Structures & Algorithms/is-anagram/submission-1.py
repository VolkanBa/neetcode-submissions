#Prüfen ob gleich lang sind. Wenn nicht direkt false. 
#Prüfen ob erster Buchstabe auch im zweiten vorhanden ist. 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = "".join(sorted(s))
        t = "".join(sorted(t))
        i = 0
        output = True
        while i < len(s) and i < len(t):
            if len(s) != len(t):
                output = False
                break
            if s[i] != t[i]:
                output = False
                break
            i+=1
        return output
        