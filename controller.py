from model import Model
from view import View


class Controller:

    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def add_button_click(self):
        current = self.view.current_select()
        self.model.select_from_db(current)

    def recomend_pipe(self, dy):
        return self.model.select_recomend_pipe(dy)




    # must be last
    def start(self):
        self.view.main()


if __name__ == '__main__':
    controller = Controller()

    # must be last
    controller.start()
