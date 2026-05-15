import numpy as np
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(arr):
            return np.sqrt(arr[0]**2 + arr[1]**2)

        def sort_points(arr,s,e):
            if e-s + 1 <= 1:
                return
            pivot = distance(arr[e])
            left = s
            for i in range(s, e):
                if distance(arr[i]) <= pivot:
                    tmp = arr[left]
                    arr[left] = arr[i]
                    arr[i] = tmp
                    left += 1

            tmp = arr[left]
            arr[left] = arr[e]
            arr[e] = tmp

            sort_points(arr, s, left-1)
            sort_points(arr, left+1, e)

        sort_points(points, 0, len(points)-1)
        return points[:k]
