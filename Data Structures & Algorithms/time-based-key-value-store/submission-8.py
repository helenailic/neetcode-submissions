class TimeMap:

    def __init__(self):
        self.mymap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mymap:
            self.mymap[key] = []
        self.mymap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mymap:
            return ""
        if len(self.mymap[key]) == 0:
            return ""
        if self.mymap[key][len(self.mymap[key])-1][0] <= timestamp:
            return self.mymap[key][len(self.mymap[key])-1][1]
        else:
            l = 0
            r = len(self.mymap[key])-1
            rightmostbest = -1
            while l <= r:
                mid = (r-l)//2+l
                if l > r:
                    return ""
                if self.mymap[key][mid][0] <= timestamp:
                    rightmostbest = mid
                    #search right
                    l = mid+1
                else:
                    #search left
                    r = mid-1

        if rightmostbest == -1:
            return ""
        return self.mymap[key][rightmostbest][1]


        
