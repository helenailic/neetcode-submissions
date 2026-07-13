import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mink = max(piles)

        def canEat(piles, h, k) -> bool:
            for pile in piles:
                h = h - math.ceil(pile/k)

            if h < 0:
                return False
            return True

        #search space is [1, max(piles)]
        def minEatingHelper(piles, h, lk, rk):
            nonlocal mink
            mid = (rk-lk)//2 + lk
            if lk > rk:
                return mink
            if canEat(piles, h, mid):
                mink = min(mink, mid)
                #search left
                minEatingHelper(piles, h, lk, mid-1)
            else:
                #search right
                minEatingHelper(piles, h, mid+1, rk)

        minEatingHelper(piles, h, 1, max(piles))
        return mink
