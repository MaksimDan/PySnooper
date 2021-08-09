import os

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
