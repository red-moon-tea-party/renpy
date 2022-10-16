init -1 python:
    from collections import defaultdict
    import random
    class ShopController:
        def __init__(self):
            self.inventory = Inventory()

    class Shop:
        def __init__(self):
            self.inventory = Inventory()

        # 返回一个商店目前拥有的所有物品的列表。
        def get_stock(self):
            return self.inventory.get_items()

        # 卖掉商品，如果没有指定数量（count），就是卖掉一个。
        def sell(self, item, count=1):
            self.inventory.remove(item, count)

        # 购买商品，如果没有指定数量（count），就是购买一个。
        # 可以用来实现玩家卖东西给商店，可以在计算的label里面乘以一个系数，从而
        # 达到商店低价收购玩家商品的功能。
        # 商店进货也可以使用此接口。
        def buy(self, item, count=1):
            self.inventory.add(item, count)

        # 判断一个物品是不是已经卖完。
        def is_sold_out(self, item):
            n = self.inventory.get_num_item(item)
            return n == 0

        # 获得商店此物品的数量
        def get_number(self, item):
            return self.inventory.get_num_item(item)

        # 刷新商店里的物品。适用于每次商店固定输出固定数量的物品的设计。
        # 如果是那种不限制出售物品的商店，可以使用buy接口来更新商店物品。
        def refresh(self, stock):
            self.inventory = Inventory()

            for item, count in stock:
                self.buy(item, count)
