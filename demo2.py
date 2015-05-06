import svetelny_panel
from textHandler import *
from matrixHandler import *

svetelny_panel.setup()

textHandler = TextHandler()

textToView = raw_input("Text to view:")

text, textwidth = textHandler.make_text(textToView, 16, 1, color=BLUE)     #Text is shifted 16 pixels horizonataly to right

engine = MatrixEngine(text) #Creates Engine object with text 'Hello world'



    
while True:
    engine.shift_left()
    matrix = engine.get_matrix(cycle=True, cycle_size_col = textwidth+16)
    svetelny_panel.set_panel_memory_from_matrix(matrix)
    
    
    #engine.print_matrix()



    
