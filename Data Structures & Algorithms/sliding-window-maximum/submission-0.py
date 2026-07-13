class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = collections.deque() #indices 
        l = 0
        r = 0

        while r < len(nums):
            #make sure no smaller values exist in queue before appending
            while len(q) != 0 and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            #if left out of bounds, remove left value out of queue  -- because it's of indices!
            if l > q[0]:
                q.popleft()
            
            #for each window add the maximum which is the left position
            if (r+1) >= k:
                res.append(nums[q[0]])
                l += 1
            
            r += 1

        
        return res