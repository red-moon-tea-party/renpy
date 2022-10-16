init -1 python:
    from collections import defaultdict
    class Item(object):
        def __init__(self, name, img):
            # 物品名字 （string）e.g. "fox"
            self.name = name

            # 物品图片 （string） e.g. "images/items/fox.png"
            self.img = img

        # 因为后面用了item这个类来做字典的键值，所以需要这两个函数，用来比较两个物品对象是不是一个物品。
        def __eq__(self, another):
            return hasattr(another, 'img') and self.img == another.img

        # 因为后面用了item这个类来做字典的键值，所以需要这两个函数，用来比较两个物品对象是不是一个物品。
        def __hash__(self):
            return hash(self.img)

        # 返回一个物品图片位置的字符串。e.g. “images/items/fox.png”
        def get_icon(self):
            return self.img

    class BoosterItem(Item):
        def __init__(self, name, price, booster, description=""):
            super(BoosterItem, self).__init__(name,
                'images/items/' + name + '.png')

            # 物品描述 （string）
            # e.g. “可以增加{color=#F37459}10点智力{/color}”
            self.description = description

            # 物品价格 （int）
            # 20
            self.price = price

            # 物品可以提升的属性，这个属性，需要和player class里的成员变量相对应。
            # dict
            # e.g. dict(charisma = 5)
            self.booster = booster

        # 这个函数会根据这个物品的booster属性，增加使用者对应的属性。
        def use(self, player):
            for attribute in self.booster:
                player.increase_by(attribute, self.booster[attribute])
