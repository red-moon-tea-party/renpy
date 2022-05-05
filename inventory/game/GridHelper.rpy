init -2 python:
    class GridHelper:
        MINIMUM_NUM_ROWS = 2
        NUM_COLUMN = 3

        # 计算需要有多少空白格子来补位。
        @classmethod
        def get_num_fill(cls, total):
            return GridHelper.get_num_row(
                total) * GridHelper.NUM_COLUMN - total

        # 计算有多少行
        @classmethod
        def get_num_row(cls, total):
            return max(GridHelper.MINIMUM_NUM_ROWS,
                (total + GridHelper.NUM_COLUMN - 1) / GridHelper.NUM_COLUMN)
