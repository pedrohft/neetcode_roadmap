class Solution:
    def nextGreaterElement(self, nums1, nums2):
        aux = []
        for i in nums1:
            a = nums2.index(i)+1
            m = i
            while a < len(nums2):
                if m < nums2[a]:
                    m = nums2[a]
                    break
                a+=1
            if m == i:
                aux.append(-1)
            else:
                aux.append(m)
        return aux
    

print(Solution().nextGreaterElement([4,1,2], [1,3,4,2]))