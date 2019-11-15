from manimlib.imports import *
from vivek.vid_0003_selection_sort.code import Code

class Indicator(VGroup):
    def __init__(self, indicator_name, **kwargs):
        super().__init__(**kwargs)
        self.arrow = Arrow(DOWN, UP, stroke_width=1)
        self.arrow.set_length(1)

        self.index_head = TextMobject("$" + indicator_name + "=$")

        self.index = TextMobject("$0$")
        self.add(self.arrow, self.index_head, self.index)
        self.scale(0.8)

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
        writes = [Write(self.b[i]) for i in indices]
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
        self.num_elems1 = 7
        self.nums1 = [23, 25, 19, 28, 14, 17, 20]
        self.seq = [0, 1, 2, 3, 4, 5, 6]
        side_length = 0.8
        self.squares1 = [Square(side_length=side_length) for i in range(self.num_elems1)]
        self.boxes1 = VGroup(*self.squares1).arrange(RIGHT, buff=0).to_edge(TOP, buff=SMALL_BUFF)

        g = VGroup(self.boxes1).arrange(RIGHT).to_edge(LEFT, buff=15 * SMALL_BUFF)
        self.play(Write(g))

        self.index_objects = [TextMobject(str(num)) for num in self.seq]
        self.indexes = VGroup(*self.index_objects).arrange(RIGHT, buff=5.9 * SMALL_BUFF)
        self.indexes.next_to(g, UP)
        self.play(Write(self.indexes))

        num_mobjects1 = [TextMobject(str(num)) for num in self.nums1]
        self.array1 = VGroup(*num_mobjects1).arrange(RIGHT, buff=3.4*SMALL_BUFF)
        self.array1.next_to(self.boxes1[0], RIGHT, buff=-6*SMALL_BUFF)
        self.play(Write(self.array1))

        self.ival, self.jval = 0, 0
        self.index_i = Indicator("i")
        s = self.squares1[0]
        self.index_i.arrow.next_to(self.squares1[0], DOWN) 
        self.index_i.index.next_to(self.index_i.arrow, LEFT)
        self.index_i.index_head.next_to(self.index_i.index, LEFT)
        self.wait(2)
        self.play(Write(self.index_i.arrow), 
                  Write(self.index_i.index_head),
                  Write(self.index_i.index)
                 )

        lines = [
            "for(i=0;i<n-1;i++) \{",
            "SPACEjmin = i",
            "SPACEfor(j=i;j<n;j++) \{",
            "SPACESPACEif(A[j]<A[jmin]) \{",
            "SPACESPACESPACEjmin = j",
            "SPACESPACE\}",
            "SPACE\}",
            "SPACEtemp = A[i]",
            "SPACEA[i] = A[jmin]",
            "SPACEA[jmin] = temp",
            "\}"
        ]

        codes = [Code(line) for line in lines]
        self.b = VGroup(*codes).arrange(DOWN).to_edge(RIGHT + DOWN)
        for i in range(0, len(codes)):
            x_diff = 1.4 + 0.65 * lines[i].count('SPACE')
            codes[i].align_to((x_diff, 0, 0), LEFT)

        self.change_indicator('i', 1)
        self.change_indicator('i', 2)
        self.change_indicator('i', 3)
        self.change_indicator('i', 4)
        self.change_indicator('i', 5)
        self.change_indicator('i', 6)
        self.change_indicator('i', 0)
        self.wait(1)
        self.write_code_lines(0, 10)
        self.wait(7)

        self.index_j = Indicator("j")
        self.index_j.arrow.next_to(self.index_i.arrow, DOWN) 
        self.index_j.index.next_to(self.index_j.arrow, LEFT)
        self.index_j.index_head.next_to(self.index_j.index, LEFT)

        self.play(Write(self.index_j.arrow), 
                  Write(self.index_j.index_head),
                  Write(self.index_j.index)
                 )

        self.wait(2)
        #self.make_braces()
        #self.brace = self.braces[(0, 0)]
        #self.brace.next_to(self.array1[0], UP)
        self.write_code_lines(2, 6)
        self.wait(3)
        self.ajmin = TextMobject("$A[j_{min}] =$")
        self.ajmin.next_to(self.indexes, UP, buff = 4 * SMALL_BUFF)
        self.ajmin_val = TextMobject("23")
        self.ajmin_val.next_to(self.ajmin)
        self.jmin = TextMobject("$j_{min} = $")
        self.jmin.next_to(self.ajmin, UP)
        self.jmin_val = TextMobject("0")
        self.jmin_val.next_to(self.jmin)
        self.play(
                  Write(self.jmin), 
                  Write(self.jmin_val), 
                )
        self.write_code_lines(1)
        self.wait(7)
        self.write_code_lines(3, 4, 5)
        self.wait(7)
        self.play(
                  Write(self.ajmin),
                  Write(self.ajmin_val),
                )
        
        self.wait(5)
        self.change_indicator('j', 1)
        self.wait(5)
        self.change_indicator('j', 2)
        self.wait(3.5)
        self.transform_jmin(2, 19)
        self.wait(2)

        self.change_indicator('j', 3)
        self.wait(5)
        self.change_indicator('j', 4)
        self.wait(2)
        self.transform_jmin(4, 14)
        self.change_indicator('j', 5)
        self.change_indicator('j', 6)
        self.wait(8)
        self.swap(0, 4)
        self.wait(2)
        self.write_code_lines(7, 8, 9)
        self.wait(18)

        self.change_indicator('i', 1)
        self.transform_jmin(1, 25)
        self.change_indicator('j', 1)
        self.change_indicator('j', 2)
        self.transform_jmin(2, 19)
        self.change_indicator('j', 3)
        self.change_indicator('j', 4)
        self.change_indicator('j', 5)
        self.transform_jmin(5, 17)
        self.change_indicator('j', 6)
        self.wait(1)
        self.swap(1, 5)
        self.wait(1)
        
        self.change_indicator('i', 2, run_time=0.5)
        self.change_indicator('j', 2, run_time=0.5)
        self.transform_jmin(2, 19, run_time=0.5)
        self.change_indicator('j', 3, run_time=0.5)
        self.change_indicator('j', 4, run_time=0.5)
        self.change_indicator('j', 5, run_time=0.5)
        self.change_indicator('j', 6, run_time=0.5)
        self.play(ApplyMethod(self.array1[self.seq[2]].set_color, RED))

        self.change_indicator('i', 3, run_time=0.5)
        self.transform_jmin(3, 28, run_time=0.5)
        self.change_indicator('j', 3, run_time=0.5)
        self.change_indicator('j', 4, run_time=0.5)
        self.transform_jmin(4, 23, run_time=0.5)
        self.change_indicator('j', 5, run_time=0.5)
        self.change_indicator('j', 6, run_time=0.5)
        self.transform_jmin(6, 20, run_time=0.5)
        self.swap(3, 6, run_time=0.5)

        self.change_indicator('i', 4, run_time=0.5)
        self.change_indicator('j', 4, run_time=0.5)
        self.transform_jmin(4, 23, run_time=0.5)
        self.change_indicator('j', 5, run_time=0.5)
        self.change_indicator('j', 6, run_time=0.5)
        self.play(ApplyMethod(self.array1[self.seq[4]].set_color, RED))

        self.change_indicator('i', 5, run_time=0.5)
        self.change_indicator('j', 5, run_time=0.5)
        self.transform_jmin(5, 25, run_time=0.5)
        self.change_indicator('j', 6, run_time=0.5)
        self.play(ApplyMethod(self.array1[self.seq[5]].set_color, RED))

        self.change_indicator('i', 6, run_time=0.5)
        self.change_indicator('j', 6, run_time=0.5)
        self.transform_jmin(6, 28, run_time=0.5)
        self.play(ApplyMethod(self.array1[self.seq[6]].set_color, RED))
        self.wait(12)

        #Complexity analysis
        rect = SurroundingRectangle(codes[3])
        self.play(Write(rect))
        self.wait(10)
        self.play(FadeOut(rect))

        self.change_indicator('i', 0, run_time=0.75)
        self.change_indicator('j', 0, run_time=0.75)
        self.change_indicator('j', 1, run_time=0.75)
        self.change_indicator('j', 2, run_time=0.75)
        self.change_indicator('j', 3, run_time=0.75)
        self.change_indicator('j', 4, run_time=0.75)
        self.change_indicator('j', 5, run_time=0.75)
        self.change_indicator('j', 6, run_time=0.75)

        self.play(self.b.scale, 0.38, self.b.to_edge, UP)

        self.wait(1)
        s1 = TextMobject("$n$")
        s1.next_to(self.b, DOWN)
        self.play(Write(s1))
        self.wait(2)

        self.change_indicator('i', 1, run_time=0.75)
        self.change_indicator('j', 1, run_time=0.75)
        self.change_indicator('j', 2, run_time=0.75)
        self.change_indicator('j', 3, run_time=0.75)
        self.change_indicator('j', 4, run_time=0.75)
        self.change_indicator('j', 5, run_time=0.75)
        self.change_indicator('j', 6, run_time=0.75)

        s2 = TextMobject("$n-1$")
        s2.next_to(s1, DOWN)
        self.play(Write(s2))

        self.wait(1)
        s3 = TextMobject("$n-2$")
        s3.next_to(s2, DOWN)
        self.play(Write(s3))

        s4 = TextMobject("$\\vdots$")
        s4.next_to(s3, DOWN)
        self.play(Write(s4))

        s5 = TextMobject("$2$")
        s5.next_to(s4, DOWN)
        self.play(Write(s5))

        s6 = TextMobject("$1$")
        s6.next_to(s5, DOWN)
        self.play(Write(s6))

        self.wait(5)

        s7 = Line(LEFT, RIGHT)
        s7.set_length(2)
        s7.next_to(s6, DOWN)

        s8 = TextMobject("$\\frac{n(n-1)}{2}$")
        s8.next_to(s7, DOWN)

        s9 = Line(LEFT, RIGHT)
        s9.set_length(2)
        s9.next_to(s8, DOWN)
        self.play(Write(s7), Write(s8), Write(s9))

        self.wait(6)
        s10 = TextMobject("$\Rightarrow O(n^2)$")
        s10.next_to(s8)
        self.play(Write(s10))
