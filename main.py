class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_table = {}
        for x in range(0,len(nums)):
            look_num = target - nums[x]
            if look_num in dict_table:
                return [dict_table[look_num],x]
            else:
                dict_table.update({nums[x]: x})
                
        return []
