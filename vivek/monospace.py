from manimlib.imports import *
import numpy as np

class Code(Scene):
    def construct(self):
        #text = TextMobject("\\normalfont\\dejavumono Hello")
        #text = TextMobject("\\normalfont\\textnormal abc def ghi jklmn")
        text = TextMobject("\\normalfont\\texttt{abc def ghi jklmn}")
        text1 = TextMobject("$for (i = 0; i  10; i++)$")
        VGroup(text, text1).arrange(DOWN)
        self.play(Write(text), Write(text1))
        
