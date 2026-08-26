"""
The median is the middle value in a sorted list of integers. For lists of even length, there is no middle value, so the median is the mean of the two middle values.

For example:

    For arr = [1,2,3], the median is 2.
    For arr = [1,2], the median is (1 + 2) / 2 = 1.5

Implement the MedianFinder class:

    MedianFinder() initializes the MedianFinder object.
    void addNum(int num) adds the integer num from the data stream to the data structure.
    double findMedian() returns the median of all elements so far.
"""

"""
Example 1:

Input:
["MedianFinder", "addNum", "1", "findMedian", "addNum", "3" "findMedian", "addNum", "2", "findMedian"]

Output:
[null, null, 1.0, null, 2.0, null, 2.0]

Explanation:
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.findMedian(); // return 1.0
medianFinder.addNum(3);    // arr = [1, 3]
medianFinder.findMedian(); // return 2.0
medianFinder.addNum(2);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
"""

"""
This is a heap problem, specifically a two-heap problem where we split the input into two heaps with the lower half is a max heap and the upper half is the min heap that way when we pop the heaps if the output of them are the same then we have our median otherwise we add them and get their mean/average.
"""

import heapq
class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if self.small and num > -(self.small[0]) or self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)
        if len(self.small) > len(self.large):
            heapq.heappush(self.large, -(heapq.heappop(self.small)))
        elif len(self.small) < len(self.large):
            heapq.heappush(self.small, -(heapq.heappop(self.large)))

    def findMedian(self) -> float:
        if len(self.small) < len(self.large):
            return self.large[0]
        elif len(self.small) > len(self.large):
            return -(self.small[0])
        else:
            return (-(self.small[0]) + self.large[0]) / 2
        