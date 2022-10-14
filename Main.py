#!/usr/bin/env python3
# coding=utf-8

import sys
from random import randint

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('uis/main.ui', self)  # загрузка формы в py-скрипт

        self.setWindowTitle('Работа с визуальными табличными данными в Python')
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))

        self.btn_random_number.clicked.connect(self.fill_random_numbers)
        self.btn_solve.clicked.connect(self.solve)

    def fill_random_numbers(self):

        row = 0
        col = 0

        # заполняем таблицу случайными числами
        while row < self.tableWidget.rowCount():
            while col < self.tableWidget.columnCount():
                random_num = randint(-10, 10)
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(random_num)))
                col += 1
            row += 1
            col = 0


    def solve(self):
            # -*- решение задания -*-
            count = 0  # количество единиц, стоящих перед нашим числом
            for i in range(self.tableWidget.rowCount()):
                for j in range(self.tableWidget.columnCount()):
                    if int(self.tableWidget.item(i, j).text()) == 0:
                        count += 1
            self.label_sum.setText("Количество нулей: " + str(count))

            if count != 0:
                for i in range(self.tableWidget.rowCount()):
                    for j in range(self.tableWidget.columnCount()):
                        print(i, j)
                        if int(self.tableWidget.item(i, j).text()) % 2 != 0:
                            self.tableWidget.setItem(i, j, QTableWidgetItem(str(count)))
            else:
                self.label_error.setText("Нет нулей ")

def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
