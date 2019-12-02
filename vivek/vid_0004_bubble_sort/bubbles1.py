from manimlib.imports import *
from manimlib.for_vivek_videos.array import *
from vivek.vid_0004_bubble_sort.code import Code
import random

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

    def well_spaced1(self, in_molecule):
        for molecule in self.molecules1:
            if self.dist(in_molecule, molecule) < 2 * self.radius:
                 return False
        return True

    def well_spaced2(self, in_molecule):
        for molecule in self.molecules2:
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

    def draw_molecules1(self):
        self.square1 = Square(side_length=2*self.hs)
        self.square1.to_edge(LEFT, buff=15 * SMALL_BUFF)
        self.t = TextMobject("Uniprocess bubble sort", color=BLUE)
        self.t.next_to(self.square1, DOWN)
        self.play(Write(self.square1), Write(self.t), run_time=0.7)
        for i in range(self.num_attempts):
            lim = self.hs - self.radius
            x = random.uniform(-lim, lim) - 3.1
            y = random.uniform(-lim, lim)
            color = self.get_random_color()
            m = self.create_molecule(x, y, color)
            if self.well_spaced1(m):
                self.molecules1.append(m)

        print("Found {} centers".format(len(self.molecules1)))

        writes = [FadeIn(molecule) for molecule in self.molecules1]
        self.play(*writes, run_time=0.7)

    def draw_molecules2(self):
        self.square2 = Square(side_length=2*self.hs)
        self.square2.to_edge(RIGHT, buff=15 * SMALL_BUFF)
        self.t = TextMobject("Real world parallel bubble sort", color=BLUE)
        self.t.next_to(self.square2, DOWN)
        self.play(Write(self.square2), Write(self.t), run_time=0.7)
        for i in range(self.num_attempts):
            lim = self.hs - self.radius
            x = random.uniform(-lim, lim) + 3.1
            y = random.uniform(-lim, lim)
            color = self.get_random_color()
            m = self.create_molecule(x, y, color)
            if self.well_spaced2(m):
                self.molecules2.append(m)

        print("Found {} centers".format(len(self.molecules2)))

        writes = [FadeIn(molecule) for molecule in self.molecules2]
        self.play(*writes, run_time=0.7)

    def find_pair_to_switch(self):
        idx = random.randint(0, len(self.molecules1) - 1)
        ref_molecule = self.molecules1[idx]
        dist = 10000000
        pairing = None
        for molecule in self.molecules1:
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

    def find_single_pair(self, covered):
        idx = random.randint(0, len(self.molecules2) - 1)
        while covered[idx]:
            idx = random.randint(0, len(self.molecules2) - 1)

        covered[idx] = True
        ref_molecule = self.molecules2[idx]
        dist = 10000000
        pairing = None
        opt = None
        for jdx, molecule in enumerate(self.molecules2):
            cond1a = molecule.get_x() != ref_molecule.get_x()
            cond1b = molecule.get_y() != ref_molecule.get_y()
            cond2 = self.dist(molecule, ref_molecule) < dist
            color1 = molecule.get_color()
            color2 = ref_molecule.get_color()
            cond3 = str(color1) > str(color2) and molecule.get_y() < ref_molecule.get_y()
            cond4 = str(color1) < str(color2) and molecule.get_y() > ref_molecule.get_y()
            cond5 = self.dist(molecule, ref_molecule) < 1.2
            cond6 = not covered[jdx] 
            if cond1a and cond1b and cond2 and (cond3 or cond4) and cond5 and cond6:
                pairing = molecule
                dist = self.dist(molecule, ref_molecule)
                opt = jdx
        if opt:
            covered[opt] = True
        return (ref_molecule, pairing)

    def find_pairs_to_switch(self):
        covered = [False] * len(self.molecules2)
        pairs = []
        for _ in range(10):
            pairs.append(self.find_single_pair(covered))
        return pairs
    
    def switch(self, c1, c2):
        x1, y1 = c1.get_x(), c1.get_y()
        x2, y2 = c2.get_x(), c2.get_y()

        c1.generate_target()
        c1.target.move_to((x2, y2, 0))

        c2.generate_target()
        c2.target.move_to((x1, y1, 0))

        #self.play(MoveToTarget(c1), MoveToTarget(c2), run_time=1)
        return MoveToTarget(c1), MoveToTarget(c2)

    def sort_by_switching(self):
        for i in range(self.num_switches):
            c1, c2 = self.find_pair_to_switch()
            if not c1 or not c2:
                continue
            self.switch(c1, c2)

    def sort(self):
        moves = []
        p = self.find_pair_to_switch()
        if p[0] and p[1]:
            moves.extend(self.switch(p[0], p[1]))
        pairs = self.find_pairs_to_switch()
        for p in pairs:
            if p[0] and p[1]:
                moves.extend(self.switch(p[0], p[1]))
        self.play(*moves)

    def construct(self):
        self.num_attempts = 400 
        self.num_switches = 35
        self.molecules1, self.molecules2 = [], []
        self.hs = 2.5 #half side
        self.radius = 0.25

        self.draw_molecules1()
        self.draw_molecules2()
        for _ in range(15):
            self.sort()

