CLI program that allows the user to create minimalistic ASCII art. 

Checkout and run program:
```
git clone git@github.com:torasirkka/ascii-art-generator.git
cd ascii-art-generator
python3 main.py
```

API:

- Canvas(height,width) instantiates a canvas object.
    - add_rectangle(rectangle) adds a rectangle object to list of rectangles to be rendered on the canvas.
    - clear_canvas() removes all rectangles from the canvas.
- Rectangle(start_x, start_y, end_x, end_y, fill_char) instantiates rectangle object.
    - update_char(char) updates the fill character of a rectangle object.
    - translate(axis, num) translates a rectangle object along the x (axis=0) or y (axis=1) axis.