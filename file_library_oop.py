import csv
import  os

class A:


    # Ввести и вернуть цифру меню
    def show_menu(self):
        print("Выберите необходимое действие:")
        print("1. Отобразить весь справочник")
        print("2. Найти абонента по фамилии")
        print("3. Найти абонента по номеру телефона")
        print("4. Добавить абонента в справочник")
        print("5. Сохранить справочник в текстовом формате")
        print("6. Изменить данные")
        print("7. Закончить работу") 
        self.choice = int(input('Введите цифру: '))
        return self.choice
    

    # функция выведет на экран список всех файлов из папки files
    def get_list_files(self):
        self.list_files=os.listdir('files') # получить список всех файлов
        print() # пустая строка
        print('Гена, вот тот самый список всех файлов который ты просил...... ')
        for i in self.list_files:
            print(i)

  
    # функция принимает на вход полное имя файла
    # и выводин на экран содержимое этого файла
    def get_show_data(self, name_file):
        self.name_file=name_file
        print()
        self.file_path=os.path.join('files',self.name_file)
        with open(self.file_path,'r',encoding='1251', newline='') as self.file: # получим данные
            self.data=list(csv.reader(self.file, delimiter=';')) #переменная с данными таблицы в виде списка
            self.n=len(self.data[0])*[0] # определим количество столбцов, оно равно первой строки и создадим список
            
            # # заполним список максимальными значениями каждого столбца по длинне слов
            for i in range(len(self.n)): # итерация по слобцам
                self.temp=[] # создам пустой список
                for k in range(len(self.data)): # итерация по строкам
                    self.temp.append(len(self.data[k][i]))
                self.n[i]=max(self.temp)+1 # запишем значение с длинной в наш список

            # Выведем на печать первую строку и подчеркнем ее 
            for k in range(len(self.n)):
                print(self.data[0][k].ljust(self.n[k]), end='')
            print()
            # ВНИМАНИЕ!!! Здесь надо разобраться почему длинна тире не сходится с длинной сроки
            # код можно написат короче
            for k in range(len(self.n)):
                for j in range(self.n[k]):
                    print('-', end='')
            print()

            # Выведем на печать нашу матрицу с учетом длинны слов со второй строки
            for i in range(1,len(self.data)):
                for k in range(len(self.n)):
                    print(self.data[i][k].ljust(self.n[k]), end='')  
                print()
            return

    # метод принимает название файла в качестве параметра и возвращает данные файла в виде списка
    def get_return_data_list(self,name_file):
        self.name_file=name_file
        self.file_path=os.path.join('files',self.name_file)
        with open(self.file_path,'r',encoding='1251', newline='') as self.file: # получим данные
            self.data=list(csv.reader(self.file, delimiter=';')) #переменная с данными таблицы в виде списка
        return self.data

    # метод который принимает список и название файла и записывает в него данные
    def writer_in_file(self, lst=None, file=''):
        if lst is not None:
            self.lst = lst  # передаем данные в виде списка
        self.file = file
        full_path = os.path.join('files', self.file)
        try:
            with open(full_path, 'w+', newline='', encoding='1251') as f:
                writer = csv.writer(f, delimiter=';')  # используем точку с запятой в качестве разделителя
                for i in self.lst:
                    writer.writerow(i)
                print(f"Данные записаны в файл {self.file}")
        except Exception as e:
            print(f"Произошла ошибка при записи в файл: {e}")

        


