from graph import Graph


# ШАБЛОНЫ ОТРИСОВКИ ГРАФИКОВ
# Очистка и подпись графика (вызывается в начале)
def cleaning_and_chart_graph(graph: Graph, x_label, y_label, title):
    graph.toolbar.home()  # Возвращаем зум в домашнюю позицию
    graph.toolbar.update()  # Очищаем стек осей (от старых x, y lim)
    # Очищаем график
    graph.axis.clear()
    # Задаем название осей
    graph.axis.set_xlabel(x_label)
    graph.axis.set_ylabel(y_label)
    # Задаем название графика
    graph.axis.set_title(title)


# Отрисовка (вызывается в конце)
def draw_graph(graph: Graph, chart_caption: bool = True):
    # Рисуем сетку
    graph.axis.grid()
    # Инициирует отображение наименований графиков (label plot)
    if chart_caption:
        graph.axis.legend()
    # Убеждаемся, что все помещается внутри холста
    graph.figure.tight_layout()
    # Показываем новую фигуру в интерфейсе
    graph.canvas.draw()


# Отрисовка при отсутствии данных
def no_data(graph: Graph):
    graph.axis.text(0.5, 0.5, "Нет данных",
                    fontsize=14,
                    horizontalalignment='center',
                    verticalalignment='center')
    # Отрисовка, без подписи данных графиков
    draw_graph(graph, chart_caption=False)


# Класс художник. Имя холст (graph), рисует на нем данные
class Drawer:
    # ПАРАМЕТРЫ ГРАФИКОВ
    # График №1 Данные
    title_data = "График №1. Данные с исследуемым веществом и без вещества"
    horizontal_axis_name_data = "Частота [МГц]"
    vertical_axis_name_data = "Гамма [усл.ед.]"

    name_without_gas = "Без вещества"
    color_without_gas = "#515151"

    # ОТРИСОВКИ
    # (1) Без данных и с данными
    @staticmethod
    def updating_gas_graph(
            graph: Graph,
            data_x=None,
            data_y=None
    ):
        # Очистка, подпись графика и осей (вызывается в начале)
        cleaning_and_chart_graph(
            # Объект графика
            graph=graph,
            # Название графика
            title=Drawer.title_data,
            # Подпись осей
            x_label=Drawer.horizontal_axis_name_data, y_label=Drawer.vertical_axis_name_data
        )

        # Данных нет
        if not data_x or not data_y:
            no_data(graph)
            return

        # Рисуем график
        graph.axis.plot(
            data_x,
            data_y,
            color=Drawer.color_without_gas, label=Drawer.name_without_gas)

        # Отрисовка (вызывается в конце)
        draw_graph(graph)
