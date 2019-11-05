from manimlib.imports import *
import numpy as np
from vivek.vid_0003_selection_sort.sortable import Sortable

class Array(Scene, Sortable):
    def setup(self):
        nums = [23, 28, 14, 33, 20, 17, 25]
        self.seq = [n for n in range(len(nums))]
        num_elems = len(nums)
        squares = [Square(side_length=1) for i in range(num_elems)]
        self.boxes = VGroup(*squares).arrange(RIGHT, buff=0)
        num_mobjects = [TextMobject(str(num)) for num in nums]
        self.array = VGroup(*num_mobjects).arrange(RIGHT, buff=5.5*SMALL_BUFF)
        indices = [TextMobject(str(i)) for i in range(num_elems)]
        self.index_array = VGroup(*indices).arrange(RIGHT, buff=8*SMALL_BUFF)
        self.index_array.next_to(self.array, DOWN, buff=0.8)
        self.items = self.array

    def construct(self):
        self.play(Write(self.boxes))
        self.play(Write(self.array))
        self.play(Write(self.index_array))
        self.move(4, 2)
        
