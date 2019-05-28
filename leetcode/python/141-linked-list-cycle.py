'''
快慢指針
'''
lass Solution(object):
    def hasCycle(self, head):
        if head is None:
            return False
        if head.next == None:
            return False
        
        fast = head.next.next
        slow = head.next
        while fast is not None:
            if fast == slow:
                return True
            if fast.next is None:
                break
            fast = fast.next.next
            slow = slow.next
        return False
        