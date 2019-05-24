class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        '''
        key:
            1. add to result list
            2. move pointer of result to the added one
            3. move pointer of the list to the next
        '''
        result = ListNode(-1)
        cur1 = l1
        cur2 = l2
        curr = result
        while(cur1 or cur2):
            if cur1 and cur2:
                if cur1.val <= cur2.val:
                    curr.next = cur1
                    curr = cur1
                    cur1 = cur1.next
                else:
                    curr.next = cur2
                    curr = cur2
                    cur2 = cur2.next
            elif cur1:
                curr.next = cur1
                curr = cur1
                cur1 = cur1.next
            else:
                curr.next = cur2
                curr = cur2
                cur2 = cur2.next
        return result.next
