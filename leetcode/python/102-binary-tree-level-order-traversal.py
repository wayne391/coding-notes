class Solution(object):
    def levelOrder(self, root):
        if root is None:
            return []
        res = []
        queue = [root]
        while len(queue):
            tmp_r = []
            tmp_q = []
            for e in queue:
                if e is not None:
                    tmp_r.append(e.val) 
                    tmp_q.extend([e.left, e.right])
            if len(tmp_r):
                res.append(tmp_r)
            queue = tmp_q
        return res