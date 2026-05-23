class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []

        results = [0]*len(temperatures)

        for i, t in enumerate(temperatures):

                while stack and t > stack[-1][0]:
                    val, index = stack.pop()
                    j = i - index
                    results[index] = j
                stack.append([t,i])
        
        return results

        