import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #piles[i] is # bananas in ith pile
        #h = hours to eat all bananas 
        #k = bananas/hour eating rate 
        #each hour choose pile of bananas and eat k bananas from that pile 
        #if pile < k bananas, can't eat from another pile in same hour

        #return min int k so all bananas can be eaten within h hours

        def canHeDoIt(piles, h, k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)

            return hours <= h
                
        #[1, max(piles)] 1 banana per hour or eat largest pile per hour
        low = 1
        high = max(piles)
        while low < high:
            mid = low + (high-low)//2
            if canHeDoIt(piles, h, mid):
                high = mid
            else:
                low = mid+1

        return low