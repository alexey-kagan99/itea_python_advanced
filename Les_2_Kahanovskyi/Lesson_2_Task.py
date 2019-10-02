class Shop:

    QUANTITI_OF_GOODS_SOLD = 0


    def __init__(self, name, count):

        self._name = name
        self._count = count


    def set_count(self, value):

        self._count += value


    def set_quantiti(self):

        Shop.QUANTITI_OF_GOODS_SOLD += self._count


    def get_quantiti(self):

        print(Shop.QUANTITI_OF_GOODS_SOLD)
        Shop.QUANTITI_OF_GOODS_SOLD = 0



    def __str__(self):

        return f' Shop {self._name} sells {self._count} goods '

class MusGoods(Shop):

    def __init__(self, name, count):

        self._name = name
        self._count = count

class SportGoods(Shop):

    def __init__(self, name, count):

        self._name = name
        self._count = count


shop_1 = MusGoods(' Rock Shop ', 5)
shop_2 = SportGoods(' Sportmaster ', 10)

print(shop_1)
print(shop_2)

shop_1.set_quantiti()
shop_2.set_quantiti()
shop_1.get_quantiti()

shop_1.set_count(5)
shop_2.set_count(10)
print(shop_1)
print(shop_2)

shop_1.set_quantiti()
shop_2.set_quantiti()
shop_1.get_quantiti()
