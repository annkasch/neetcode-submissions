import numpy as np
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(arr):
            return np.sqrt(arr[0]**2 + arr[1]**2)
        
        def sort_points(arr,cache, s,e):
            if e-s + 1 <= 1:
                return
            pivot = distance(arr[e])
            left = s
            for i in range(s, e):
                if cache[i] == -1:
                    cache[i] = distance(arr[i])
                if cache[i] <= pivot:
                    tmp = arr[left]
                    arr[left] = arr[i]
                    arr[i] = tmp
                    tmp = cache[left]
                    cache[left] = cache[i]
                    cache[i] = tmp
                    left += 1

            tmp = arr[left]
            arr[left] = arr[e]
            arr[e] = tmp
            tmp = cache[left]
            cache[left] = cache[e]
            cache[e] = tmp

            sort_points(arr, cache, s, left-1)
            sort_points(arr, cache, left+1, e)
        
        cache = [-1 for i in points]
        sort_points(points, cache, 0, len(points)-1)
        return points[:k]
