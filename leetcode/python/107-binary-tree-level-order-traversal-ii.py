
'''
Best solution
Key: Maintion all item in the queue to have the same depth.
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root):
        if root is None:
            return []
        collect = []
        queue = [root]

        while(len(queue)):
            tmp_queue = []
            tmp_collect = []
            for item in queue:
                tmp_collect.append(item.val)
                if item.left:
                    tmp_queue.append(item.left)
                if item.right:
                    tmp_queue.append(item.right)
            collect.append(tmp_collect)
            queue = tmp_queue
        return collect[::-1]


'''
Using library, slower
'''
# import queue
# class Solution:
#     def levelOrderBottom(self, root):
#         if root is None:
#             return []
#         q = queue.Queue()
#         collect = dict()
#         root.lv = 0
#         N = 0
#         q.put(root)

#         while(not q.empty()):
#             cur = q.get()
#             N = cur.lv
#             collect[cur.lv] = collect.get(cur.lv, []) + [cur.val]

#             if cur.left:
#                 cur.left.lv = cur.lv + 1
#                 q.put(cur.left)
#             if cur.right:
#                 cur.right.lv = cur.lv + 1
#                 q.put(cur.right)
#         return [collect[i] for i in range(N, -1, -1)]
