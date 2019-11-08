from manimlib.imports import *
import numpy as np
from vivek.vid_0003_selection_sort.sortable import Sortable

class Limb(VGroup):
    def __init__(self, back, side, t, **kwargs):
        super().__init__(**kwargs)
        self.back = back
        assert side in ['left', 'right']
        assert t in ['arm', 'leg']
        self.length = 0.4
        if side == 'left':
            self.angle = PI / 4
        else:
            self.angle = -PI / 4

        if t == 'arm':
            self.shift = self.back.get_length() / 4
        else:
            self.shift = self.back.get_length()

    def create_limb(self):
        limb = Line(UP, DOWN)
        limb.set_height(self.length)
        limb.move_to(self.back.get_start())
        limb.shift(DOWN * (self.length / 2.0))
        limb.rotate(self.angle, about_point = self.back.get_start())
        limb.shift(DOWN * self.shift)
        return limb

class StickMan(VGroup):
    CONFIG = {
        "head_diameter": 0.25,
        "head_style": {
            "stroke_width": 0,
            "fill_opacity": 1,
            "fill_color": GREY_BROWN,
            "sheen_direction": UL,
            "sheen_factor": 0.5,
            "background_stroke_color": BLACK,
            "background_stroke_width": 3,
            "background_stroke_opacity": 0.5,
        },
        "back_style": {
            "stroke_width": 3,
            "stroke_color": LIGHT_GREY,
            "sheen_direction": UP,
            "sheen_factor": 1,
        },
    }

    def __init__(self, length, **kwargs):
        super().__init__(**kwargs)
        self.length = length
        self.create_stick_man()
        self.update()

    def create_stick_man(self):
        back = Line(UP, DOWN)
        back.set_height(self.length)
        back.set_style(**self.back_style)
        self.add(back)

        head = Circle()
        head.set_width(self.head_diameter)
        head.set_style(**self.head_style)
        head.move_to(back.get_start())
        self.add(head)

        left_arm = Limb(back, 'left', 'arm').create_limb()
        self.add(left_arm)

        right_arm = Limb(back, 'right', 'arm').create_limb()
        self.add(right_arm)

        left_leg= Limb(back, 'left', 'leg').create_limb()
        self.add(left_leg)

        right_leg= Limb(back, 'right', 'leg').create_limb()
        self.add(right_leg)

class Children(Scene, Sortable):
    def move_stick_man(self, target, pos):
        self.stick_men[self.seq[target]].set_color(RED)
        self.move(target, pos)

    def show_little_arrow_and_remark(self):
        pass

    def construct(self):
        self.nums = nums = [23, 20, 17, 14, 28, 33, 25]
        self.seq = [n for n in range(len(nums))]
        lengths = [num / 20 for num in nums]
        self.stick_men = VGroup(*[StickMan(l) for l in lengths]).arrange(RIGHT, buff = 0.6 * LARGE_BUFF, aligned_edge = DOWN)
        self.items = self.stick_men #to propagate to Sortable class
        self.multiple = 1.17
        self.delta = 0.5
        self.adjust = True
        
        self.platform = Line(LEFT, RIGHT)
        self.platform.set_width(8)
        self.platform.to_edge(DOWN, buff = 2.95 * LARGE_BUFF)
        self.play(Write(self.platform))
        self.play(Write(self.stick_men))

        #self.move_stick_man(2, 0)
        #self.move_stick_man(5, 1)
        #self.move_stick_man(5, 2)
        #self.move_stick_man(6, 4)

        self.platform.generate_target()
        self.platform.target.shift(2 * UP)
        
        self.stick_men.generate_target()
        self.stick_men.target.shift(2 * UP)

        self.play(MoveToTarget(self.platform), MoveToTarget(self.stick_men))


        num_elems = len(self.nums)
        squares = [Square(side_length=1.15) for i in range(num_elems)]
        self.boxes = VGroup(*squares).arrange(RIGHT, buff=0)
        self.boxes.next_to(self.platform, DOWN, buff=LARGE_BUFF)
        num_mobjects = [TextMobject(str(num)) for num in self.nums]
        self.array = VGroup(*num_mobjects).arrange(RIGHT, buff=6.8*SMALL_BUFF)
        self.array.next_to(self.platform, DOWN, buff=14 * SMALL_BUFF)
    
        self.play(Write(self.boxes))

        transforms = [Transform(self.stick_men[i], self.array[i]) for i in range(num_elems)]
        transforms.append(FadeOut(self.platform))
        self.play(*transforms)

        # Reset for array play
        self.nums = nums = [23, 20, 17, 14, 28, 33, 25]
        self.delta = 0
        self.adjust = False
        self.seq = [n for n in range(len(nums))]
        self.stick_men = self.array
        self.move_stick_man(4, 1)

        self.show_little_arrow_and_remark()
