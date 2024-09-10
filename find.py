class WordFinder:
    def __init__(self, *filename):
        self.file_names = filename

    def __p_minus__(self, string):  # метод удаления знаков препинания
        a = ''
        for i in string:  # перебор знаков строки
            zpf = 0  # флаг обнаружения знака препинания (обнуление)
            for p in '.,:;!?=-':  # перебор знаков препинания
                if i == p:  # проверка на совпадение со знаком препинания
                    zpf = 1
                    break
            if zpf == 1:  # проверка флага обнаруженного знака препинания
                continue
            else:
                a = a + i
        return a

    def __get_all_words__(self):  # метод формирования словаря
        a = {}
        for i in self.file_names:
            with open(i, 'r', encoding='utf-8') as b:
                a[i] = self.__p_minus__(b.read().lower()).split() # удаление зп/понижение рег-ра/разбиение по пробелам
        return a

    def __find__(self, word):  # метод поиска слова
        a = self.__get_all_words__()  # получили словарь
        b = {}
        for fail in list(a.keys()):  # перебор ключей
            poz = 1  # позиционный счётчик
            for i in a[fail]:  # перебор слов в файлах
                if i == word:  # проверка на совпадение слов
                    b[fail] = poz
                    break
                else:
                    poz = poz + 1  # инкремент позиционного счётчика
        if b == {}:
            return 'Слово не найдено'
        else:
            return b

    def __count__(self, word):  # метод подсчёта найденных слов
        a = self.__get_all_words__()  # получили словарь
        b = {}
        for fail in list(a.keys()):  # перебор ключей
            poz = 0  # счётчик совпавших слов
            for i in a[fail]:  # перебор слов в файлах
                if i == word:  # проверка на совпадение слов
                    poz = poz + 1  # инкремент счётчика совпавших слов
                    b[fail] = poz
        if b == {}:
            return 'Слово не найдено'
        else:
            return b

# ТЕСТ ----------------------------------------------------------------------------------------------------------------

finder = WordFinder('f1.txt','f2.txt','f3.txt')

print(finder.__get_all_words__())

print(finder.__find__('детали'))

print(finder.__count__('детали'))