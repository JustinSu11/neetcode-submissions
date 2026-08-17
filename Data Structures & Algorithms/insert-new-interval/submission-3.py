class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        intervals.append(newInterval)
        sortedIntervalList = sorted(intervals)
        firstInterval = sortedIntervalList[0]
        currIntervalStart = firstInterval[0]
        currIntervalEnd = firstInterval[-1]
        ans = []
        for s, e in sortedIntervalList[1: ]:
            if currIntervalEnd < s:
                ans.append([currIntervalStart, currIntervalEnd])
                currIntervalStart = s
            currIntervalEnd = max(currIntervalEnd, e)
        ans.append([currIntervalStart, currIntervalEnd])
        return ans