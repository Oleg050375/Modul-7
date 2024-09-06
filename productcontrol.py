class Product:
    def __init__(self, name, weight, category):
        self.name = name  # наименование (str)
        self.weight = weight  # вес (float)
        self.category = category  #  категория (str)

    def __str__(self):  # формирование строки описания продукта
        return self.name + ', ' + str(self.weight) + ', ' + self.category

class Shop:
    __file_name = 'product.txt'  # переменная имени файла

    def __getproduct__(self):  # метод получения списка продуктов
        a = open(self.__file_name, 'r')  # открытие файла для чтения
        b = a.read()  # сохранение списка продуктов
        a.close()  # закрыли файл
        return b

    def __add__(self, *products):  # метод пополнения списка продуктов
        b = self.__getproduct__()  # получение имеющегося списка продуктов
        a = open(self.__file_name, 'a')  # открытие файла для записи
        for i in range(len(products)):
            if products[i].name in b:  # проверка наличия нового продукта в списке имеющихся
                print('Продукт', products[i].name, 'уже есть в магазине')
            else:
                a.write(products[i].__str__() + '\n')  # пополнение файла со списком продуктов
        a.close()  # закрыли файл


# ТЕСТ ----------------------------------------------------------------------------------------------------------------

p1 = Product('Картофель', 50.1, 'Овощи')
p2 = Product('Земляника', 12.7, 'Ягоды')
p3 = Product('Яблоки', 7.9, 'Фрукты')
s1 = Shop()  # создание магазина

s1.__add__(p1,p2,p3)  # добавление ряда продуктов в список
print(s1.__getproduct__())  # посмотрим список продуктов

