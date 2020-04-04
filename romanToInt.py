class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_to_int = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
            'IV':4,
            'IX':9,
            'XL':40,
            'XC':90,
            'CD':400,
            'CM':900}
        value_list =[]
        if s != "":
            for i,character in enumerate(s):
                    if s[i:i+2] in ['IV','IX','XL','XC','CD','CM']:
                        value_list.append(s[i:i+2])
                        print(i, value_list, s)
                    elif s[i-1:i+1] in ['IV','IX','XL','XC','CD','CM']:
                        pass 
                    else:
                        value_list.append(s[i])
                        print(i, value_list, s)
        return sum([roman_to_int[k] for k in value_list])
