from manimlib.imports import *
from vivek.vid_0003_selection_sort.code import Code

class Opening(Scene):
    def construct(self):
        text = TextMobject("Computer Science by Pandey")

        subtext = TextMobject("One video: One snack sized topic")
        topic = TextMobject("SELECTION SORT")
        topic.set_color(BLUE)
        VGroup(text, subtext, topic).arrange(DOWN)
        self.play(FadeIn(text), FadeIn(subtext))
        self.wait(15)
        self.play(FadeOut(text), FadeOut(subtext))

class Topic(Scene):
    def swap(self, later, former, run_time=1):
        multiple = 0.8
        delta = 0
        later_stick = self.array1[self.seq[later]]
        former_stick = self.array1[self.seq[former]]

        self.play(ApplyMethod(self.array1[self.seq[later]].set_color, RED))

        later_stick.generate_target()
        later_stick.target.next_to(later_stick, 2 * UP)
        former_stick.generate_target()
        former_stick.target.next_to(former_stick, 2 * DOWN)
        self.play(MoveToTarget(later_stick), MoveToTarget(former_stick), run_time=run_time)

        shift = (later - former) * multiple + delta

        later_stick.generate_target()
        later_stick.target.shift(shift * LEFT)
        former_stick.generate_target()
        former_stick.target.shift(shift * RIGHT)
        self.play(MoveToTarget(later_stick), MoveToTarget(former_stick), run_time=run_time)

        later_stick.generate_target()
        later_stick.target.next_to(later_stick, 2 * DOWN)
        former_stick.generate_target()
        former_stick.target.next_to(former_stick, 2 * UP)
        self.play(MoveToTarget(later_stick), MoveToTarget(former_stick), run_time=run_time)
        
        self.seq[later], self.seq[former] = self.seq[former], self.seq[later]
   
    def construct(self):
        topic = TextMobject("SELECTION SORT")
        topic.scale(2)
        topic.set_color(BLUE)
        self.play(Write(topic))

        self.num_elems1 = 7
        self.nums1 = [23, 25, 19, 28, 14, 17, 20]
        self.seq = [0, 1, 2, 3, 4, 5, 6]
        side_length = 0.8
        self.squares1 = [Square(side_length=side_length) for i in range(self.num_elems1)]
        self.boxes1 = VGroup(*self.squares1).arrange(RIGHT, buff=0).to_edge(TOP, buff=SMALL_BUFF)

        g = VGroup(self.boxes1).arrange(RIGHT).next_to(topic, DOWN, buff=10 * SMALL_BUFF)

        num_mobjects1 = [TextMobject("$a_" + str(i) + "$") for i in range(self.num_elems1)]
        self.array1 = VGroup(*num_mobjects1).arrange(RIGHT, buff=3.8*SMALL_BUFF)
        self.array1.next_to(self.boxes1[0], RIGHT, buff=-6*SMALL_BUFF)
        self.play(FadeIn(self.array1), FadeIn(g))
        self.swap(4, 0)
        self.swap(6, 1)
        self.swap(3, 2)
        self.swap(5, 3)
        self.wait(15)

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
        self.wait(2)
        self.play(Write(rect1))
        self.wait(1)

        self.play(Write(arrow))

        self.play(Write(real_world))
        self.wait(2)
        self.play(Write(rect2))
        self.wait(12)

    def get_algo_world(self):
        t = Tree()
        t.scale(0.5)

        squares = [Square(side_length=0.5) for i in range(7)]
        boxes = VGroup(*squares).arrange(RIGHT, buff=0)

        lines = [
            "for (i = 0; i < n; i++) \{",
            "SPACEfor (j = 0; j < n; j++) \{",
            "\\vdots"
          ]
        codes = [Code(line) for line in lines]
        c = VGroup(*codes).arrange(DOWN).to_edge(RIGHT + DOWN)
        for i in range(0, len(codes)):
            x_diff = 1.4 + 0.65 * lines[i].count('SPACE')
            if 'vdots' in lines[i]:
                x_diff = 4.5
            codes[i].align_to((x_diff, 0, 0), LEFT)
        self.add(c)
        
        x = VGroup(t, boxes, c).arrange(DOWN, buff = LARGE_BUFF)
        x.scale(0.9)
        x.to_edge(LEFT, buff=LARGE_BUFF)
        return x, SurroundingRectangle(x)

    def get_real_world(self):
        r1 = SVGMobject(file_name = 'eagle-svgrepo-com.svg').scale(0.5)
        r2 = SVGMobject(file_name = 'mountain-climb-svgrepo-com.svg').scale(0.5)
        r3 = SVGMobject(file_name = 'hummingbird-svgrepo-com.svg').scale(0.5)
        r4 = SVGMobject(file_name = 'lion-face-svgrepo-com.svg').scale(0.5)
        r5 = SVGMobject(file_name = 'tree-swallow-svgrepo-com.svg').scale(0.5)

        x1 = VGroup(r1, r2).arrange(DOWN, buff = LARGE_BUFF)
        x2 = VGroup(r3, r4, r5).arrange(DOWN, buff = LARGE_BUFF)
        y = VGroup(x1, x2).arrange(RIGHT, buff = LARGE_BUFF)
        y.to_edge(RIGHT, buff=10*SMALL_BUFF + LARGE_BUFF)
        rect2 = SurroundingRectangle(y, buff=6*SMALL_BUFF)
        return y, rect2

    def get_arrow(self, rect1, rect2):
        return Arrow(rect1.get_right(), rect2.get_left())
