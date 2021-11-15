import turtle as t
from settings import Settings


class Constellation:
    """Рисует созвездие"""

    def __init__(self, name):
        self.name = name
        self.settings = Settings()
        self._draw_point_name()
        self._set_position_start_line()
        self._draw_line()
        self._draw_name_constellation()

    @staticmethod
    def _draw_point(x, y):
        t.hideturtle()
        t.penup()
        t.setposition(x, y)
        t.dot(10, 'red')

    @staticmethod
    def _draw_name(star_name):
        t.left(90)
        t.forward(10)
        t.left(90)
        t.forward(30)
        t.write(star_name, font=('Arial', 18, 'normal'))
        t.right(180)

    def _draw_point_name(self):
        if self.name == 'ORION':
            for key, value in self.settings.orion_point_coordinate.items():
                self._draw_point(value[0], value[1])
                self._draw_name(key)

    @staticmethod
    def _set_position_start_line():
        t.hideturtle()
        t.setposition(-90, -180)
        t.pendown()
        t.pencolor('red')

    def _draw_line(self):
        if self.name == 'ORION':
            for key, value in self.settings.orion_line_coordinate.items():
                t.setposition(value[0], value[1])

    def _draw_name_constellation(self):
        t.penup()
        t.setposition(-300, 280)
        t.pencolor('red')
        t.speed(1)
        x = 280
        for letter in self.name:
            if letter == 'I':
                x += 10
            t.write(letter, font=('Arial', 22, 'normal'))
            t.setposition(-x, 280)
            x -= 20


class Orion(Constellation):
    pass
