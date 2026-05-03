class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        max = 0

        for i in range(n-1,-1,-1):
            print(i, arr[i], max)
            tmp = arr[i]
            arr[i] = max
            if tmp > max:
                max = tmp
            

        arr[n-1] = -1
        return arr

            
             

            

        