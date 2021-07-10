"""A CLI program to draw ASCII art! Add rectangles and squares to a canvas."""


class Canvas():

    def __init__(self, height:int=10, width:int=10):
        self.height = height
        self.width = width
        self.rectangles = []


    def render_canvas(self):
        """Print out the canvas in the cmd line.
        
        The canvas is a matrix of whitespaces."""
        
        for i in range(self.height):
            # Making rows lists because they're mutable so 
            # updating the row with chars from rectangles
            # is more efficient. Before printing I need to 
            # join them!
            row  = [" "] * self.width

            # If there are shapes on the canvas, loop
            # through them and add their characters.
            for rectangle in self.rectangles:
                if rectangle.start_y <= i <= rectangle.end_y:
                    # Slice the part of the canvas covered by
                    # the rectangle. Update the characters in
                    # slice to those specified by the rectangle
                    # instance.
                    row[rectangle.start_x: rectangle.end_x] = [rectangle.fill_char] * (rectangle.end_x - rectangle.start_x)

            print(" ".join(row))

    def add_rectangle(self, rectangle):
        """Add rectangle to canvas."""
        self.rectangles.append(rectangle)
        

    def clear_canvas(self):
        """Removes all rectangles from canvas."""

        self.rectangles = []

    def __repr__(self):
        return f'Canvas dimensions: {self.width}x{self.height}. n rectangles: {len(self.rectangles)}'


class Rectangle():

    def __init__(self, start_x:int, start_y:int, end_x:int, end_y:int, fill_char:str):
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.fill_char = str(fill_char)

    def update_char(self, char):
        self.fill_char = str(char)

    def __repr__(self):
        return f'Rectangle dim: {self.end_x - self.start_x}x{self.end_y - self.start_y}.'


if __name__ == "__main__":
    mycanvas = Canvas(12,10)
    mycanvas.render_canvas()
    print(mycanvas)
    rectangle1 = Rectangle(2,1,5,7,'*')
    rectangle2 = Rectangle(1, 1,3,3,'&')
    print(rectangle1, rectangle2)
    mycanvas.add_rectangle(rectangle1)
    mycanvas.add_rectangle(rectangle2)
    print(mycanvas)
    mycanvas.render_canvas()