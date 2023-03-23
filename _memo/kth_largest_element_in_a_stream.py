import heapq


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.lists, self.num = [], k
        for i in nums:
            self.add(i)

    def add(self, val: int) -> int:
        heapq.heappush(self.lists, val)
        if len(self.lists) > self.num:
            heapq.heappop(self.lists)
        return self.lists[0]


kth = KthLargest(3, [4, 5, 8, 2, 6, 1])
kth.add(3)
kth.add(5)
kth.add(9)
kth.add(4)
