from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        if l1.val is None:
            return ListNode[l2.val]
        elif l2.val is None:
            return ListNode[l1.val]
        

        first = l1.val
        res_1 = 0

        second = l2.val
        res_2 = 0

        for idx, x in enumerate(first):
             res_1 += x*10**idx

        for idy, y in enumerate(second):
             res_2 += y*10**idy


        res = list(reversed([int(x) for x in str(res_1+res_2)]))

        return ListNode(res)




a = Solution()
print(a.addTwoNumbers(ListNode([2,4,3]), ListNode([5,6,4])))
print(a.addTwoNumbers(ListNode([9,9,9,9,9,9,9]), ListNode([9,9,9,9])))
print(a.addTwoNumbers(ListNode([0]), ListNode([0])))     