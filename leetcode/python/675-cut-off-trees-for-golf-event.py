import queue

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


class Solution:
    def cutOffTree(self, forest):
        final = []
        q = queue.Queue()
        x_b = len(forest)
        y_b = len(forest[0])
        forest[0][0] = -1
        num_trees = sum([1 for row in forest for t in row if t > 1])
        start = {
            'loc': (0, 0),
            'map': forest,
            'step': 0,
            'max': -1,
            'remain': num_trees,
        }

        q.put(start)
        while(not q.empty()):
            cur = q.get()
            cur_remain = cur['remain']
            cur_step = cur['step']
            cur_loc = cur['loc']
            cur_map = cur['map']
            cur_max = cur['max']

            # success
            if cur_remain == 0:
                final.append(cur_step)
                continue

            if cur_step > (x_b*y_b):
                continue

            for d in directions:
                x = cur_loc[0] + d[0]
                y = cur_loc[1] + d[1]

                # boundary
                if (x < 0) or (y < 0) or (x >= x_b) or (y >= y_b):
                    continue
                next_step = forest[x][y]

                # obstacle
                if (not next_step) or next_step==-1:
                    continue

                # if cut, check height
                new_remain = -1
                new_max = -1
                if next_step > 1:
                    if next_step < cur_max:
                        continue
                    else:
                        new_remain = cur_remain - 1
                        new_max = next_step

                new_map = cur_map[:]
                new_map[x][y] = -1
                tmp = {
                    'loc': (x, y),
                    'map': new_map,
                    'step': cur_step+1,
                    'max': cur_max if new_max == -1 else new_max,
                    'remain': cur_remain if new_remain == -1 else new_remain,
                }
                q.put(tmp)
        print(final)
        ans = min(final) if final else -1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.cutOffTree([[54581641,64080174,24346381,69107959],
                        [86374198,61363882,68783324,79706116],
                        [668150  ,92178815,89819108,94701471],
                        [83920491,22724204,46281641,47531096],
                        [89078499,18904913,25462145,60813308]])
