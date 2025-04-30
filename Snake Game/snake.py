from turtle import  Turtle

class Snake:

    __STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0), (-60, 0), (-80, 0)]
    __UP = 90
    __DOWN = 270
    __LEFT = 180
    __RIGHT = 0
    def __init__(self):
        self._segments = []
        self.create_snake()
        self.__heading =  self._segments[0]

    def create_snake(self):
        for position in self.__STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self._segments.append(new_segment)

    def move(self):
        for seg_number in range(len(self._segments) - 1 , 0 , -1):
            new_x = self._segments[seg_number - 1].xcor()
            new_y = self._segments[seg_number - 1].ycor()
            self._segments[seg_number].goto(new_x, new_y)
        self.__heading.forward(20)

    def  up(self):
        if self.__heading.heading() != self.__DOWN:
            self.__heading.setheading(self.__UP)

    def down(self):
        if self.__heading.heading() != self.__UP:
            self.__heading.setheading(self.__DOWN)

    def left(self):
        if self.__heading.heading() != self.__RIGHT:
            self.__heading.setheading(self.__LEFT)

    def    right(self):
        if self.__heading.heading() != self.__LEFT:
            self.__heading.setheading(self.__RIGHT)