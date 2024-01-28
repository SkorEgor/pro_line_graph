from PyQt5 import QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)


class Graph:
    """ Класс для объектов графика"""

    def __init__(self,
                 layout: QtWidgets.QLayout,
                 widget: QtWidgets.QWidget) -> None:
        """ Инициализирует объекты графика

        :param layout: слой для отрисовки графика.
        :param widget: виджет для отрисовки график.
        """
        # Объекты графика
        self.axis = None
        self.figure = None
        self.canvas = None
        self.toolbar = None
        # Объекты UI для отрисовки графика
        self.layout = layout  # Слой - для отрисовки графика
        self.widget = widget  # Виджет - для отрисовки графика
        # Вызываем инициализацию
        self.initialize()

    def initialize(self):
        """ Инициализирует фигуру matplotlib внутри контейнера GUI.
        Вызываем только один раз для инициализации объектов графика."""

        # Создание фигуры (self.fig и self.ax)
        self.figure = Figure()  # Создание пустой фигуры
        self.axis = self.figure.add_subplot(111)  # Место для графика, вид разделения
        # Создание холста
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)
        self.canvas.draw()
        # Создание Toolbar
        self.toolbar = NavigationToolbar(self.canvas, self.widget, coordinates=True)
        self.layout.addWidget(self.toolbar)

    def zoom_area(self, x_min, x_max, y_min, y_max):
        """Приближает указанную область"""
        # На графике задаем область
        self.toolbar.push_current()  # Сохранить текущий статус zoom как домашний

        self.axis.set_xlim([x_min, x_max])
        self.axis.set_ylim([y_min, y_max])

        # Перерисовываем
        self.canvas.draw()
