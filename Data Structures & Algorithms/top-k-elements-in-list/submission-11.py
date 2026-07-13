from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #list where indices represent anmount of times a nunber shows up
        #the value in it is the number that shows up that many times
        #then go through that guy from right to left
        
        my_dict = defaultdict(int) #num: amount of times
        for num in nums:
            my_dict[num] += 1

        my_list = []
        for i in range(len(nums)+1):
            my_list.append([])
        print(my_list)
        print(my_dict)

        for key in my_dict:
            numTimes = my_dict[key]
            numberItself = key

            my_list[numTimes].append(numberItself)

        print(my_list)

        numElemsTaken = 0
        outputList = []
        for i in range(len(my_list)-1, -1, -1):
            if numElemsTaken == k:
                break
            if len(my_list[i]) != 0:
                for val in my_list[i]:
                    outputList.append(val)
                    numElemsTaken += 1

        return outputList

