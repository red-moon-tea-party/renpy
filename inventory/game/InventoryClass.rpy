init -1 python:
    from collections import defaultdict
    class Inventory:
        def __init__(self):
            # dict（字典）
            # e.g. {FOX: 10}
            self.stock = defaultdict(int)

        # 这个函数是用来在控制台debug的时候，可以打印出目前仓库里所有的东西和数量。
        def __str__(self):
            res = ""
            for item in self.stock:
                res += item.name + ' ' + str(self.stock[item])
            return res

        # 检查物品是否存在，如果不存在，程序会直接报错。
        def __check_item_exist__(self, item):
            if not item in self.stock:
                raise Exception('Bag: item {:s} not in bag.', item.name)

        # 某种物品的数量增加1，或者增加count个，如果不传入count，就是增加1个。
        def add(self, item, count=1):
            self.stock[item] += count

        # 某种物品的数量减少1，或者减少count个
        def remove(self, item, count=1):
            self.__check_item_exist__(item)

            if self.stock[item] < count:
                raise "There is not enough {:s}".format(item.name)

            self.stock[item] -= count

        # 获得这个物品有几个
        def get_num_item(self, item):
            self.__check_item_exist__(item)
            return self.stock[item]

        # 返回背包里的物品，如果filter_empty是True，不返回数量为0的物品。
        def get_items(self, filter_empty=False):
            if filter_empty:
                return [x for x in self.stock.keys() if self.stock[x]]
            return list(self.stock.keys())
