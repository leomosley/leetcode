class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        
        magazine = [i for i in magazine]
        for i in ransomNote:
            if i not in magazine:
                return False
            else:
                magazine.remove(i)
        return True
                
        