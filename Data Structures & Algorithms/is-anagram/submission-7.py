#Prüfen ob gleich lang sind. Wenn nicht direkt false. 
#Prüfen ob erster Buchstabe auch im zweiten vorhanden ist. 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)