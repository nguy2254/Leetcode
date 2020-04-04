class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        dictionary = {}
        for cpdomain in cpdomains:
            result = cpdomain.replace("."," ").split() 
            count = int(result[0])
            domain = result[1:][::-1]
            options= [domain[0]]
            for i in domain[1:]:
                option = i+'.'+ options[-1]
                options.append(option)
            for option in options:
                if option in dictionary.keys():
                    dictionary[option] += count 
                else:
                    dictionary[option] = count 
        
        result = [str(value)+' '+str(key) for key, value in         zip(dictionary.keys(),dictionary.values())]
        return result  
