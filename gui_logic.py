import matplotlib
from PyQt5 import QtWidgets

from gui import Ui_Dialog
from drawing.drawer import Drawer as drawer

matplotlib.use('TkAgg')


class GuiProgram(Ui_Dialog):
    """ Класс контроллер - интерпретирует действия пользователя """

    def __init__(self, dialog: QtWidgets.QDialog) -> None:
        """ Вызывается при создании нового объекта класса """
        # Создание окна
        Ui_Dialog.__init__(self)
        # Установка пользовательского интерфейс
        self.setupUi(dialog)

        # ПОЛЯ КЛАССА
        # Параметры 1 графика
        self.drawer_1 = drawer(
            layout=self.layout_plot_1,
            widget=self.widget_plot_1
        )

        # ДЕЙСТВИЯ ПРИ ВКЛЮЧЕНИИ
        # Для примера, рисуем первичные данные
        self.draw()

    def draw(self):
        """ Рисуем график """
        x = list(range(5))
        y = list(range(5))
        self.drawer_1.draw_line(x, y)
