from manimlib.imports import *
from vivek.vid_0003_selection_sort.code import Code

class Opening(Scene):
    def construct(self):
        text = TextMobject("Computer Science by Pandey")

        subtext = TextMobject("One video: One snack sized topic")
        VGroup(text, subtext).arrange(DOWN)
        self.play(Write(text))
        self.wait(1)
        self.play(Write(subtext))
        self.wait(15)
        self.play(FadeOut(text), FadeOut(subtext))

class Tree(VGroup):
    class MyEllipse(Ellipse):
        def __init__(self, **kwargs):
            CONFIG = {
                "stroke_width": 3
            }
            super().__init__(**CONFIG)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        root = self.MyEllipse()
        root.scale(0.5)
        root.to_corner(UP)

        child1 = self.MyEllipse()
        child1.scale(0.5)
        child1.next_to(root, 4 * DOWN + LEFT)

        child2 = self.MyEllipse()
        child2.scale(0.5)
        child2.next_to(root, 4 * DOWN + RIGHT)

        child11 = self.MyEllipse()
        child11.scale(0.5)
        child11.next_to(child1, 4 * DOWN + LEFT)

        child12 = self.MyEllipse()
        child12.scale(0.5)
        child12.next_to(child1, 4 * DOWN + RIGHT)

        child22 = self.MyEllipse()
        child22.scale(0.5)
        child22.next_to(child2, 4 * DOWN + RIGHT)

        child121 = self.MyEllipse()
        child121.scale(0.5)
        child121.next_to(child12, 4 * DOWN + LEFT)

        child122 = self.MyEllipse()
        child122.scale(0.5)
        child122.next_to(child12, 4 * DOWN + RIGHT)

        child1211 = self.MyEllipse()
        child1211.scale(0.5)
        child1211.next_to(child121, 4 * DOWN + LEFT)

        child1212 = self.MyEllipse()
        child1212.scale(0.5)
        child1212.next_to(child121, 4 * DOWN + RIGHT)

        arrow1 = Arrow(root.get_bottom(), child1.get_top(), stroke_width=3)
        arrow1.scale(0.8)

        arrow2 = Arrow(root.get_bottom(), child2.get_top())
        arrow2.scale(0.8)

        arrow11 = Arrow(child1.get_bottom(), child11.get_top())
        arrow11.scale(0.8)

        arrow12 = Arrow(child1.get_bottom(), child12.get_top())
        arrow12.scale(0.8)

        arrow22 = Arrow(child2.get_bottom(), child22.get_top())
        arrow22.scale(0.8)

        arrow121 = Arrow(child12.get_bottom(), child121.get_top())
        arrow121.scale(0.8)

        arrow122 = Arrow(child12.get_bottom(), child122.get_top())
        arrow122.scale(0.8)

        arrow1211 = Arrow(child121.get_bottom(), child1211.get_top())
        arrow1211.scale(0.8)

        arrow1212 = Arrow(child121.get_bottom(), child1212.get_top())
        arrow1212.scale(0.8)

        self.add(root, 
                 child1,
                 child2,
                 child11,
                 child12,
                 child22,
                 child121,
                 child122,
                 child1211,
                 child1212,
                 arrow1,
                 arrow2,
                 arrow11,
                 arrow12,
                 arrow22,
                 arrow121,
                 arrow122,
                 arrow1211,
                 arrow1212,
              )
    
class RealWorld(Scene):
    def construct(self):
        algo_world, rect1 = self.get_algo_world()
        real_world, rect2 = self.get_real_world()
        arrow = self.get_arrow(rect1, rect2)

        self.play(Write(algo_world))
        self.play(Write(rect1))

        self.play(Write(arrow))

        self.play(Write(real_world))
        self.play(Write(rect2))

    def get_algo_world(self):
        t = Tree()
        t.scale(0.5)

        squares = [Square(side_length=0.5) for i in range(7)]
        boxes = VGroup(*squares).arrange(RIGHT, buff=0)

        line1 = "for (i = 0; i < n; i++) \{"
        line2 = "SPACEfor (j = 0; j < n; j++) \{"
        line3 = "\\vdots"
        c = Code(line1, line2, line3).scale(0.7)
        self.add(c)
        
        x = VGroup(t, boxes, c).arrange(DOWN, buff = LARGE_BUFF)
        x.scale(0.9)
        x.to_edge(LEFT, buff=LARGE_BUFF)
        return x, SurroundingRectangle(x)

    def get_real_world(self):
        r1 = SVGMobject(file_name = 'eagle-svgrepo-com.svg').scale(0.5)
        r2 = SVGMobject(file_name = 'sparrow-svgrepo-com.svg').scale(0.5)
        r3 = SVGMobject(file_name = 'tree-swallow-svgrepo-com.svg').scale(0.5)
        r4 = SVGMobject(file_name = 'hummingbird-svgrepo-com.svg').scale(0.5)
        r5 = SVGMobject(file_name = 'flamingo-svgrepo-com.svg').scale(0.5)

        x1 = VGroup(r1, r2).arrange(DOWN, buff = LARGE_BUFF)
        x2 = VGroup(r3, r4, r5).arrange(DOWN, buff = LARGE_BUFF)
        y = VGroup(x1, x2).arrange(RIGHT, buff = LARGE_BUFF)
        y.to_edge(RIGHT, buff=10*SMALL_BUFF + LARGE_BUFF)
        rect2 = SurroundingRectangle(y, buff=6*SMALL_BUFF)
        return y, rect2

    def get_arrow(self, rect1, rect2):
        return Arrow(rect1.get_right(), rect2.get_left())
