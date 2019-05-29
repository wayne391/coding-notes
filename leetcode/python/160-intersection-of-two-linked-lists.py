
'''
My posts:
https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/301264/python3-two-solutions

Solution 1
'''
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None
        curA = headA
        curB = headB
        while curA != curB:
            curA = curA.next if curA else headB
            curB = curB.next if curB else headA
        return curA

'''
Solution 2
'''          

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None

        # compute length of A
        lenA = 0
        cur = headA
        while cur:
            cur = cur.next
            lenA += 1
            
        # compute length of B
        lenB = 0
        cur = headB
        while cur:
            cur = cur.next
            lenB += 1
        
        # compute offset for stripping
        shiftA = lenA - lenB if lenA > lenB else 0
        shiftB = lenB - lenA if lenB > lenA else 0
        
        curA = headA
        curB = headB
        
        # strip two linked list to the same length
        while shiftA:
            curA = curA.next
            shiftA -= 1
            
        while shiftB:
            curB = curB.next
            shiftB -= 1
        
        # compare
        res = None
        while curA and curB:
            if curA == curB:
                return curA
            curA = curA.next
            curB = curB.next
        return res