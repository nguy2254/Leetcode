#Such an elegant answer - Not mine 
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for num in nums:
            #Get the index of this number 
            i = abs(num) - 1 
            #Find the element of ith in the nums sequence
            #If it is there, mark them by turn it into negative 
            #If a number is repeated, no need to mark (one number should be there one time)
            if nums[i] > 0:
                nums[i] = - nums[i]
            #Suppose we have all numbers, then all should be turn into negative 
            #If one of the number is missing, then the number at that location will not marked
        missing_array =  [i+1 for i,num in enumerate(nums) if num >0]
        return missing_array
