class Solution(object):
    def getIntersectionNode(self, headA, headB):
        lenA = 0
        cur = headA
        while cur:
            cur = cur.next
            lenA += 1
            
        lenB = 0
        cur = headB
        while cur:
            cur = cur.next
            lenB += 1
            
        shiftA = lenA - lenB if lenA > lenB else 0
        shiftB = lenB - lenA if lenB > lenA else 0
        
        curA = headA
        curB = headB
        
        while shiftA:
            curA = curA.next
            shiftA -= 1
            
        while shiftB:
            curB = curB.next
            shiftB -= 1
        
        res = None
        while curA and curB:
            if curA == curB:
                return curA
            curA = curA.next
            curB = curB.next
        return res