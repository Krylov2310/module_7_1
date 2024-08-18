print('\033[30m\033[47mДомашнее задание по теме "Режимы открытия файлов"\033[0m')
print('\033[30m\033[47mЗадача "Учёт товаров":\033[0m')
print('\033[30m\033[47mСтудент Крылов Эдуард Васильевич\033[0m')
thanks = '\033[30m\033[47mБлагодарю за внимание :-)\033[0m'
print()


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self, __file_name='products.txt'):
        self.__file_name = __file_name

    def get_products(self):
        file = open(self.__file_name, 'r')
        file_ = file.read()
        file.close()
        return file_

    def add(self, *product):
        for i in product:
            prod_ = str(i)
            file = open(self.__file_name, 'r')
            file_ = file.read()
            file.close()
            if prod_ in file_:
                print(f'Продукт {prod_} уже есть в магазине!')
            else:
                file = open(self.__file_name, 'a')
                file.write(f'\n{prod_}')
                file.close()


# Пример работы программы:
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())
print()
print(thanks)
