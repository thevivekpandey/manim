from manimlib.imports import *
from vivek.vid_0003_selection_sort.code import Code

class BubbleSortCode(Scene):
    def construct(self):
        line1 = "for (i = 0; i < n - 1; i++) \{"
        line2 = "SPACEmin\_idx = 0"
        line3 = "SPACEfor (j = i + 1, j < n; j++) \{"
        line4 = "SPACESPACEif (arr[j] < arr[min\_idx]) \{"
        line5 = "SPACESPACESPACEmin\_idx = j"
        line6 = "SPACESPACE\}"
        line7 = "SPACE\}"
        line8 = "SPACEswap(arr[min\_idx], arr[i])"
        line9 = "\}"
        b = Code(line1, line2, line3, line4, line5, line6, line7, line8, line9)
        b.move_to(UP + LEFT)
        self.add(b)
        self.play(Write(b))
