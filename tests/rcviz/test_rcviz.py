import math
import os
from typing import List

import pysnooper


_dirname = os.path.dirname(__file__)


def test_reviz1():
    @pysnooper.snoop(vis_args=['n', 'a', 'b'], vis_outfile=os.path.join(_dirname, '../resources/fib.png'))
    def fib(n):
        if n <= 1:
            return n
        else:
            a = fib(n - 1)
            b = fib(n - 2)
            return a + b

    fib(5)


def test_reviz2():
    def assign_bikes(workers: List[List[int]], bikes: List[List[int]]):
        cur_min = math.inf
        cur_sum = 0
        assigned_bikes = set()
        manhattan_dist = lambda p1, p2: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        @pysnooper.snoop(vis_args=['cur_sum', 'cur_min', 'assigned_bikes'],
                         vis_outfile=os.path.join(_dirname, '../resources/assign_bikes.png'))
        def dfs(worker_index):
            nonlocal cur_sum, cur_min

            # once we reach a leaf node (all workers have been assigned)
            if worker_index >= len(workers):
                cur_min = min([cur_sum, cur_min])
                return

            # prune if we have already encountered a case that is smaller than the current sum
            if cur_sum > cur_min:
                return

            # assign bike to each worker
            for i in range(len(bikes)):
                if i not in assigned_bikes:
                    dist = manhattan_dist(workers[worker_index], bikes[i])
                    cur_sum += dist
                    assigned_bikes.add(i)

                    dfs(worker_index + 1)

                    assigned_bikes.remove(i)
                    cur_sum -= dist

        dfs(0)
        return cur_min

    assign_bikes([[0, 0], [1, 1], [2, 0]], [[1, 0], [2, 2], [2, 1]])
