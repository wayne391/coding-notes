'''
Interval---> Sort!!!!
My new solution
'''
class Solution:
    def merge(self, intervals: 'List[Interval]') -> 'List[Interval]':
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
                                       
        ans = []
        
        cur_start = intervals[0][0]
        cur_end = intervals[0][1]
        
        for item in intervals:
            if item[0] <= cur_end:
                if item[1] > cur_end:
                    cur_end = item[1]
            else:
                ans.append([cur_start, cur_end])
                cur_start = item[0]
                cur_end = item[1]
        ans.append([cur_start, cur_end])
        return ans

'''
Interval: min max
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key=lambda x: x[0])
        for i in range(len(intervals)):
            if res and res[-1][1] >= intervals[i][0]:
                res[-1] = [min(intervals[i][0], res[-1][0]),max(intervals[i][1],res[-1][1])]
            else:
                res.append(intervals[i])
        return res

'''
My original: stack, too slow
'''
class Solution:
    def merge(self, intervals: 'List[Interval]') -> 'List[Interval]':
        if not intervals:
            return []
        
        candidates = []
        for item in intervals:
            candidates += [(item[0], 0), (item[1], 1)]
        candidates.sort(key=lambda x: (x[0], x[1]))

        ans = []
        depth = 0
        st = None
        for c in candidates:
            if c[1] == 0:
                if depth == 0:
                    st = c[0]
                depth += 1
            else:
                depth -= 1
                if depth == 0:
                    ans.append([st, c[0]])
        return ans