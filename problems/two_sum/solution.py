class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ##################################################
        #Best Solution
        ##################################################
        hashMap ={}
        for i, num in enumerate(nums):
            diff=target-num
            if diff in hashMap:
                return [hashMap[diff], i]
            hashMap[num]=i
        
        
        
        
        
        
        
        
        
        
    #########################################################
    #My Answer
    #########################################################
#        for i in range(len(nums)):
#            for j in range(len(nums)):
#                if (nums[i]+nums[j]==target and i != j ):
#                    return [i,j]

                