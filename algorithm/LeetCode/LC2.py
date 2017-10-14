# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_current = l1
        l2_current = l2
        ll1 = []
        ll2 = []
        while l1_current is not None:
            ll1.append(l1_current.val)
            l1_current = l1_current.next
        while l2_current is not None:
            ll2.append(l2_current.val)
            l2_current = l2_current.next
        t_length = max(len(ll1), len(ll2))
        ll1 += [0] * (t_length - len(ll1))
        ll2 += [0] * (t_length - len(ll2))
        sums = [x + y for x, y in zip(ll1, ll2)]
        for i in range(len(sums)):
            if i == (len(sums) - 1):
                if sums[i] >= 10:
                    sums[i] -= 10
                    sums.append(1)
            else:
                if sums[i] >= 10:
                    sums[i] -= 10
                    sums[i+1] += 1
        result = ListNode(0)
        r = result
        for i in range(len(sums)):
            r.val = sums[i]
            if i != len(sums)-1:
                r.next = ListNode(0)
                r = r.next
        return result