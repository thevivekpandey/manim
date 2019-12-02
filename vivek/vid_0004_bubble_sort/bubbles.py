from manimlib.imports import *
from manimlib.for_vivek_videos.array import *
from vivek.vid_0004_bubble_sort.code import Code
import random

SHIFT = "shift"
SWAP = "swap"

class MyCode(VGroup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        lines = [
            "for (i = 0; i < n; i++) \{",
            "SPACEfor (j=0; j<n-1; j++) \{",
            "SPACESPACEif (A[j] > A[j+1]) \{",
            "SPACESPACESPACEtemp = A[j]",
            "SPACESPACESPACEA[j] = A[j + 1]",
            "SPACESPACESPACEA[j + 1] = temp",
            "SPACESPACE\}",
            "SPACE\}",
            "\}"
        ]

        self.codes = [Code(line) for line in lines]
        self.b = VGroup(*self.codes).arrange(DOWN).to_edge(RIGHT + UP)
        for i in range(0, len(self.codes)):
            x_diff = 0.8 + 0.65 * lines[i].count('SPACE')
            self.codes[i].align_to((x_diff, 0, 0), LEFT)
        self.add(self.b)

class Bubbles(Scene):
    CONFIG = {
        "weight_style": {
            "stroke_width": 0,
            "fill_opacity": 1,
            "sheen_direction": UL,
            "sheen_factor": 0.5,
            "background_stroke_color": BLACK,
            "background_stroke_width": 0,
            "background_stroke_opacity": 0.5,
        },
        "min_color": 20,
        "max_color": 200
    }

    def get_random_color(self):
        colors = ["#222222", "#555555", "#888888", "#BBBBBB", "#EEEEEE"]
        #grade = hex(random.randint(self.min_color, self.max_color)).upper()[2:]
        #grade = hex(random.randint(20, 100)).upper()[2:]
        #return "#" + grade + grade + grade
        return colors[random.randint(0, 4)]

    def dist(self, p1, p2):
        x1, y1 = p1.get_x(), p1.get_y()
        x2, y2 = p2.get_x(), p2.get_y()
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    def well_spaced(self, in_molecule):
        for molecule in self.molecules:
            if self.dist(in_molecule, molecule) < 2 * self.radius:
                 return False
        return True

    def create_molecule(self, x, y, color):
        c = Circle()
        c.set_width(2 * self.radius)
        c.set_style(**self.weight_style)
        c.set_color(color)
        c.move_to((x, y, 0))
        return c

    def draw_molecules(self):
        self.square = Square(side_length=2*self.hs)
        self.play(Write(self.square))
        for i in range(self.num_attempts):
            lim = self.hs - self.radius
            x = random.uniform(-lim, lim)
            y = random.uniform(-lim, lim)
            color = self.get_random_color()
            m = self.create_molecule(x, y, color)
            if self.well_spaced(m):
                self.molecules.append(m)

        print("Found {} centers".format(len(self.molecules)))

        for molecule in self.molecules:
            self.play(Write(molecule), run_time=0.1)

    def find_pair_to_switch(self):
        idx = random.randint(0, len(self.molecules) - 1)
        ref_molecule = self.molecules[idx]
        dist = 10000000
        pairing = None
        for molecule in self.molecules:
            cond1a = molecule.get_x() != ref_molecule.get_x()
            cond1b = molecule.get_y() != ref_molecule.get_y()
            cond2 = self.dist(molecule, ref_molecule) < dist
            color1 = molecule.get_color()
            color2 = ref_molecule.get_color()
            cond3 = str(color1) > str(color2) and molecule.get_y() < ref_molecule.get_y()
            cond4 = str(color1) < str(color2) and molecule.get_y() > ref_molecule.get_y()
            cond5 = self.dist(molecule, ref_molecule) < 1.2
            if cond1a and cond1b and cond2 and (cond3 or cond4) and cond5:
                pairing = molecule
                dist = self.dist(molecule, ref_molecule)
        return (ref_molecule, pairing)

    def switch(self, c1, c2):
        x1, y1 = c1.get_x(), c1.get_y()
        x2, y2 = c2.get_x(), c2.get_y()

        c1.generate_target()
        c1.target.move_to((x2, y2, 0))

        c2.generate_target()
        c2.target.move_to((x1, y1, 0))

        self.play(MoveToTarget(c1), MoveToTarget(c2), run_time=1)

    def draw_gradient(self):
        num_rects = 30
        height = (2 * self.hs) / num_rects
        rects = []
        rect_style = {
            'height': (2 * self.hs) / num_rects,
            'width': 0.8,
            'fill_opacity': 1,
            'stroke_width': 0
        }
        for i in range(num_rects):
            minc, maxc = self.min_color, self.max_color
            cval = maxc - (maxc - minc) * (i / num_rects)
            val = str(hex(int(cval)))[2:].upper()
            color = "#" + val * 3
            rect_style['color'] = color
            rects.append(Rectangle(**rect_style))
         
        self.bar = VGroup(*rects).arrange(DOWN, buff=0)
        self.bar.next_to(self.square, buff=4*SMALL_BUFF)
        self.play(Write(self.bar))

        self.light_color_text = TextMobject("Lighter Gases")
        self.heavy_color_text = TextMobject("Heavier Gases")
        self.light_color_text.scale(0.6)
        self.heavy_color_text.scale(0.6)
        self.light_color_text.next_to(rects[0], RIGHT)
        self.heavy_color_text.next_to(rects[num_rects - 1], RIGHT)
        self.play(Write(self.light_color_text))
        self.play(Write(self.heavy_color_text))

    def sort_by_switching(self):
        for i in range(self.num_switches):
            c1, c2 = self.find_pair_to_switch()
            if not c1 or not c2:
                continue
            self.switch(c1, c2)

    def swap(self, i, j):
        r, s = self.seq[i], self.seq[j]
        self.play(self.Move(r, UP,   1.5), self.Move(s, DOWN, 1.5), run_time=self.rt)
        self.play(self.Move(r, RIGHT, 2.0), self.Move(s, LEFT, 2.0), run_time=self.rt)
        self.play(self.Move(r, DOWN, 1.5), self.Move(s, UP, 1.5), run_time=self.rt)
        self.seq[i], self.seq[j] = self.seq[j], self.seq[i]

    def swap_small(self, i, j):
        r, s = self.seq[i], self.seq[j]
        self.play(self.Move(r, UP,   1.5), self.Move(s, DOWN, 1.5), run_time=self.rt)
        self.play(self.Move(r, RIGHT, 1.6), self.Move(s, LEFT, 1.6), run_time=self.rt)
        self.play(self.Move(r, DOWN, 1.5), self.Move(s, UP, 1.5), run_time=self.rt)
        self.seq[i], self.seq[j] = self.seq[j], self.seq[i]

    def Move(self, i, direction, magnitude):
        item = self.nums_t[i]
        item.generate_target()
        item.target.next_to(item, magnitude * direction)
        return MoveToTarget(item)

    def move_brace(self, n):
        self.b.generate_target()
        x0, y0 = self.b.get_x(), self.b.get_y()
        m1 = (x0 + 1.2 * n, y0, 0)
        self.b.target.move_to((m1))
        self.play(MoveToTarget(self.b), run_time=self.rt)

    def move_brace_small(self, n):
        self.b.generate_target()
        x0, y0 = self.b.get_x(), self.b.get_y()
        m1 = (x0 + 0.96 * n, y0, 0)
        self.b.target.move_to((m1))

        self.j_indicator.arrow.generate_target()
        x0, y0 = self.j_indicator.arrow.get_x(), self.j_indicator.arrow.get_y()
        m1 = (x0 + 0.96 * n, y0, 0)
        self.j_indicator.arrow.target.move_to((m1))
        
        self.index += 1
        x = TextMobject("$" + str(self.index) + "$")
        x.next_to(self.j_indicator.index_head)
        t = Transform(self.j_indicator.index, x)
        self.play(MoveToTarget(self.b), MoveToTarget(self.j_indicator.arrow), t, run_time=self.rt)

    def movements(self, *moves):
        count = 0
        while count < len(moves):
            if moves[count] == SHIFT:
                self.move_brace(1)
                count += 1
            else:
                self.swap(moves[count + 1], moves[count + 2])
                count += 3

    def set_back(self):
        m0 = self.Move(self.seq[0], UP, 1.5)
        m1 = self.Move(self.seq[1], DOWN, 1.5)
        m2 = self.Move(self.seq[2], UP, 1.5)
        m3 = self.Move(self.seq[3], DOWN, 1.5)
        m4 = self.Move(self.seq[4], UP, 1.5)
        m5 = self.Move(self.seq[5], DOWN, 1.5)
        m6 = self.Move(self.seq[6], UP, 1.5)

        self.play(m0, m1, m2, m3, m4, m5, m6, run_time=0.1)

        m0 = self.Move(self.seq[0], RIGHT, 4 * 3.3)
        m1 = self.Move(self.seq[1], RIGHT, 4 * 3.3)
        m2 = self.Move(self.seq[2], RIGHT, 4 * 3.3)
        m3 = self.Move(self.seq[3], LEFT, 2 * 3.0)
        m4 = self.Move(self.seq[4], LEFT, 4 * 3.3)
        m5 = self.Move(self.seq[5], LEFT, 2 * 3.0)
        m6 = self.Move(self.seq[6], LEFT, 4 * 3.3)

        self.play(m0, m1, m2, m3, m4, m5, m6, run_time=0.1)

        m0 = self.Move(self.seq[0], DOWN, 1.5)
        m1 = self.Move(self.seq[1], UP, 1.5)
        m2 = self.Move(self.seq[2], DOWN, 1.5)
        m3 = self.Move(self.seq[3], UP, 1.5)
        m4 = self.Move(self.seq[4], DOWN, 1.5)
        m5 = self.Move(self.seq[5], UP, 1.5)
        m6 = self.Move(self.seq[6], DOWN, 1.5)

        self.play(m0, m1, m2, m3, m4, m5, m6, run_time=0.1)
        self.seq = [0, 1, 2, 3, 4, 5, 6]

    def write_code_lines(self, *indices):
        writes = [Write(self.my_code.b[i]) for i in indices]
        self.play(*writes)

    def change_color(self, color, *indexes):
        a_s = []
        for index in indexes:
            a_s.append(ApplyMethod(self.nums_t[self.seq[index]].set_color, color))
        self.play(*a_s, run_time=self.rt)
   
    def construct(self):
        #self.num_attempts = 10 
        self.num_attempts = 400 
        self.num_switches = 35
        #self.num_switches = 5
        self.molecules = []
        self.hs = 2.5 #half side
        self.radius = 0.25

        self.draw_molecules()
        self.draw_gradient()
        self.sort_by_switching()

        nums = [25, 23, 33, 28, 14, 18, 20]

        side_length = 0.8
        self.array = [Square(side_length=side_length, color=YELLOW) for num in nums]
        self.array_g = VGroup(*self.array).arrange(RIGHT, buff=0).scale(1.5)
        self.nums_t = [TextMobject(str(num)) for num in nums]
        self.nums_t_g = VGroup(*self.nums_t).arrange(RIGHT, buff=3.4*SMALL_BUFF).scale(1.5)
        self.seq = [0, 1, 2, 3, 4, 5, 6]
        transform = Transform(self.square, self.array_g)
        self.play(transform, 
                  FadeIn(self.nums_t_g),
                  *[FadeOut(m) for m in self.molecules],
                  FadeOut(self.bar),
                  FadeOut(self.light_color_text),
                  FadeOut(self.heavy_color_text)
                 )
        self.wait(10)

        g = VGroup(self.array[0], self.array[1])
        self.b = Brace(g, DOWN)
        self.play(Write(self.b))

        self.rt = 1.0

        self.move_brace(1)
        self.move_brace(1)
        self.move_brace(1)
        self.move_brace(1)
        self.move_brace(1)

        self.move_brace(-5)
        self.wait(8)

        self.swap(0, 1)
        self.move_brace(1)
        self.wait(4)
        self.move_brace(1)
        self.wait(4)
        self.swap(2, 3)
        self.move_brace(1)
        self.swap(3, 4)
        self.move_brace(1)
        self.swap(4, 5)
        self.move_brace(1)
        self.swap(5, 6)

        self.change_color(GREEN, 6)

        self.move_brace(-5)
        self.wait(1)
        self.rt = 0.6
        self.movements(SHIFT, SHIFT, SWAP, 2, 3, SHIFT, SWAP, 3, 4, SHIFT, SWAP, 4, 5, SHIFT)
        self.change_color(GREEN, 5)

        self.rt = 0.36
        self.move_brace(-5)
        self.movements(SHIFT, SWAP, 1, 2, SHIFT, SWAP, 2, 3, SHIFT, SWAP, 3, 4, SHIFT, SHIFT)
        self.change_color(GREEN, 4)

        self.rt = 0.1
        self.move_brace(-5)
        self.movements(SWAP, 0, 1, SHIFT, SWAP, 1, 2, SHIFT, SWAP, 2, 3, SHIFT, SHIFT, SHIFT)
        self.change_color(GREEN, 3)

        self.change_color(GREEN, 2)
        self.change_color(GREEN, 1)
        self.change_color(GREEN, 0)

        #self.wait(99)
        a0 = ApplyMethod(self.b.shift, 8.5 * LEFT)
        a1 = ApplyMethod(self.square.shift, 3.0 * LEFT)
        a2 = ApplyMethod(self.nums_t_g.shift, 3.0 * LEFT)
        a3 = ApplyMethod(self.b.scale, 0.8)
        a4 = ApplyMethod(self.square.scale, 0.8)
        a5 = ApplyMethod(self.nums_t_g.scale, 0.8)
  
        self.play(a3, a4, a5, run_time=0.1)
        self.play(a0, a1, a2, run_time=0.1)
        self.change_color(WHITE, 0, 1, 2, 3, 4, 5, 6)

        self.set_back()
        self.wait(6)
        self.j_indicator = Indicator("j")
        self.j_indicator.arrow.next_to(self.b, DOWN)
        self.j_indicator.index.next_to(self.j_indicator.arrow, LEFT)
        self.j_indicator.index_head.next_to(self.j_indicator.index, LEFT)
        
        self.play(Write(self.j_indicator))

        self.my_code = MyCode()
        self.write_code_lines(1, 2, 3, 4, 5, 6, 7)
        self.wait(3)

        self.rt = 0.8 
        self.index = 0
        self.swap(0, 1)
        self.wait(3)
        self.move_brace_small(1)
        self.move_brace_small(1)
        self.swap(2, 3)
        self.move_brace_small(1)
        self.swap(3, 4)
        self.rt = 0.4
        self.move_brace_small(1)
        self.swap(4, 5)
        self.move_brace_small(1)
        self.swap(5, 6)
        self.change_color(GREEN, 6)

        self.wait(15)

        self.write_code_lines(0, 8)

        self.wait(18)
        s1 = TextMobject("$i = 0 \Rightarrow n - 1$ comparisons").scale(0.7)
        s2 = TextMobject("$i = 1 \Rightarrow n - 2$ comparisons").scale(0.7)
        s3 = TexMobject("\\vdots").scale(0.7)
        s4 = TextMobject("$i = i \Rightarrow n - 1 - i$ comparisons").scale(0.7)
        s = VGroup(s1, s2, s3, s4).arrange(DOWN)
        s.next_to(self.array[0], DOWN)
        self.play(Write(s1))
        self.wait(8)
        self.play(Write(s2))
        self.wait(5)
        self.play(Write(s3))
        self.play(Write(s4))
        x = Code("SPACEfor (j=0; j<n-i-1; j++) \{")
        x.next_to(self.my_code.codes[0], DOWN)
        t = Transform(self.my_code.codes[1], x)
        rp = SurroundingRectangle(x, color=RED)
        self.play(t, Write(rp))

        self.wait(14)
        r = SurroundingRectangle(self.my_code.codes[2])
        self.my_code.add(r)
        self.play(Write(r), FadeOut(rp))

        self.wait(15)
        #self.my_code.scale(0.2).to_edge(TOP)
        self.play(self.my_code.scale, 0.6, self.my_code.to_edge, UP, FadeOut(r))

        self.wait(2)
        s2 = TextMobject("$n-1$").scale(0.8)
        s2.next_to(self.my_code, DOWN)
        self.play(Write(s2))

        self.wait(5)
        s3 = TextMobject("$n-2$").scale(0.8)
        s3.next_to(s2, DOWN)
        self.play(Write(s3))

        self.wait(2)
        s4 = TextMobject("$\\vdots$").scale(0.8)
        s4.next_to(s3, DOWN)
        self.play(Write(s4))

        s5 = TextMobject("$2$").scale(0.8)
        s5.next_to(s4, DOWN)
        self.play(Write(s5))

        s6 = TextMobject("$1$").scale(0.8)
        s6.next_to(s5, DOWN)
        self.play(Write(s6))

        self.wait(4)

        s7 = Line(LEFT, RIGHT)
        s7.set_length(2)
        s7.next_to(s6, DOWN)

        s8 = TextMobject("$n(n-1)/2$").scale(0.8)
        s8.next_to(s7, DOWN)

        s9 = Line(LEFT, RIGHT)
        s9.set_length(2)
        s9.next_to(s8, DOWN)
        self.play(Write(s7), Write(s8), Write(s9))

        self.wait(3)
        s10 = TextMobject("$\Rightarrow O(n^2)$").scale(0.9)
        s10.next_to(s8)
        self.play(Write(s10))
        self.wait(5)
