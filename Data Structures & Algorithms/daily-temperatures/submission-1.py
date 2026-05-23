class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)

        results = [0 for i in temperatures]

        for i, t in enumerate(temperatures):

            if not stack or t < stack[-1][0]:
                stack.append([t,i])
            else:
                j = 0
                while stack and t > stack[-1][0]:
                    val, index = stack.pop()

                    j = i - index
                    results[index] = j
                stack.append([t,i])
        
        return results

        