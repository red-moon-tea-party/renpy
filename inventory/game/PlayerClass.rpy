init -1 python:
    from collections import defaultdict

    class Player:
        def __init__(self, name):
            # 玩家的名字（string）e.g. "black pineapple"
            self.name = name

            # 智力/身材/魅力 (int) e.g. 5
            self.intelligence = 10
            self.fitness = 5
            self.charisma = 5

            # 金钱(int) e.g. 1000
            self.money = 1000

        # 增加玩家的某种属性
        # e.g. intelligence， 5 增加5点智力
        def increase_by(self, attribute, value):
            setattr(self, attribute, value + self.get(attribute))

        # 获得某个属性的数值。
        # e.g. intelligence
        def get(self, attribute):
            return getattr(self, attribute)
