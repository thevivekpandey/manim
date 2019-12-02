from manimlib.imports import *

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

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_stick_man()

    def set_color(self, color):
        a1 = ApplyMethod(self.back.set_color, color)
        a2 = ApplyMethod(self.head.set_color, color)
        a3 = ApplyMethod(self.left_arm.limb.set_color, color)
        a4 = ApplyMethod(self.right_arm.limb.set_color, color)
        a5 = ApplyMethod(self.left_leg.limb.set_color, color)
        a6 = ApplyMethod(self.right_leg.limb.set_color, color)
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

        self.left_arm = left_arm = Limb(back, 'left', 'arm')
        left_arm.create_limb()
        self.add(left_arm.limb)

        self.right_arm = right_arm = Limb(back, 'right', 'arm')
        right_arm.create_limb()
        self.add(right_arm.limb)

        self.left_leg = left_leg = Limb(back, 'left', 'leg')
        left_leg.create_limb()
        self.add(left_leg.limb)

        self.right_leg = right_leg = Limb(back, 'right', 'leg')
        right_leg.create_limb()
        self.add(right_leg.limb)

