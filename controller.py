from model import Model
from view import View


class Controller:

    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def start_app(self):
        app = self.view


if __name__ == '__main__':
    controller = Controller()
    controller.start_app()
