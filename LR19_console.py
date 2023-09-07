# coding: utf-8
from LR19_classes import *


class CircusTerm:
    def __init__(self):
        self.circus_worker_database = CircusWorkerDatabase()
        self.circus_performance_database = CircusPerformanceDatabase()
        self.circus_tour_schedule_database = CircusTourScheduleDatabase()
        self.circus_performance_troupe_database = CircusPerformanceTroupeDatabase()
        self.circus_program_database = CircusProgramDatabase()

    def print_worker_db(self):
        for worker in self.circus_worker_database:
            print('worker name {0} phone {1}'.format(worker.fullname, worker.phone))

    def print_performance_db(self):
        for performance in self.circus_performance_database:
            print('name {0} producer {1}'.format(performance.name, performance.producer))

    def print_tour_schedule_db(self):
        for tour_schedule in self.circus_tour_schedule_database:
            print('performance {0} date {1}-{2}'.format(tour_schedule.performance, tour_schedule.start_date,
                                                        tour_schedule.end_date))

    def print_performance_troupe_db(self):
        for performance_troupe in self.circus_performance_troupe_database:
            print('circus actor {0} performance {1}'.format(performance_troupe.circus_actor,
                                                            performance_troupe.performance))

    def print_program_db(self):
        for program in self.circus_program_database:
            print('performance {0} date {1} price {2}'.format(program.performance, program.period,
                                                              program.ticket_price))

    def run(self):
        choice = 0
        choices = {
            1: lambda: self.print_worker_db(),
            2: lambda: self.circus_worker_database.add_circus_worker(input('surname: '), input('name: '),
                                                                     input('patronymic: '), input('birth_year: '),
                                                                     input('admission_year: '),
                                                                     input('work_experience: '), input('post: '),
                                                                     input('gender: '), input('address: '),
                                                                     input('city: '), input('phone: '),
                                                                     input('performance: ')),
            3: lambda: self.circus_worker_database.delete_worker(input('enter phone: ')),
            4: lambda: self.circus_worker_database.change_address(input('enter phone: '),
                                                                  input('enter address: '),
                                                                  input('enter city: ')),
            5: lambda: self.print_performance_db(),
            6: lambda: self.circus_performance_database.add_circus_performance(input('name: '), input('producer: '),
                                                                               input('production designer: '),
                                                                               input('conductor director: '),
                                                                               input('author: '), input('genre: '),
                                                                               input('type: ')),
            7: lambda: self.circus_performance_database.delete_performance(input('enter name: ')),
            8: lambda: self.print_tour_schedule_db(),
            9: lambda: self.circus_tour_schedule_database.add_circus_tour_schedule(input('performance: '),
                                                                                   input('start_date: '),
                                                                                   input('end_date: '),
                                                                                   input('location: ')),
            10: lambda: self.circus_tour_schedule_database.delete_tour_schedule(input('enter performance: ')),
            11: lambda: self.circus_tour_schedule_database.change_start_date(input('enter performance: '),
                                                                             input('enter date: ')),
            12: lambda: self.circus_tour_schedule_database.change_end_date(input('enter performance: '),
                                                                           input('enter date: ')),
            13: lambda: self.print_performance_troupe_db(),
            14: lambda: self.circus_performance_troupe_database.add_circus_performance_troupe(input('performance: '),
                                                                                              input('surname: '),
                                                                                              input('name: '),
                                                                                              input('patronymic: '),
                                                                                              input('role_name: ')),
            15: lambda: self.circus_performance_troupe_database.delete_performance_troupe(input
                                                                                          ('enter circus actor: ')),
            16: lambda: self.print_program_db(),
            17: lambda: self.circus_program_database.add_circus_program(input('performance: '), input('start_date: '),
                                                                        input('end_date: '), input('days_time: '),
                                                                        input('ticket_price: ')),
            18: lambda: self.circus_program_database.delete_program(input('enter performance: ')),
            19: lambda: self.circus_program_database.change_price(input('enter performance: '),
                                                                  input('enter price: '))
        }
        while choice != 20:
            print()
            print('1. print worker database')
            print('2. add worker')
            print('3. delete worker')
            print('4. change worker address')
            print('5. print performance database')
            print('6. add performance')
            print('7. delete performance')
            print('8. print tour schedule database')
            print('9. add tour schedule')
            print('10. delete tour schedule')
            print('11. change tour schedule start date')
            print('12. change tour schedule end date')
            print('13. print performance troupe database')
            print('14. add performance troupe')
            print('15. delete performance troupe')
            print('16. print program database')
            print('17. add program')
            print('18. delete program')
            print('19. change program ticket price')
            print('20. EXIT')
            print('choose:')
            choice = int(input())
            if choice in choices:
                choices[choice]()


if __name__ == '__main__':
    CircusTerm().run()
