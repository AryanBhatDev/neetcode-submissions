class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        N = len(arr)
        largestEle = arr[N - 1]
        arr[N-1] = -1

        for i in range(N - 2 , -1, -1):
            if arr[i] <= largestEle:
                arr[i] = largestEle

            else:
                arr[i],largestEle  = largestEle, arr[i]

        return arr                 




     



        