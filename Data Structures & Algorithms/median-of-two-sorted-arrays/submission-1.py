class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        A = nums1
        B = nums2
        tot = len(A) + len(B)
        half = (tot + 1) // 2
        
        left, right = 0, len(A)

        while left <= right:
            mid = (left + right) // 2
            Aleft = A[mid - 1] if mid > 0 else float('-infinity')
            Aright = A[mid] if mid < len(A) else float('infinity')
            Bleft = B[half - mid - 1] if half - mid > 0 else float('-infinity')
            Bright = B[half - mid] if half - mid < len(B) else float('infinity')

            print("A:", Aleft, ",", Aright, ". B:", Bleft, ",", Bright)
            if Aleft > Bright:
                right = mid - 1
                continue
            
            if Bleft > Aright:
                left = mid + 1
                continue
            
            if Aleft <= Bright and Bleft <= Aright:
                if tot % 2:
                    return max(Aleft, Bleft)
                else:
                    return float(1.0 * (max(Aleft, Bleft) + min(Aright, Bright)) / 2)
        
        return -1
            