class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        cur = head
        is_next = True
        carry = 0
        cur_1 = l1
        cur_2 = l2
        while is_next:
            if not cur_1 and not cur_2 and not carry:
                break
                
            val_1 = cur_1.val if cur_1 else 0
            val_2 = cur_2.val if cur_2 else 0
            val = val_1 + val_2 + carry
           
            carry = val // 10

            res = ListNode(val % 10)
            cur.next = res
            cur = res
            
            is_next = False
            if cur_1 is not None:
                cur_1 = cur_1.next
                is_next = True
                    
            if cur_2 is not None:
                cur_2 = cur_2.next
                is_next = True
                
        return head.next