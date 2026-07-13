class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #sorted in increasing order 
        #first index is the smallest 
        
        front_index = 0
        back_index = len(numbers)-1

        #if sum of numbers at 2 pointers greater than target decrement right, else increment left
        #repeat until you find a target 
        while front_index < back_index:
            if numbers[front_index] + numbers[back_index] == target:
                if front_index > back_index:
                    return [back_index+1, front_index+1]
                else:
                    return [front_index+1, back_index+1]
            if numbers[back_index] + numbers[front_index] > target:
                back_index -= 1
            else:
                front_index += 1