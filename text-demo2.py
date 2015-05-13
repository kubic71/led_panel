import svetelny_panel, colors
from textHandler import *
from matrixHandler import *


#Moving text demo

svetelny_panel.setup()

textHandler = TextHandler()

textToView = raw_input("Text to view:")

text, textwidth = textHandler.make_text(textToView, x_shift=16, y_shift=0, color=colors.PINK)     #Text is shifted 16 pixels horizonataly to right at the very beggining

engine = MatrixEngine(text) #Creates Engine object with text from 'textToView' variable



    
while True:
    engine.shift_left()
    matrix = engine.get_matrix(cycle_x=True, cycle_size_x = textwidth+16)   #Moving text
    svetelny_panel.set_panel_memory_from_matrix(matrix)
    
    #engine.print_matrix()  #Prints matrix to console



    
