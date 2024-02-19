
class Model:
    def __init__(self):
        self.length = 0
        self.height= 0
        self.width = 0

    def calculate(self, length, width, height):
        try:
            length = float(length)
            width = float(width)
            height = float(height)

            self.length = length
            self.width = width
            self.height = height

            diagonal = self.calculate_diagonal()
            volume = self.calculate_volume()
            surface_area = self.calculate_surface_area()
            return diagonal, volume, surface_area

        except ValueError:
            return None, None, None

    def calculate_diagonal(self):
        return (self.length ** 2 + self.width ** 2 + self.height ** 2) ** 0.5

    def calculate_volume(self):
        return self.length * self.width * self.height

    def calculate_surface_area(self):
        return 2 * (self.length * self.width + self.length * self.height + self.width * self.height)