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
        self.limb = limb
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

    def set_color(self, color):
        a1 = ApplyMethod(self.back.set_color, color)
        a2 = ApplyMethod(self.head.set_color, color)
        a3 = ApplyMethod(self.left_arm.set_color, color)
        a4 = ApplyMethod(self.right_arm.set_color, color)
        a5 = ApplyMethod(self.left_leg.set_color, color)
        a6 = ApplyMethod(self.right_leg.set_color, color)
        return [a1, a2, a3, a4, a5, a6]

    def create_stick_man(self):
        back = Line(UP, DOWN)
        back.set_height(self.length)
        back.set_style(**self.back_style)
        self.add(back)
        self.back = back

        head = Dot(radius=0.15)
        head.move_to(back.get_start())
        self.add(head)
        self.head = head

        left_arm = Limb(back, 'left', 'arm').create_limb()
        self.add(left_arm)
        self.left_arm = left_arm

        right_arm = Limb(back, 'right', 'arm').create_limb()
        self.add(right_arm)
        self.right_arm = right_arm

        left_leg= Limb(back, 'left', 'leg').create_limb()
        self.add(left_leg)
        self.left_leg = left_leg

        right_leg= Limb(back, 'right', 'leg').create_limb()
        self.add(right_leg)
        self.right_leg = right_leg

class Children(Scene, Sortable):
    def move_stick_man(self, target, pos, partial=False, set_color=True):
        self.play(*self.stick_men[self.seq[target]].set_color(RED))
        self.move(target, pos, partial)

    def make_little_arrow_and_remark(self):
        self.arrows = []
        for i in range(4):
            a = Arrow()
            a.set_length(0.5)
            a.set_color(YELLOW)
            self.arrows.append(a)
        self.g = VGroup(*self.arrows).arrange(RIGHT, buff=0.70*LARGE_BUFF)
        self.b = Brace(self.g, DOWN)
        self.text = TextMobject("Multiple shifts")
        self.tot = VGroup(self.b, self.text).arrange(DOWN)
        self.tot.next_to(self.boxes[1], DOWN + 0.5 * RIGHT)
        self.b1 = Brace(self.tot, RIGHT)
     
        self.play(FadeIn(self.tot))
        self.play(FadeIn(self.b1))
  
    def construct(self):
        #Start: 00:28
        #Step 1: Children play
        self.nums = nums = [23, 25, 33, 28, 14, 17, 20]
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
        self.wait(12) #00:42

        self.move_stick_man(4, 0)
        self.wait(1) #00:52
        self.move_stick_man(5, 1)
        self.wait(2) #01:02
        self.move_stick_man(6, 2)
        self.play(*self.stick_men[self.seq[3]].set_color(RED))
        self.play(*self.stick_men[self.seq[4]].set_color(RED))
        self.move_stick_man(6, 5)
        self.play(*self.stick_men[self.seq[6]].set_color(RED))

        self.wait(4) #1:27
        self.platform.generate_target()
        self.platform.target.shift(2 * UP)
        
        self.stick_men.generate_target()
        self.stick_men.target.shift(2 * UP)

        self.play(MoveToTarget(self.platform), MoveToTarget(self.stick_men))

        # Step 2: array play
        num_elems = len(self.nums)
        squares = [Square(side_length=1.15) for i in range(num_elems)]
        self.boxes = VGroup(*squares).arrange(RIGHT, buff=0)
        self.boxes.next_to(self.platform, DOWN, buff=LARGE_BUFF)
        num_mobjects = [TextMobject(str(num)) for num in self.nums]
        self.array = VGroup(*num_mobjects).arrange(RIGHT, buff=6.8*SMALL_BUFF)
        self.array.next_to(self.platform, DOWN, buff=14 * SMALL_BUFF)
    
        #self.play(Write(self.boxes))
        self.play(FadeIn(self.boxes))

        transforms = [Transform(self.stick_men[i], self.array[i]) for i in range(num_elems)]
        transforms.append(FadeOut(self.platform))
        self.play(*transforms)
        self.wait(7)

        self.nums = nums = [23, 25, 33, 28, 14, 17, 20]
        self.multiple = 1.17
        self.delta = 0
        self.adjust = False
        self.seq = [n for n in range(len(nums))]
        #self.items1 = self.array
        self.move_stick_man(4, 0, set_color=False)
        self.move_stick_man(5, 1, partial=True, set_color=False)

        self.make_little_arrow_and_remark()
        self.wait(10)
        self.move_left(1, 4)
        self.wait(2)
        self.target_move_down_and_right(1, 5)
        self.target_move_up_down(1, 5)
        self.seq[1], self.seq[5] = self.seq[5], self.seq[1]

        self.wait(6)
        self.play(*self.stick_men[self.seq[6]].set_color(RED))
        self.swap(6, 2)
        self.play(*self.stick_men[self.seq[5]].set_color(RED))
        self.swap(5, 3)
        self.play(*self.stick_men[self.seq[6]].set_color(RED))
        self.swap(6, 4)
        self.play(*self.stick_men[self.seq[6]].set_color(RED))
        self.swap(6, 5)
        self.play(*self.stick_men[self.seq[6]].set_color(RED))

        self.wait(60)
        return
        #self.swap(5, 6)
        #self.swap(4, 6)
        #self.swap(3, 5)
        #self.swap(2, 6)
        #self.swap(1, 5)
        #self.swap(0, 4)

        #Step 3 Now the algo will be shown
        self.boxes.generate_target()
        self.boxes.target.shift(UP)

        #self.stick_men1.generate_target()
        #self.stick_men1.target.shift(UP)

        self.array.generate_target()
        self.array.target.shift(UP)

        self.play(FadeOut(self.boxes), FadeOut(self.array), FadeOut(self.stick_men))
