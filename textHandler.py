from matrixHandler import *
import sys


BLACK = "000000"
WHITE = "ffffff"
BLUE = "0000FF"
RED = "FF0000"

class CharMatrix:
    def __init__(self, name, charwidth):
        self.name = name
        self.charwidth = charwidth
        self.matrix = []




    def __str__(self):
        data = ""
        for row in self.matrix:
            data += " ".join(row) + "\n"
        return data
    
        


class TextHandler:
    #Prepares letters in row for matrixEngine


    def __init__(self, path_to_font="fonts.dat"):

        self.load_font(path_to_font)


    def load_font(self, path):
        f = open(path, "r")

        exec(f.read())      # Creates variable 'fonts' with dictionary-based data structure

        self.font = {}

        f.close()

        for name in fonts:
            biggiest_width = 0

            for line in fonts[name]:
                if len(line) > biggiest_width:
                    biggiest_width = len(line)

            
            

            char = CharMatrix(name, biggiest_width)
            char.matrix = fonts[name]
                    
            print char
                    
            self.font[name] = char
                    
                    


    def make_text(self, text, start_poscol=0, start_posrow=1, space_between=0, color="ffffff"):

        print "Making text:" + text.encode("utf-8")
        #Makes MatrixObject sequence
        
        objects = []

        textwidth = 0
        
        poscol = start_poscol
        posrow = start_posrow
        for letter in text:

            print letter.encode("utf-8")

            print letter in self.font
            
            
            if letter in self.font:
                charMatrix = self.font[letter]
                objects.append(MatrixObject(charMatrix.matrix, posrow, poscol, "*", color))                
                poscol += charMatrix.charwidth + space_between
                textwidth += charMatrix.charwidth + space_between



        return objects, textwidth
                

        
            
        



        
        


if __name__=="__main__":

    textHandler = TextHandler()
    print textHandler.font["a"]
    print textHandler.font["h"]
    print textHandler.font["o"]
    print textHandler.font["j"]

    text, textwidth = textHandler.make_text("Hello world", 16)     #Text is shifted 16 pixels horizonataly to right

    engine = MatrixEngine(text) #Creates Engine object with text 'Hello world'



    
    for i in range(300):
        engine.shift_left()
        engine.get_matrix(cycle=True, cycle_size_col = textwidth+16) 
        engine.print_matrix()
    

