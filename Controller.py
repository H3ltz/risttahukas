from Model import Model
from View import View


class Controller:
    def __init__(self):
        self.model = Model() #mudel
        self.view = View(self)

    def calculate(self, values):
        self.view.btn_arvuta['state'] = 'normal'
        length, width, height = values
        diagonal, volume, surface_area = self.model.calculate(length, width, height)
        result_text = f"Diagonaal: {diagonal:.2f}, Ruumala: {volume:.2f}, Täis pindala: {surface_area:.2f}"
        self.view.set_result(result_text, values)
