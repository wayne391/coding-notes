# --------------------------------- #
# My Original Ans: 2 placeholders
# --------------------------------- #

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        prev = None
        while cur and cur.next:
            if cur.val != cur.next.val:
                prev = cur
                cur = cur.next
            else:
                end = cur.next
                while end:
                    if end.val != cur.val:
                        break
                    end = end.next
                if prev:
                    prev.next = end
                else:
                    head = end
                cur = end
        return head