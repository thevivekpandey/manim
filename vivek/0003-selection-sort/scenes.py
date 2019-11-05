from manimlib.imports import *
import numpy as np

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

class Scene1(Scene):
    def construct(self):
        text = TextMobject("Computer Science by Pandey")

        subtext = TextMobject("One video: One snack sized topic")
        VGroup(text, subtext).arrange(DOWN)
        self.play(Write(text))
        self.wait(5)
        self.play(Write(subtext))
        self.wait(15)
        self.play(FadeOut(text), FadeOut(subtext))
 
class Scene2(Scene):
    def update_seq(self, target, pos):
        saved = self.seq[target]
        for i in range(target, pos, -1):
            self.seq[i] = self.seq[i - 1]
        self.seq[pos] = saved

    def move(self, target, pos):
        target_stick = self.stick_men[self.seq[target]]
        pos_stick = self.stick_men[self.seq[pos]]

        target_stick.generate_target()
        target_stick.target.next_to(target_stick, UP)
        self.play(MoveToTarget(target_stick))

        target_stick.generate_target()
        target_stick.target.next_to(pos_stick, LEFT + UP)
        self.play(MoveToTarget(target_stick))

        target_stick.generate_target()
        target_stick.target.next_to(pos_stick, LEFT)
        self.play(MoveToTarget(target_stick))

        self.stick_men[self.seq[target - 1]].generate_target()
        self.stick_men[self.seq[target - 1]].target.next_to(self.stick_men[self.seq[target - 1]], RIGHT, buff=0.6*LARGE_BUFF )
        self.play(MoveToTarget(self.stick_men[self.seq[target - 1]]))

        for i in range(target - 2, pos - 1, -1):
            self.stick_men[self.seq[i]].generate_target()
            self.stick_men[self.seq[i]].target.next_to(self.stick_men[self.seq[i + 1]], LEFT, buff=0.6*LARGE_BUFF )
            self.play(MoveToTarget(self.stick_men[self.seq[i]]))
         
        target_stick.generate_target()
        target_stick.target.next_to(pos_stick, LEFT, buff=0.6*LARGE_BUFF )
        self.play(MoveToTarget(target_stick))
        self.update_seq(target, pos)

    def construct(self):

        platform = Line(LEFT, RIGHT)
        platform.set_width(8)
        platform.to_edge(DOWN, buff = 2.95 * LARGE_BUFF)
        platform.to_edge(RIGHT)
        self.play(Write(platform))

        nums = [23, 28, 14, 33, 20, 17, 25]
        self.seq = [n for n in range(len(nums))]
        lengths = [num / 20 for num in nums]
        self.stick_men = VGroup(*[StickMan(l) for l in lengths]).arrange(RIGHT, buff = 0.6 * LARGE_BUFF, aligned_edge = DOWN)
        self.stick_men.to_edge(RIGHT)
        self.play(Write(self.stick_men))

        self.move(1, 0)
        self.wait(2)
