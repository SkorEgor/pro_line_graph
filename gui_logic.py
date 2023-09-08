from gui import Ui_Dialog

from graph import Graph
from drawer import Drawer as drawer

import matplotlib

matplotlib.use('TkAgg')


# КЛАСС АЛГОРИТМА ПРИЛОЖЕНИЯ
class GuiProgram(Ui_Dialog):

    def __init__(self, dialog):
        # Создаем окно
        Ui_Dialog.__init__(self)
        self.setupUi(dialog)  # Устанавливаем пользовательский интерфейс

        # ПОЛЯ КЛАССА
        # Параметры 1 графика
        self.graph_1 = Graph(
            layout=self.layout_plot_1,
            widget=self.widget_plot_1
        )

        # ДЕЙСТВИЯ ПРИ ВКЛЮЧЕНИИ
        # Для примера, от рисуем первичные данные
        self.draw()

    def draw(self):
        x = list(range(5))
        y = list(range(5))
        drawer.updating_gas_graph(self.graph_1, x, y)
