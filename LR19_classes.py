# coding: utf-8
from datetime import datetime
import pickle
import time


def method_time(func):
    def wrapper_t(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        runtime = time.perf_counter() - start
        print(runtime)
    return wrapper_t


def method_counter(func):
    def wrapper_c(*args, **kwargs):
        wrapper_c.count += 1
        func(*args, **kwargs)
    wrapper_c.count = 0
    return wrapper_c


class Circus_workers(object):
    """Класс Circus_workers хранит следующие атрибуты: фамилия, имя, отчество, год рождения, год поступления на работу,
стаж, должность, пол, адрес, город, телефон."""
    def __init__(self, surname, name, patronymic, birth_year,
                 admission_year, work_experience, post,
                 gender, address, city, phone, performance=None):
        self.__surname = surname
        self.__name = name
        self.__patronymic = patronymic
        self.__birth_year = birth_year
        self.__admission_year = admission_year
        self.__work_experience = work_experience
        self.__post = post
        if gender == 'мужской' or gender == 'женский':
            self.__gender = gender
        else:
            raise InvalidGenderError(gender)
        self.__address = address
        self.__city = city
        if len(phone) == 11:
            self.__phone = phone
        else:
            raise InvalidPhoneError(phone)
        self.__queue = []
        self.perf_troupe = Circus_performance_troupe(performance, surname, name, patronymic, post)
        self.__fullname = self.__surname + ' ' + self.__name + ' ' + self.__patronymic

    def __add__(self, x):
        """Метод __add__ увеличивает стаж работы."""
        self.__work_experience += x

    @property
    def surname(self):
        return self.__surname

    @property
    def name(self):
        return self.__name

    @property
    def patronymic(self):
        return self.__patronymic

    @property
    def fullname(self):
        return self.__fullname

    @property
    def birth_year(self):
        return self.__birth_year

    @property
    def admission_year(self):
        return self.__admission_year

    @property
    def work_experience(self):
        return self.__work_experience

    @property
    def post(self):
        return self.__post

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, val):
        if not (val == 'мужской' or val == 'женский'):
            raise InvalidGenderError(val)

    @property
    def address(self):
        return self.__address

    @property
    def city(self):
        return self.__city

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, val):
        if len(val) != 11:
            raise InvalidPhoneError(val)

    @property
    def queue(self):
        return self.__queue

    @property
    def age_at_admission(self):
        return self.__age_at_admission

    @property
    def change_phone(self):
        return self.__change_phone

    @property
    def change_address(self):
        return self.__change_address

    def __str__(self):
        '''Метод __str__ выводит имя, телефон и адрес.'''
        return 'name: {0}, phone: {1}, address: {2}'.format(self.__name, self.__phone, self.__address + ' ' +
                                                            self.__city)

    @method_counter
    @method_time
    def __change_phone(self, new_phone):
        '''Метод __change_phone меняет номер телефона объекта.'''
        if len(new_phone) != 11:
            raise InvalidPhoneError(new_phone)
        else:
            self.__phone = new_phone
            self.__queue.append(Circus_transaction(new_phone, 'change_phone'))

    @method_counter
    @method_time
    def __change_address(self, new_address, new_city):
        '''Метод __change_address меняет адрес объекта.'''
        self.__address = new_address
        self.__city = new_city

    @method_counter
    @method_time
    def __age_at_admission(self):
        '''Метод __age_at_admission выводит возраст, в котором работник поступил на работу.'''
        age = self.__admission_year - self.__birth_year
        if age % 10 == 1:
            y = 'года'
        else:
            y = 'лет'
        self.__queue.append(Circus_transaction(age, 'age_at_admission'))
        return(self.__surname + ' ' + self.__name + ' ' + self.__patronymic +
               ' поступил(а) на работу в возрасте ' + str(age) + ' ' + y + '.')

    def __get_transaction(self):
        '''Метод __get_transaction выводит информацию о транзакции.'''
        for i in range(len(self.__queue)):
            item = self.__queue.pop(0)
            print('when {0} : operation {1}, value {2} \n'.format(item.when, item.operation, item.value))

    def __del__(self):
        '''Удаление объекта.'''
        print('Object Circus_workers destroyed')


class InvalidPhoneError(Exception):
    '''Класс InvalidPhoneError выводит ошибку ввода номера телефона.'''
    def __init__(self, phone):
        self.phone = phone

    def __str__(self):
        return 'invalid phone {0}'.format(self.phone)


class InvalidGenderError(Exception):
    '''Класс InvalidGenderError выводит ошибку ввода пола.'''
    def __init__(self, gender):
        self.gender = gender

    def __str__(self):
        return 'invalid gender {0}'.format(self.gender)


class WorkerPlaceOfLiving(Circus_workers):
    '''Класс WorkerPlaceOfLiving наследует атрибуты от объекта класса Circus_workers.'''
    def __init__(self, surname, name, patronymic, birth_year,
                 admission_year, work_experience, post,
                 gender, address, city, phone, country='', work_phone=''):
        super(WorkerPlaceOfLiving, self).__init__(surname, name, patronymic, birth_year, admission_year,
                                                  work_experience, post, gender, address, city, phone)
        self.__name = name
        self.__country = country
        self.__work_phone = work_phone

    @property
    def country(self):
        return self.__country

    @property
    def work_phone(self):
        return self.__work_phone

    @property
    def change_phone(self):
        return self.__change_phone

    @property
    def change_address(self):
        return self.__change_address

    def __str__(self):
        return 'name: {0}, address: {1}'.format(self.__surname + ' ' + self.__name + ' ' + self.__patronymic,
                                                self.__address + ', ' + self.__city + ', ' + self.__country)

    @method_counter
    @method_time
    def __change_phone(self, new_phone, new_work_phone):
        '''Метод __change_phone меняет номера телефона объекта.'''
        self.__phone = new_phone
        self.__work_phone = new_work_phone
        self.__queue.append(Circus_transaction(new_phone, 'change_phone'))

    @method_counter
    @method_time
    def __change_address(self, new_address, new_city, new_country):
        '''Метод __change_address меняет адрес объекта.'''
        self.__address = new_address
        self.__city = new_city
        self.__country = new_country


class Circus_performance():
    '''Класс Circus_performance хранит следующие атрибуты: название, режиссер-постановщик, художник-постановщик,
дирижер-постановщик, автор, жанр, тип.'''
    def __init__(self, name, producer, production_designer,
                 conductor_director, author, genre, type):
        self.__name = name
        self.__producer = producer
        self.__production_designer = production_designer
        self.__conductor_director = conductor_director
        self.__author = author
        self.__genre = genre
        self.__type = type
        self.__queue = []

    @property
    def name(self):
        return self.__name

    @property
    def producer(self):
        return self.__producer

    @property
    def production_designer(self):
        return self.__production_designer

    @property
    def conductor_director(self):
        return self.__conductor_director

    @property
    def author(self):
        return self.__author

    @property
    def genre(self):
        return self.__genre

    @property
    def type(self):
        return self.__type

    @property
    def queue(self):
        return self.__queue

    @property
    def prod(self):
        return self.__prod

    @method_counter
    @method_time
    def __prod(self):
        '''Метод __prod выводит режиссёра-постановщика представления.'''
        return self.__producer+' - режиссёр-постановщик представления "'+self.__name+'".'

    def __del__(self):
        print('Object Circus_performance destroyed')


class Circus_tour_schedule():
    '''Класс Circus_tour_schedule хранит следующие атрибуты: представление, дата начала, дата окончания,
места проведения гастролей.'''
    def __init__(self, performance, start_date, end_date,
                 location):
        self.__performance = performance
        self.__start_date = start_date
        self.__end_date = end_date
        self.__location = location
        self.__queue = []
        self.program = Circus_program(performance, start_date, start_date+'-'+end_date)

    @property
    def performance(self):
        return self.__performance

    @property
    def start_date(self):
        return self.__start_date

    @property
    def end_date(self):
        return self.__end_date

    @property
    def location(self):
        return self.__location

    @property
    def queue(self):
        return self.__queue

    @property
    def change_end_date(self):
        return self.__change_end_date

    @property
    def change_start_date(self):
        return self.__change_start_date

    @method_counter
    @method_time
    def __change_start_date(self, date):
        '''Метод __change_start_date меняет дату начала проведения гастролей.'''
        self.__start_date = date
        self.__queue.append(Circus_transaction(date, 'change_start_date'))

    @method_counter
    @method_time
    def __change_end_date(self, date):
        '''Метод __change_end_date меняет дату окончания проведения гастролей.'''
        self.__end_date = date
        self.__queue.append(Circus_transaction(date, 'change_end_date'))

    def __get_transaction(self):
        '''Метод __get_transaction выводит информацию о транзакции.'''
        for i in range(len(self.__queue)):
            item = self.__queue.pop(0)
            print('when {0} : operation {1}, value {2} \n'.format(item.when, item.operation, item.value))

    def __del__(self):
        print('Object Circus_tour_schedule destroyed')


class Circus_performance_troupe():
    '''Класс Circus_performance_troupe хранит следующие атрибуты: представление, актер цирка, название роли.'''
    def __init__(self, performance='', surname='', name='', patronymic='', role_name=''):
        self.__performance = performance
        self.__circus_actor = surname + ' ' + name + ' ' + patronymic
        self.__role_name = role_name
        self.__queue = []

    @property
    def performance(self):
        return self.__performance

    @property
    def circus_actor(self):
        return self.__circus_actor

    @property
    def role_name(self):
        return self.__role_name

    @property
    def queue(self):
        return self.__queue

    @property
    def in_perf(self):
        return self.__in_perf

    @method_counter
    @method_time
    def __in_perf(self):
        '''Метод __in_perf выводит информацию о том, в каком представлении участвует актер.'''
        return self.__circus_actor+' участвует в представлении "'+self.__performance+'".'

    def __del__(self):
        print('Object Circus_performance_troupe destroyed')


class Circus_program():
    '''Класс Circus_program хранит следующие атрибуты: представление, дата премьеры, период проведения, дни и время,
цена билета.'''
    def __init__(self, performance='', start_date='', period='', days_time=None,
                 ticket_price=0):
        self.perf_troupe = Circus_performance_troupe(performance)
        self.__performance = performance
        self.__date = start_date
        self.__period = period
        self.__days_time = days_time
        self.__ticket_price = int(ticket_price)
        self.__queue = []

    @method_counter
    @method_time
    def __add__(self, x):
        '''Метод __add__ увеличивает цену билета на введенное значение.'''
        self.__ticket_price += x

    @method_counter
    @method_time
    def __sub__(self, x):
        '''Метод __sub__ уменьшает цену билета на введенное значение.'''
        self.__ticket_price -= x

    @method_counter
    @method_time
    def __mul__(self, x):
        '''Метод __mul__ умножает цену билета на введенное значение.'''
        self.__ticket_price *= x

    @method_counter
    @method_time
    def __truediv__(self, x):
        '''Метод __truediv__ делит цену билета на введенное значение.'''
        self.__ticket_price /= x

    @property
    def performance(self):
        return self.__performance

    @property
    def date(self):
        return self.__date

    @property
    def period(self):
        return self.__period

    @property
    def days_time(self):
        return self.__days_time

    @property
    def ticket_price(self):
        return self.__ticket_price

    @property
    def queue(self):
        return self.__queue

    @property
    def change_price(self):
        return self.__change_price

    @method_counter
    @method_time
    def __change_price(self, new_price):
        '''Метод __change_price меняет стоимость билета.'''
        self.__ticket_price = int(new_price)
        '''if self.__ticket_price % 10 == 1:
            w = 'рубль'
        else:
            w = 'рублей'
        self.__queue.append(Circus_transaction(self.__ticket_price, 'change_price'))
        return('Цена билета на '+self.__performance+' изменена. Новая стоимость - '+str(self.__ticket_price)+' '+w+'.')'''

    def __get_transaction(self):
        '''Метод __get_transaction выводит информацию о транзакции.'''
        for i in range(len(self.__queue)):
            item = self.__queue.pop(0)
            print('when {0} : operation {1}, value {2} \n'.format(item.when, item.operation, item.value))

    def __del__(self):
        print('Object Circus_program destroyed')


class Circus_transaction(object):
    '''Класс Circus_transaction содержит информацию о дате транзакции, операции и введенном значении.'''
    def __init__(self, value, operation):
        self.__when = datetime.today()
        self.__operation = operation
        self.__value = value
        #self.f = open('transaction.txt', 'a')

    @property
    def when(self):
        return self.__when

    @property
    def operation(self):
        return self.__operation

    @property
    def value(self):
        return self.__value

    def __del__(self):
        '''Удаляет объект и записывает информацию о транзакции в файл transaction.txt.'''
        with open('transaction.txt', 'a') as f:
            f.write('when {0} : operation {1}, value {2} \n'.format(self.__when, self.__operation, self.__value))
        #self.f.write('when {0} : operation {1}, value {2} \n'.format(self.__when, self.__operation, self.__value))
        # self.f.closed


class CircusWorkerAccount(object):
    '''Класс CircusWorkerAccount выполняет сериализацию/десериализацию объекта класса Circus_workers.'''
    @staticmethod
    def __serialize(account):
        '''Метод __serialize выполняет сериализацию объекта.'''
        with open('circus_worker_account.pkl', 'wb') as f:
            pickle.dump(account, f)
        f.closed

    @staticmethod
    def __deserialize():
        '''Метод __deserialize выполняет десериализацию объекта.'''
        with open('circus_worker_account.pkl', 'rb') as f:
            account = pickle.load(f)
        f.closed
        return account


class CircusPerformanceAccount(object):
    '''Класс CircusPerformanceAccount выполняет сериализацию/десериализацию объекта класса Circus_performance.'''
    @staticmethod
    def __serialize(account):
        '''Метод __serialize выполняет сериализацию объекта.'''
        with open('circus_performance_account.pkl', 'wb') as f:
            pickle.dump(account, f)
        f.closed

    @staticmethod
    def __deserialize():
        '''Метод __deserialize выполняет десериализацию объекта.'''
        with open('circus_performance_account.pkl', 'rb') as f:
            account = pickle.load(f)
        f.closed
        return account


class CircusTourScheduleAccount(object):
    '''Класс CircusTourScheduleAccount выполняет сериализацию/десериализацию объекта класса Circus_tour_schedule.'''
    @staticmethod
    def __serialize(account):
        '''Метод __serialize выполняет сериализацию объекта.'''
        with open('circus_tour_schedule_account.pkl', 'wb') as f:
            pickle.dump(account, f)
        f.closed

    @staticmethod
    def __deserialize():
        '''Метод __deserialize выполняет десериализацию объекта.'''
        with open('circus_tour_schedule_account.pkl', 'rb') as f:
            account = pickle.load(f)
        f.closed
        return account


class CircusPerformanceTroupeAccount(object):
    '''Класс CircusPerformanceTroupeAccount выполняет сериализацию/десериализацию объекта класса
    Circus_performance_troupe.'''
    @staticmethod
    def __serialize(account):
        '''Метод __serialize выполняет сериализацию объекта.'''
        with open('circus_performance_troupe_account.pkl', 'wb') as f:
            pickle.dump(account, f)
        f.closed

    @staticmethod
    def __deserialize():
        '''Метод __deserialize выполняет десериализацию объекта.'''
        with open('circus_performance_troupe_account.pkl', 'rb') as f:
            account = pickle.load(f)
        f.closed
        return account


class CircusProgramAccount(object):
    '''Класс CircusProgramAccount выполняет сериализацию/десериализацию объекта класса Circus_program.'''
    @staticmethod
    def __serialize(account):
        '''Метод __serialize выполняет сериализацию объекта.'''
        with open('circus_program_account.pkl', 'wb') as f:
            pickle.dump(account, f)
        f.closed

    @staticmethod
    def __deserialize():
        '''Метод __deserialize выполняет десериализацию объекта.'''
        with open('circus_program_account.pkl', 'rb') as f:
            account = pickle.load(f)
        f.closed
        return account


class CircusWorkerDatabase(object):
    def __init__(self):
        self.filename = 'circus_workers.pkl'
        self.database = {}
        self.index = 0
        try:
            self.open_database()
        except:
            self.save_database()

    phone = property(lambda self: self.database[self.index].phone)

    def __iter__(self):
        for item in self.database:
            yield self.database[item]

    def next(self):
        if self.index == len(self.database):
            raise StopIteration
        self.index = self.index + 1
        return self.database[self.index]

    def prev(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.database[self.index]

    def open_database(self):
        with open(self.filename, 'rb') as f:
            self.database = pickle.load(f)

    def save_database(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self.database, f)

    def add_circus_worker(self, surname, name, patronymic, birth_year,
                          admission_year, work_experience, post,
                          gender, address, city, phone, performance=None):
        circus_worker = Circus_workers(surname, name, patronymic, birth_year,
                                       admission_year, work_experience, post,
                                       gender, address, city, phone, performance)
        self.database[circus_worker.phone] = circus_worker
        self.save_database()

    def get_worker_by_phone(self, phone):
        if phone not in self.database:
            return None
        return self.database[phone]

    def delete_worker(self, phone):
        del self.database[phone]
        self.save_database()

    def change_address(self, phone, new_address, new_city):
        worker = self.get_worker_by_phone(phone)
        if not worker:
            raise ValueError('value does not exist')
        worker.change_address(new_address, new_city)
        self.save_database()


class CircusPerformanceDatabase(object):
    def __init__(self):
        self.filename = 'circus_performance.pkl'
        self.database = {}
        self.index = 0
        try:
            self.open_database()
        except:
            self.save_database()

    name = property(lambda self: self.database[self.index].name)

    def __iter__(self):
        for item in self.database:
            yield self.database[item]

    def next(self):
        if self.index == len(self.database):
            raise StopIteration
        self.index = self.index + 1
        return self.database[self.index]

    def prev(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.database[self.index]

    def open_database(self):
        with open(self.filename, 'rb') as f:
            self.database = pickle.load(f)

    def save_database(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self.database, f)

    def add_circus_performance(self, name, producer, production_designer,
                               conductor_director, author, genre, type):
        circus_performance = Circus_performance(name, producer, production_designer,
                                                conductor_director, author, genre, type)
        self.database[circus_performance.name] = circus_performance
        self.save_database()

    def get_performance_by_name(self, name):
        if name not in self.database:
            return None
        return self.database[name]

    def delete_performance(self, name):
        del self.database[name]
        self.save_database()


class CircusTourScheduleDatabase(object):
    def __init__(self):
        self.filename = 'circus_tour_schedule.pkl'
        self.database = {}
        self.index = 0
        try:
            self.open_database()
        except:
            self.save_database()

    performance = property(lambda self: self.database[self.index].performance)

    def __iter__(self):
        for item in self.database:
            yield self.database[item]

    def next(self):
        if self.index == len(self.database):
            raise StopIteration
        self.index = self.index + 1
        return self.database[self.index]

    def prev(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.database[self.index]

    def open_database(self):
        with open(self.filename, 'rb') as f:
            self.database = pickle.load(f)

    def save_database(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self.database, f)

    def add_circus_tour_schedule(self, performance, start_date, end_date,
                                 location):
        circus_tour_schedule = Circus_tour_schedule(performance, start_date, end_date,
                                                    location)
        self.database[circus_tour_schedule.performance] = circus_tour_schedule
        self.save_database()

    def get_tour_schedule_by_performance(self, performance):
        if performance not in self.database:
            return None
        return self.database[performance]

    def delete_tour_schedule(self, performance):
        del self.database[performance]
        self.save_database()

    def change_start_date(self, performance, date):
        tour_schedule = self.get_tour_schedule_by_performance(performance)
        if not tour_schedule:
            raise ValueError('value does not exist')
        tour_schedule.change_start_date(date)
        self.save_database()

    def change_end_date(self, performance, date):
        tour_schedule = self.get_tour_schedule_by_performance(performance)
        if not tour_schedule:
            raise ValueError('value does not exist')
        tour_schedule.change_end_date(date)
        self.save_database()


class CircusPerformanceTroupeDatabase(object):
    def __init__(self):
        self.filename = 'circus_performance_troupe.pkl'
        self.database = {}
        self.index = 0
        try:
            self.open_database()
        except:
            self.save_database()

    circus_actor = property(lambda self: self.database[self.index].circus_actor)

    def __iter__(self):
        for item in self.database:
            yield self.database[item]

    def next(self):
        if self.index == len(self.database):
            raise StopIteration
        self.index = self.index + 1
        return self.database[self.index]

    def prev(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.database[self.index]

    def open_database(self):
        with open(self.filename, 'rb') as f:
            self.database = pickle.load(f)

    def save_database(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self.database, f)

    def add_circus_performance_troupe(self, performance, surname, name, patronymic, role_name):
        circus_performance_troupe = Circus_performance_troupe(performance, surname, name, patronymic,
                                                              role_name)
        self.database[circus_performance_troupe.circus_actor] = circus_performance_troupe
        self.save_database()

    def get_performance_troupe_by_circus_actor(self, circus_actor):
        if circus_actor not in self.database:
            return None
        return self.database[circus_actor]

    def delete_performance_troupe(self, circus_actor):
        del self.database[circus_actor]
        self.save_database()


class CircusProgramDatabase(object):
    def __init__(self):
        self.filename = 'circus_program.pkl'
        self.database = {}
        self.index = 0
        try:
            self.open_database()
        except:
            self.save_database()

    performance = property(lambda self: self.database[self.index].performance)

    def __iter__(self):
        for item in self.database:
            yield self.database[item]

    def next(self):
        if self.index == len(self.database):
            raise StopIteration
        self.index = self.index + 1
        return self.database[self.index]

    def prev(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.database[self.index]

    def open_database(self):
        with open(self.filename, 'rb') as f:
            self.database = pickle.load(f)

    def save_database(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self.database, f)

    def add_circus_program(self, performance, start_date, period, days_time, ticket_price):
        circus_program = Circus_program(performance, start_date, period, days_time, ticket_price)
        self.database[circus_program.performance] = circus_program
        self.save_database()

    def get_program_by_performance(self, performance):
        if performance not in self.database:
            return None
        return self.database[performance]

    def delete_program(self, performance):
        del self.database[performance]
        self.save_database()

    def change_price(self, performance, price):
        program = self.get_program_by_performance(performance)
        if not program:
            raise ValueError('value does not exist')
        program.change_price(price)
        self.save_database()


'''circus_term = CircusProgramDatabase()
circus_term.add_circus_program('Цирк Шапито', '21.04.2021', '21.04.2021-14.05.2021', ['21.04.2021, 7:00',
                                                                                      '26.04.2021, 8:30',
                                                                                      '03.05.2021, 7:20',
                                                                                      '07.05.2021, 9:00',
                                                                                      '14.05.2021, 8:30'], 400)
circus_term.change_price('Цирк Шапито', 300)
print(circus_term.database)'''

