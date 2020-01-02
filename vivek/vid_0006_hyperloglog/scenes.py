from manimlib.imports import *

class Opening(Scene):
    def construct(self):
        text = TextMobject("Computer Science by Pandey")
        subtext = TextMobject("One video: One snack sized topic")
        logo = ImageMobject("logo/website_logo_transparent_background.png").scale(1.5)
        text.next_to(logo, DOWN, buff=3*SMALL_BUFF)
        subtext.next_to(text, DOWN)
        self.play(FadeIn(logo), FadeIn(text), FadeIn(subtext))
        self.wait(2)
        self.play(FadeOut(logo), FadeOut(text), FadeOut(subtext))

class LargeList(MovingCameraScene):
    def setup(self):
        MovingCameraScene.setup(self)

    def construct(self):
        dist = 3.5 * SMALL_BUFF
        N = 25
        suffixes = [i for i in range(N)]
        elems = [TexMobject("X_{" + str(s) + "}") for s in suffixes]
        elem_group = VGroup(*elems).arrange(RIGHT, buff=dist)
        elem_group.to_edge(LEFT)
        hi = TextMobject("hi")
        hi.to_edge(TOP + LEFT)
        self.play(Write(elem_group), Write(hi))

        self.camera_frame.generate_target()
        self.camera_frame.target.shift(12 * RIGHT)

        hi.generate_target()
        hi.target.shift(12 * RIGHT)
        self.play(MoveToTarget(self.camera_frame), MoveToTarget(hi))

