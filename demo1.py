# -*- coding: utf-8 -*-
import svetelny_panel
from textHandler import *
from matrixHandler import *

svetelny_panel.setup()

textHandler = TextHandler()
#text, textwidth = textHandler.make_text("Sedi dva smutni informatici v serverovne, prijde k nim treti a pta se:- Proc jste tak smutni? - No vcera jsme se trosku ozrali a menili jsme hesla..", 16)     #Text is shifted 16 pixels horizonataly to right

text, textwidth = textHandler.make_text("Už Ý Á É umíme háčky i čárky!".decode("utf-8"), 16)     #Text is shifted 16 pixels horizonataly to right

engine = MatrixEngine(text) #Creates Engine object with text 'Hello world'



    
while True:
    engine.shift_left()
    matrix = engine.get_matrix(cycle=True, cycle_size_col = textwidth+16)
    svetelny_panel.set_panel_memory_from_matrix(matrix)
    
    #engine.print_matrix()



    
