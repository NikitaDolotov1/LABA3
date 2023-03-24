class Hero:
    def __init__(self, name, lvl, money):
        self._name = name
        self._lvl = lvl
        self._money = money

    def setName(self, name):
        self._name = name

    def setLvl(self, lvl):
        self._lvl = lvl

    def setMoney(self, money):
        self._money = money

    def getName(self):
        return self._name

    def getLvl(self):
        return self._lvl

    def getMoney(self):
        return self._money


h = Hero("Storm Spirit", 25 , 22600)

print(f'Имя: {h._name}, Уровень: {h._lvl}, Деньги: {h._money}')