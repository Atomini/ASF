from model import Model
from view import View


class Controller:

    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def add_button_click(self):
        """Срабативает при нажатиии кнопки Добавить, добавляет строку со значениями в TableWidget"""
        current = self.view.current_select()    # получает значения из полей
        result = self.model.select_from_db(current)      # передает значения в модель и возвращает результаты
        self.view.add_date_in_table(result)

    def recomend_pipe(self, dy):
        """Срабативаеит при изменениях в combobox_dy. передает в модель текущее значение комбобокса"""
        return self.model.select_recomend_pipe(dy)

    def save_button_click(self):
        """ Срабативает при нпжатии кнопки сохранить, записивает дание в файл exel"""
        data = self.view.save_data_to_exel()
        self.model.save_to_exel(data)


    # must be last
    def start(self):
        self.view.main()


if __name__ == '__main__':
    controller = Controller()

    # must be last
    controller.start()
