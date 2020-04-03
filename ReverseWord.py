class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip().split()[::-1]
        new_s = ""
        for word in s:
            new_s+=" "+ word
        new_s = new_s.strip()
        return new_s
        
   class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s[::-1]
        word = ""
        new_string = ""
        for j, character in enumerate(s):
            if character != " " and s[j-1] == " " and word !="":
                new_string += (word + " ")
                word = character 
            elif character !=  " ":
                word = character + word 
        new_string += word
        return new_string
    
