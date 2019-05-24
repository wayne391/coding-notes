
# --------------------------------- #
# 1 placeholders
# --------------------------------- #
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
                continue
            cur = cur.next
        return head

# --------------------------------- #
# My Original Ans: 2 placeholders
# --------------------------------- #

# class Solution:
#     def deleteDuplicates(self, head: ListNode) -> ListNode:
#         if head is None or head.next is None:
#             return head

#         front = head
#         back = head.next
#         while back:
#             if back.val == front.val:
#                 front.next =  back.next
#                 back = back.next
#             else:
#                 front = back
#                 back = back.next
#         return head