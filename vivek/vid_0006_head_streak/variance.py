from manimlib.imports import *
import random
import math

class StreakFreq(Axes):
    CONFIG = {
        "number_line_config": {
            "color": "#EEEEEE",
            "stroke_width": 2,
            "include_tip": False,
        },
        "graph_style": {
            "stroke_color": GREEN,
            "stroke_width": 3,
            "fill_opacity": 0,
        },
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_labels()
        self.circle_counts = {}
        self.top_circles = {}

    def add_axes(self):
        self.axes = Axes(**self.axes_config)
        self.add(self.axes)

    def add_labels(self):
        x_axis = self.get_x_axis()
        y_axis = self.get_y_axis()

        t_label = self.t_label = TextMobject("streak length")
        t_label.next_to(x_axis.get_right(), RIGHT, MED_SMALL_BUFF)
        x_axis.label = t_label
        x_axis.add(t_label)
        theta_label = self.theta_label = TextMobject("count")
        theta_label.next_to(y_axis.get_top(), LEFT, MED_LARGE_BUFF)
        y_axis.label = theta_label
        y_axis.add(theta_label)

        self.y_axis_label = theta_label
        self.x_axis_label = t_label

        x_axis.add(self.get_x_axis_coordinates(x_axis))
        y_axis.add(self.get_y_axis_coordinates(y_axis))

    def get_y_axis_coordinates(self, y_axis):
        #texs = [
        #    1, 2, 3, 4, 5
        #]
        texs = [i for i in range(self.y_max + 1)]
        labels = VGroup()
        values = np.arange(1, self.y_max + 1)
        for tex, value in zip(texs, values):
            if value > self.y_max or value < self.y_min:
                continue
            symbol = TexMobject(tex)
            symbol.scale(0.5)
            point = y_axis.number_to_point(value)
            symbol.next_to(point, LEFT, MED_SMALL_BUFF)
            labels.add(symbol)
        return labels

    def get_x_axis_coordinates(self, x_axis):
        steps = self.x_axis_config['tick_frequency']
        texs = [
            i for i in range(self.x_max) if i % steps == 0
        ]
        labels = VGroup()
        values = np.arange(0, self.x_max, steps)
        for tex, value in zip(texs, values):
            if value > self.x_max or value < self.x_min:
                continue
            symbol = TexMobject(tex)
            symbol.scale(0.5)
            point = x_axis.number_to_point(value)
            symbol.next_to(point, DOWN, MED_SMALL_BUFF)
            labels.add(symbol)
        return labels

    def get_circle(self, val):
        circle = Circle(color=YELLOW).scale(0.05)
        if val not in self.top_circles:
            point = self.x_axis.number_to_point(val)
            circle.next_to(point, UP, buff=0)
            self.circle_counts[val] = 1
        else:
            circle.next_to(self.top_circles[val], UP, buff=0)
            self.circle_counts[val] += 1
        self.top_circles[val] = circle
        return circle

class Towers():
    def __init__(self, **kwargs):
        self.TEXT_SCALE = 0.80
        self.tower = []
        self.seq = ''

    def get_seq(self):
        self.seq = ''
        for j in range(200):
            toss = 'H' if random.randint(0, 1) == 0 else 'T'
            self.seq += toss
        return self.seq

    def get_tower(self):
        seq = self.get_seq()
        self.elems = [TextMobject(t).scale(self.TEXT_SCALE) for t in [*seq]]
        tower = VGroup(*self.elems).arrange(RIGHT, buff=0.06)
        return tower

    def get_streak_rect(self):
        count = 0
        mx, mx_end = 0, 0
        for idx, ht in enumerate(self.seq):
            if ht == 'H':
                count += 1
                mx = max(mx, count)
                if mx == count:
                    mx_end = idx
            else:
                count = 0
        mx_start = mx_end - mx + 1
        grp = Group(*self.elems[mx_start: mx_end + 1])
        return SurroundingRectangle(grp), mx

class TossingExperiment(Scene):
    CONFIG = {
        "estreak_vs_flip_config": {
            "y_max": 4,
            "y_min": 0,
            "y_axis_config": {
                "tick_frequency": 1,
                "unit_size": 0.7,
                "tip_length": 0.3,
            },
            "x_max": 15,
            "x_min": 0,
            "x_axis_config": {
                "tick_frequency": 1,
                "unit_size": 0.7,
                "tip_length": 0.3,
            },
            "number_line_config": {
                "stroke_width": 2,
            }
        },
    }

    def construct(self):
        random.seed(11)

        axes = self.axes = StreakFreq(**self.estreak_vs_flip_config)
        axes.to_edge(DOWN)
        axes.shift(3 * LEFT)
        self.play(Write(axes))

        towers = Towers()
        for i in range(200):
            tower = towers.get_tower()
            tower.to_edge(UP)
            rect, mx = towers.get_streak_rect()
            #self.play(FadeIn(tower), run_time=0.3)
            #self.play(FadeIn(rect), run_time=0.3)
            circle = axes.get_circle(mx)   
            #self.play(Transform(rect, circle), run_time=0.3)
            self.play(Write(circle), run_time=0.3)
            #self.play(FadeOut(tower))
