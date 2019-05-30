class Solution(object):
    def reverseList(self, head):
        if head is None:
            return head
        curr = head.next
        prev = head
        prev.next = None
        while curr is not None:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
        return prev