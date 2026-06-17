class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        print(nums)

        res = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            
            number1 = nums[i]
            l, r = i+1, len(nums)-1

            while l < r:
                threeSum = number1 + nums[l] + nums[r]

                if threeSum < 0:
                    l += 1
                
                elif threeSum > 0:
                    r -= 1

                else:
                    res.append([number1, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return res