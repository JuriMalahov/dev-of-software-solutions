import sys
import pickle
import LR19_classes
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from MainCircus import Ui_MainWindow
from WidgetWorker import Ui_WorkerForm
from WidgetPerformance import Ui_PerformanceForm
from WidgetTourSchedule import Ui_TourSchedForm
from WidgetPerformanceTroupe import Ui_PerformanceTroupeForm
from WidgetProgram import Ui_ProgramForm


class ListView(QtCore.QAbstractListModel):
    def __init__(self, tm_type, *args, todos=None, **kwargs):
        super(ListView, self).__init__(*args, **kwargs)
        self.list = todos or []
        self.list_type = tm_type

    def data(self, index, role):
        if role == Qt.DisplayRole:
            if self.list_type == 4:
                text = self.list[index.row()]
            else:
                obj = self.list[index.row()][1]
                if self.list_type == 0:
                    text = obj.surname+' '+obj.name+' '+obj.patronymic
                elif self.list_type == 1:
                    text = obj.name
                elif self.list_type == 2:
                    text = obj.performance
                elif self.list_type == 3:
                    text = obj.circus_actor
            return text

    def rowCount(self, index):
        return len(self.list)


class WorkerWidget(QtWidgets.QWidget, Ui_WorkerForm):
    def __init__(self, obj_list, index=None):
        super(WorkerWidget, self).__init__()
        self.setupUi(self)
        self.setFixedSize(391, 513)
        self.obj_list = obj_list
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.show()
        self.index = index
        self.okButton.clicked.connect(self.add)
        self.cancelButton.clicked.connect(self.close)
        self.gender = ''
        self.gender1.toggled.connect(self.set_gender)
        self.gender2.toggled.connect(self.set_gender)
        self.database = LR19_classes.CircusWorkerDatabase()
        if self.index:
            self.change()

    def change(self):
        worker = self.obj_list.list[self.index.row()][1]
        self.surnameEdit.setText(worker.surname)
        self.nameEdit.setText(worker.name)
        self.patronymicEdit.setText(worker.patronymic)
        self.birthyearEdit.setText(worker.birth_year)
        self.admissionyearEdit.setText(worker.admission_year)
        self.workexperienceEdit.setText(worker.work_experience)
        self.postEdit.setText(worker.post)
        self.gender = worker.gender
        if worker.gender == 'мужской':
            self.gender1.setChecked(True)
        else:
            self.gender2.setChecked(True)
        self.addressEdit.setText(worker.address)
        self.cityEdit.setText(worker.city)
        self.phoneEdit.setText(worker.phone)
        self.performanceEdit.setText(worker.perf_troupe.performance)

    def set_gender(self):
        rb = self.sender()
        if rb.isChecked():
            self.gender = rb.text()
            print(self.gender)

    def add(self):
        worker_data = [self.surnameEdit.text(), self.nameEdit.text(), self.patronymicEdit.text(),
                       self.birthyearEdit.text(), self.admissionyearEdit.text(),
                       self.workexperienceEdit.text(), self.postEdit.text(), self.gender,
                       self.addressEdit.text(), self.cityEdit.text(), self.phoneEdit.text(),
                       self.performanceEdit.text()]
        phone_wrong = False
        for i in self.phoneEdit.text():
            if i not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
                phone_wrong = True
        if len(self.phoneEdit.text()) != 11:
            phone_wrong = True
        if '' not in worker_data and not phone_wrong:
            self.database.add_circus_worker(self.surnameEdit.text(), self.nameEdit.text(),
                                            self.patronymicEdit.text(), self.birthyearEdit.text(),
                                            self.admissionyearEdit.text(), self.workexperienceEdit.text(),
                                            self.postEdit.text(), self.gender,
                                            self.addressEdit.text(), self.cityEdit.text(),
                                            self.phoneEdit.text(), self.performanceEdit.text())
            if self.index:
                self.obj_list.list[self.index.row()] = [self.phoneEdit.text(),
                                                        self.database.database[self.phoneEdit.text()]]
            else:
                self.obj_list.list.append([self.phoneEdit.text(),
                                           self.database.database[self.phoneEdit.text()]])
            self.obj_list.layoutChanged.emit()
            self.save()
            self.close()
        elif '' in worker_data:
            self.err_msg.setText('Введены не все данные')
        elif phone_wrong:
            self.err_msg.setText('Неправильно введен номер телефона')

    def save(self):
        database = {}
        for i in self.obj_list.list:
            database[i[0]] = i[1]
        with open('circus_workers.pkl', 'wb') as f:
            pickle.dump(database, f)


class PerformanceWidget(QtWidgets.QWidget, Ui_PerformanceForm):
    def __init__(self, obj_list, index=None):
        super(PerformanceWidget, self).__init__()
        self.setupUi(self)
        self.setFixedSize(391, 374)
        self.obj_list = obj_list
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.show()
        self.index = index
        self.okButton.clicked.connect(self.add)
        self.cancelButton.clicked.connect(self.close)
        self.database = LR19_classes.CircusPerformanceDatabase()
        if self.index:
            self.change()

    def change(self):
        perf = self.obj_list.list[self.index.row()][1]
        self.nameEdit.setText(perf.name)
        self.producerEdit.setText(perf.producer)
        self.prod_designerEdit.setText(perf.production_designer)
        self.cond_directorEdit.setText(perf.conductor_director)
        self.authorEdit.setText(perf.author)
        self.genreEdit.setText(perf.genre)
        self.typeEdit.setText(perf.type)

    def add(self):
        perf_data = [self.nameEdit.text(), self.producerEdit.text(), self.prod_designerEdit.text(),
                     self.cond_directorEdit.text(), self.authorEdit.text(),
                     self.genreEdit.text(), self.typeEdit.text()]
        if '' not in perf_data:
            self.database.add_circus_performance(self.nameEdit.text(), self.producerEdit.text(),
                                                 self.prod_designerEdit.text(), self.cond_directorEdit.text(),
                                                 self.authorEdit.text(), self.genreEdit.text(), self.typeEdit.text())
            if self.index:
                self.obj_list.list[self.index.row()] = [self.nameEdit.text(),
                                                        self.database.database[self.nameEdit.text()]]
            else:
                self.obj_list.list.append([self.nameEdit.text(),
                                           self.database.database[self.nameEdit.text()]])
            self.obj_list.layoutChanged.emit()
            self.save()
            self.close()
        elif '' in perf_data:
            self.err_msg.setText('Введены не все данные')

    def save(self):
        database = {}
        for i in self.obj_list.list:
            database[i[0]] = i[1]
        with open('circus_performance.pkl', 'wb') as f:
            pickle.dump(database, f)


class TourScheduleWidget(QtWidgets.QWidget, Ui_TourSchedForm):
    def __init__(self, obj_list, index=None):
        super(TourScheduleWidget, self).__init__()
        self.setupUi(self)
        self.setFixedSize(391, 412)
        self.obj_list = obj_list

        self.locations = ListView(4)
        self.listView.setModel(self.locations)

        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.show()
        self.index = index
        self.okButton.clicked.connect(self.add)
        self.cancelButton.clicked.connect(self.close)
        self.addButton.clicked.connect(self.add_loc)
        self.delButton.clicked.connect(self.delete)
        self.database = LR19_classes.CircusTourScheduleDatabase()
        if self.index:
            self.change()

    def add_loc(self):
        self.locations.list.append(self.locationEdit.text())
        self.locationEdit.setText('')
        self.locations.layoutChanged.emit()

    def delete(self):
        indexes = self.listView.selectedIndexes()
        if indexes:
            index = indexes[0]
            del self.locations.list[index.row()]
            self.locations.layoutChanged.emit()
            self.listView.clearSelection()
            self.save()

    def change(self):
        perf = self.obj_list.list[self.index.row()][1]
        self.performanceEdit.setText(perf.performance)
        self.startEdit.setText(perf.start_date)
        self.endEdit.setText(perf.end_date)
        for loc in perf.location:
            self.locations.list.append(loc)
        self.locations.layoutChanged.emit()

    def add(self):
        perf_data = [self.performanceEdit.text(), self.startEdit.text(), self.endEdit.text()]
        if '' not in perf_data and self.locations.list != []:
            self.database.add_circus_tour_schedule(self.performanceEdit.text(), self.startEdit.text(),
                                                   self.endEdit.text(), self.locations.list)
            if self.index:
                self.obj_list.list[self.index.row()] = [self.performanceEdit.text(),
                                                        self.database.database[self.performanceEdit.text()]]
            else:
                self.obj_list.list.append([self.performanceEdit.text(),
                                           self.database.database[self.performanceEdit.text()]])
            self.obj_list.layoutChanged.emit()
            self.save()
            self.close()
        elif '' in perf_data or self.locations.list == []:
            self.err_msg.setText('Введены не все данные')

    def save(self):
        database = {}
        for i in self.obj_list.list:
            database[i[0]] = i[1]
        with open('circus_tour_schedule.pkl', 'wb') as f:
            pickle.dump(database, f)


class PerformanceTroupeWidget(QtWidgets.QWidget, Ui_PerformanceTroupeForm):
    def __init__(self, obj_list, index=None):
        super(PerformanceTroupeWidget, self).__init__()
        self.setupUi(self)
        self.setFixedSize(391, 323)
        print('gg')
        self.obj_list = obj_list
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.show()
        self.index = index
        self.okButton.clicked.connect(self.add)
        self.cancelButton.clicked.connect(self.close)
        self.database = LR19_classes.CircusPerformanceTroupeDatabase()
        if self.index:
            self.change()

    def change(self):
        perf = self.obj_list.list[self.index.row()][1]
        self.performanceEdit.setText(perf.performance)
        actor = perf.circus_actor.split(' ')
        self.surnameEdit.setText(actor[0])
        self.nameEdit.setText(actor[1])
        self.patronymicEdit.setText(actor[2])
        self.roleEdit.setText(perf.role_name)

    def add(self):
        perf_data = [self.performanceEdit.text(), self.surnameEdit.text(), self.nameEdit.text(),
                     self.patronymicEdit.text(), self.roleEdit.text()]
        if '' not in perf_data:
            actor = self.surnameEdit.text()+' '+self.nameEdit.text()+' '+self.patronymicEdit.text()
            self.database.add_circus_performance_troupe(self.performanceEdit.text(), self.surnameEdit.text(),
                                                        self.nameEdit.text(), self.patronymicEdit.text(),
                                                        self.roleEdit.text())
            if self.index:
                self.obj_list.list[self.index.row()] = [actor,
                                                        self.database.database[actor]]
            else:
                self.obj_list.list.append([actor,
                                           self.database.database[actor]])
            self.obj_list.layoutChanged.emit()
            self.save()
            self.close()
        elif '' in perf_data:
            self.err_msg.setText('Введены не все данные')

    def save(self):
        database = {}
        for i in self.obj_list.list:
            database[i[0]] = i[1]
        with open('circus_performance_troupe.pkl', 'wb') as f:
            pickle.dump(database, f)


class ProgramWidget(QtWidgets.QWidget, Ui_ProgramForm):
    def __init__(self, obj_list, index=None):
        super(ProgramWidget, self).__init__()
        self.setupUi(self)
        self.setFixedSize(391, 431)
        self.obj_list = obj_list

        self.daystime = ListView(4)
        self.listView.setModel(self.daystime)

        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.show()
        self.index = index
        self.okButton.clicked.connect(self.add)
        self.cancelButton.clicked.connect(self.close)
        self.addButton.clicked.connect(self.add_daystime)
        self.delButton.clicked.connect(self.delete)
        self.database = LR19_classes.CircusProgramDatabase()
        if self.index:
            self.change()

    def add_daystime(self):
        self.daystime.list.append(self.daystimeEdit.text())
        self.daystimeEdit.setText('')
        self.daystime.layoutChanged.emit()

    def delete(self):
        indexes = self.listView.selectedIndexes()
        if indexes:
            index = indexes[0]
            del self.daystime.list[index.row()]
            self.daystime.layoutChanged.emit()
            self.listView.clearSelection()
            self.save()

    def change(self):
        prog = self.obj_list.list[self.index.row()][1]
        self.performanceEdit.setText(prog.performance)
        self.startdateEdit.setText(prog.date)
        self.periodEdit.setText(prog.period)
        self.priceEdit.setText(str(prog.ticket_price))
        for dt in prog.days_time:
            self.daystime.list.append(dt)
        self.daystime.layoutChanged.emit()

    def add(self):
        prog_data = [self.performanceEdit.text(), self.startdateEdit.text(), self.periodEdit.text(),
                     self.priceEdit.text()]
        price_wrong = False
        for i in self.priceEdit.text():
            if i not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
                price_wrong = True
        if '' not in prog_data and self.daystime.list != [] and not price_wrong:
            self.database.add_circus_program(self.performanceEdit.text(), self.startdateEdit.text(),
                                             self.periodEdit.text(), self.daystime.list, self.priceEdit.text())
            if self.index:
                self.obj_list.list[self.index.row()] = [self.performanceEdit.text(),
                                                        self.database.database[self.performanceEdit.text()]]
            else:
                self.obj_list.list.append([self.performanceEdit.text(),
                                           self.database.database[self.performanceEdit.text()]])
            self.obj_list.layoutChanged.emit()
            self.save()
            self.close()
        elif '' in prog_data or self.daystime.list == []:
            self.err_msg.setText('Введены не все данные')
        elif price_wrong:
            self.err_msg.setText('Неправильно введена цена билета')

    def save(self):
        database = {}
        for i in self.obj_list.list:
            database[i[0]] = i[1]
        with open('circus_program.pkl', 'wb') as f:
            pickle.dump(database, f)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setFixedSize(331, 305)
        self.obj_list = ListView(tm_type=0)
        self.objView.setModel(self.obj_list)
        self.choosetype.addItems(['Workers', 'Performances', 'Tour schedules',
                                  'Performance troupes', 'Programs'])
        self.load()
        self.choosetype.currentIndexChanged.connect(self.load)
        self.addButton.clicked.connect(self.open_form)
        self.changeButton.clicked.connect(self.open_form_changing)
        self.delButton.clicked.connect(self.delete)

    def open_form(self):
        if self.choosetype.currentText() == 'Workers':
            self.form = WorkerWidget(self.obj_list)
        elif self.choosetype.currentText() == 'Performances':
            self.form = PerformanceWidget(self.obj_list)
        elif self.choosetype.currentText() == 'Tour schedules':
            self.form = TourScheduleWidget(self.obj_list)
        elif self.choosetype.currentText() == 'Performance troupes':
            self.form = PerformanceTroupeWidget(self.obj_list)
        elif self.choosetype.currentText() == 'Programs':
            self.form = ProgramWidget(self.obj_list)

    def open_form_changing(self):
        indexes = self.objView.selectedIndexes()
        if indexes:
            index = indexes[0]
            if self.choosetype.currentText() == 'Workers':
                self.form = WorkerWidget(self.obj_list, index)
            elif self.choosetype.currentText() == 'Performances':
                self.form = PerformanceWidget(self.obj_list, index)
            elif self.choosetype.currentText() == 'Tour schedules':
                self.form = TourScheduleWidget(self.obj_list, index)
            elif self.choosetype.currentText() == 'Performance troupes':
                self.form = PerformanceTroupeWidget(self.obj_list, index)
            elif self.choosetype.currentText() == 'Programs':
                self.form = ProgramWidget(self.obj_list, index)

    def delete(self):
        indexes = self.objView.selectedIndexes()
        if indexes:
            index = indexes[0]
            del self.obj_list.list[index.row()]
            self.obj_list.layoutChanged.emit()
            self.objView.clearSelection()
            self.save()

    def load(self):
        if self.choosetype.currentText() == 'Workers':
            filename = 'circus_workers.pkl'
            self.obj_list = ListView(0)
        elif self.choosetype.currentText() == 'Performances':
            filename = 'circus_performance.pkl'
            self.obj_list = ListView(1)
        elif self.choosetype.currentText() == 'Tour schedules':
            filename = 'circus_tour_schedule.pkl'
            self.obj_list = ListView(2)
        elif self.choosetype.currentText() == 'Performance troupes':
            filename = 'circus_performance_troupe.pkl'
            self.obj_list = ListView(3)
        elif self.choosetype.currentText() == 'Programs':
            filename = 'circus_program.pkl'
            self.obj_list = ListView(2)
        self.objView.setModel(self.obj_list)
        try:
            with open(filename, 'rb') as f:
                database = pickle.load(f)
                for i in database.keys():
                    self.obj_list.list.append([i, database[i]])
                self.obj_list.layoutChanged.emit()
        except Exception:
            pass

    def save(self):
        database = {}
        if self.choosetype.currentText() == 'Workers':
            filename = 'circus_workers.pkl'
        elif self.choosetype.currentText() == 'Performances':
            filename = 'circus_performance.pkl'
        elif self.choosetype.currentText() == 'Tour schedules':
            filename = 'circus_tour_schedule.pkl'
        elif self.choosetype.currentText() == 'Performance troupes':
            filename = 'circus_performance_troupe.pkl'
        elif self.choosetype.currentText() == 'Programs':
            filename = 'circus_program.pkl'
        for i in self.obj_list.list:
            database[i[0]] = i[1]
        with open(filename, 'wb') as f:
            pickle.dump(database, f)


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
