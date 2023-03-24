class Hero:
    def __init__(self, name, lvl, money):
        self._name = name
        self._lvl = lvl
        self._money = money

    @property
    def name(self):
        return self._name

    @property
    def lvl(self):
        return self._lvl

    @property
    def money(self):
        return self._money

    @name.setter
    def name(self, name):
        self._name = name

    @lvl.setter
    def lvl(self, lvl):
        self._lvl = lvl

    @money.setter
    def money(self, money):
        self._money = money




h = Hero("Pangolier", 20, 21444)


print(f'Имя: {h.name}, Уровень: {h.lvl}, Деньги: {h.money}')


h.name = "Storm Spirit"
h.lvl = 24
h.money = 17600

print(f'Имя: {h.name}, Уровень: {h.lvl}, Деньги: {h.money}')