from manimlib.imports import *
from vivek.vid_0004_bubble_sort.code import Code

class Indicator(VGroup):
    def __init__(self, indicator_name, **kwargs):
        super().__init__(**kwargs)
        self.arrow = Arrow(DOWN, UP, stroke_width=1)
        self.arrow.set_length(1)

        self.index_head = TextMobject("$" + indicator_name + "=$")

        self.index = TextMobject("$0$")
        self.add(self.arrow, self.index_head, self.index)
        self.scale(0.8)

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
        self.b = VGroup(*self.codes).arrange(DOWN).scale(1.2)
        self.b.to_edge(RIGHT)
        for i in range(0, len(self.codes)):
            x_diff = 0.8 + 0.65 * lines[i].count('SPACE')
            self.codes[i].align_to((x_diff, 0, 0), LEFT)
        self.add(self.b)

class Algorithm(Scene):
    def make_braces(self):
        self.braces = {}
        elems = [0, 1, 2, 3, -3, -2, -1]
        for i in elems:
            few_braces = []
            for j in elems:
                if i >= 0 and j >= 0:
                    arr = VGroup(self.array1[i:j])
                elif i < 0 and j < 0:
                    arr = VGroup(self.array2[3+i:3+j])
                elif i >= 0 and j < 0:
                    arr = VGroup(self.array1[i:4], self.ellipsis, self.array2[0:3+j])
                a_brace = Brace(arr, UP)
                self.braces[(i, j)] = a_brace

    def change_indicator(self, index_str, ival, run_time=1):
        assert index_str in ['i', 'j']
        if index_str == 'i':
            index = self.index_i
            self.ival = ival
        else:
            index = self.index_j
            self.jval = ival
        n = TextMobject("$" + str(ival) + "$")
        n.next_to(index.index_head, RIGHT)
        transform = Transform(index.index, n)       

        delta = 0.8 
        offset = 3.3

        index.arrow.generate_target()
       
        x0 = -5.2111
        y = index.arrow.get_y()

        if ival >= 0:
            loc = x0 + delta * ival
        else:
            loc = x0 + offset + delta * (self.num_elems2 + ival + 1)
        index.arrow.target.move_to((loc, y, 0))

        self.play(transform, MoveToTarget(index.arrow), run_time = run_time)

    def iterate_j(self, *vals):
        for val in vals:
            self.change_indicator('j', val)

    def transform_jmin(self, jmin_val, ajmin_val, run_time=1):
        t = TextMobject("$" + str(jmin_val) + "$")
        t1 = TextMobject("$" + str(ajmin_val) + "$")
        t.next_to(self.jmin)
        t1.next_to(self.ajmin)
        self.play(Transform(self.jmin_val, t), Transform(self.ajmin_val, t1), run_time=run_time)

    def iterate_jj(self, vals, jmin_vals, ajmin_vals, sleep_times):
        for val, jmin, ajmin_val, sleep_time in zip(vals, jmin_vals, ajmin_vals, sleep_times):
            if jmin >= 0:
                t = TextMobject("$" + str(jmin) + "$")
            else:
                t = TextMobject("$n" + str(jmin) + "$")
            t1 = TextMobject("$" + str(ajmin_val) + "$")
            t.next_to(self.jmin)
            t1.next_to(self.ajmin)
  
            self.change_indicator('j', val, 
                             Transform(self.jmin_val, t),
                             Transform(self.ajmin_val, t1))
            self.wait(sleep_time)

    def write_code_lines(self, *indices):
        writes = [Write(self.my_code.b[i]) for i in indices]
        self.play(*writes)

    def swap(self, later, former, run_time=1):
        multiple = 0.8
        delta = 0
        later_stick = self.array1[self.seq[later]]
        former_stick = self.array1[self.seq[former]]

        self.play(ApplyMethod(self.array1[self.seq[former]].set_color, RED))

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
        self.num_elems1 = 6
        self.nums1 = [23, 25, 19, 28, 14, 17]
        self.seq = [0, 1, 2, 3, 4, 5]
        side_length = 1.4
        self.squares1 = [Square(side_length=side_length, color=YELLOW) for i in range(self.num_elems1)]
        self.boxes1 = VGroup(*self.squares1).arrange(RIGHT, buff=0).to_edge(TOP, buff=2 * SMALL_BUFF)

        g = VGroup(self.boxes1).arrange(RIGHT).to_edge(TOP + LEFT, buff=6 * SMALL_BUFF)
        self.play(FadeIn(g))

        self.index_objects = [TextMobject(str(num)).scale(2.4) for num in self.seq]
        self.indexes = VGroup(*self.index_objects).arrange(RIGHT, buff=8.5 * SMALL_BUFF)
        self.indexes.next_to(g, UP)
        self.play(FadeIn(self.indexes))

        num_mobjects1 = [TextMobject(str(num), color=RED).scale(2.4) for num in self.nums1]
        self.array1 = VGroup(*num_mobjects1).arrange(RIGHT, buff=3.5*SMALL_BUFF)
        self.array1.next_to(self.boxes1[0], RIGHT, buff=-12*SMALL_BUFF)
        self.play(FadeIn(self.array1))

        self.my_code = MyCode()
        topic1 = TextMobject("Bubble Sort")
        topic1.scale(3.4)
        topic1.next_to(g, DOWN, buff=8*SMALL_BUFF)

        topic2 = TextMobject("Why so slow?")
        topic2.scale(3.0)
        topic2.next_to(topic1, DOWN, buff=3*SMALL_BUFF)

        self.write_code_lines(0, 1, 2, 3, 4, 5, 6, 7, 8)
        self.play(FadeIn(topic1), FadeIn(topic2))
