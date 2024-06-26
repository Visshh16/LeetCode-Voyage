class Solution(object):
    def heightChecker(self, heights):
        cnt = 0
        expected = sorted(heights)

        for i in range(len(heights)):
            if heights[i] != expected[i]:
                cnt += 1
        
        return cnt
