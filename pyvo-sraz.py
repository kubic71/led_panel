import svetelny_panel, colors, time
from textHandler import *
from matrixHandler import *


#Moving text demo

svetelny_panel.setup()

textHandler = TextHandler()

def show_text(text, text_color, delay=0.1):
    text, width = textHandler.make_text(text  , x_shift=16, y_shift=1, color=text_color)
    engine = MatrixEngine(text)


    last = time.time()
    for i in range(width + 16):
        engine.shift_left()
        matrix = engine.get_matrix(cycle_x=False)   #Moving text


        #Wait unit time delay reached
        while True:
            if time.time() - last > delay:
                last = time.time()
                break
            
        svetelny_panel.set_panel_memory_from_matrix(matrix)


show_text("Pyvo", colors.RED1)
show_text("50. sraz", colors.GREEN)
show_text("Pyvec - gymgeek     Studenti gymnazia Roudnice zdravi python komunitu!", colors.PURPLE)


