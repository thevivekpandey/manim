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

    def change_indicator(self, index_str, ival, in_transform=None, in_transform2=None):
        assert index_str in ['i', 'j']
        if index_str == 'i':
            index = self.index_i
            self.ival = ival
        else:
            index = self.index_j
            self.jval = ival
        if ival >= 0:
          n = TextMobject("$" + str(ival) + "$")
        else:
          n = TextMobject("$n" + str(ival) + "$")
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

        if in_transform:
            self.play(transform, MoveToTarget(index.arrow), in_transform, in_transform2)
        else:
            self.play(transform, MoveToTarget(index.arrow))

    def iterate_j(self, *vals):
        for val in vals:
            self.change_indicator('j', val)

    def iterate_jj(self, vals, jmin_vals, ajmin_vals):
        for val, jmin, ajmin_val in zip(vals, jmin_vals, ajmin_vals):
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

    def write_code_lines(self, *indices):
        writes = [Write(self.b[i]) for i in indices]
        self.play(*writes)

    def construct(self):
        self.num_elems1 = 4
        self.nums1 = [23, 25, 19, 28]
        side_length = 0.8
        self.squares1 = [Square(side_length=side_length) for i in range(self.num_elems1)]
        self.boxes1 = VGroup(*self.squares1).arrange(RIGHT, buff=0).to_edge(TOP, buff=SMALL_BUFF)

        self.ellipsis = TextMobject("$\hdots$")

        self.num_elems2 = 3
        self.squares2 = [Square(side_length=side_length) for i in range(self.num_elems2)]
        self.boxes2 = VGroup(*self.squares2).arrange(RIGHT, buff=0).to_edge(TOP, buff=SMALL_BUFF)

        g = VGroup(self.boxes1, self.ellipsis, self.boxes2).arrange(RIGHT).to_edge(LEFT, buff=15 * SMALL_BUFF)
        self.play(Write(g))

        num_mobjects1 = [TextMobject(str(num)) for num in self.nums1]
        self.array1 = VGroup(*num_mobjects1).arrange(RIGHT, buff=3.4*SMALL_BUFF)
        self.array1.next_to(self.boxes1[0], RIGHT, buff=-6*SMALL_BUFF)
        self.play(Write(self.array1))

        self.nums2 = [14, 17, 20]
        num_mobjects2 = [TextMobject(str(num)) for num in self.nums2]
        self.array2 = VGroup(*num_mobjects2).arrange(RIGHT, buff=3.4*SMALL_BUFF)
        self.array2.next_to(self.boxes2[0], RIGHT, buff=-6*SMALL_BUFF)
        self.play(Write(self.array2))

        self.ival, self.jval = 0, 0
        self.index_i = Indicator("i")
        s = self.squares1[0]
        self.index_i.arrow.next_to(self.squares1[0], DOWN) 
        self.index_i.index.next_to(self.index_i.arrow, LEFT)
        self.index_i.index_head.next_to(self.index_i.index, LEFT)
        self.play(Write(self.index_i.arrow), 
                  Write(self.index_i.index_head),
                  Write(self.index_i.index)
                 )

        lines = [
            "for(i=0;i<n-1;i++) \{",
            "SPACEjmin = A[i]",
            "SPACEfor(j=i+1;j<n;j++) \{",
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

        #self.change_indicator('i', 1)
        #self.change_indicator('i', 2)
        #self.change_indicator('i', 3)
        #self.change_indicator('i', -3)
        #self.change_indicator('i', -2)
        #self.change_indicator('i', -1)
        #self.write_code_lines(0, 10)

        #self.change_indicator('i', 0)

        self.index_j = Indicator("j")
        self.index_j.arrow.next_to(self.index_i.arrow, DOWN) 
        self.index_j.index.next_to(self.index_j.arrow, LEFT)
        self.index_j.index_head.next_to(self.index_j.index, LEFT)

        self.write_code_lines(1)
        #self.make_braces()
        #self.brace = self.braces[(0, 0)]
        #self.brace.next_to(self.array1[0], UP)
        self.ajmin = TextMobject("$A[j_{min}] =$")
        self.ajmin.next_to(self.array1[0], UP, buff = 4 * SMALL_BUFF)
        self.ajmin_val = TextMobject("23")
        self.ajmin_val.next_to(self.ajmin)
        self.jmin = TextMobject("$j_{min} = $")
        self.jmin.next_to(self.ajmin, UP)
        self.jmin_val = TextMobject("0")
        self.jmin_val.next_to(self.jmin)
        self.play(
                  Write(self.ajmin),
                  Write(self.ajmin_val),
                  Write(self.jmin), 
                  Write(self.jmin_val), 
                )

        self.play(Write(self.index_j.arrow), 
                  Write(self.index_j.index_head),
                  Write(self.index_j.index)
                 )
        self.write_code_lines(2, 3, 4, 5, 6)
        #self.iterate_j([1, 2, 3, -3, -2, -1)]
        self.iterate_jj([1, 2, 3, -3, -2, -1], [0, 1, 1, -3, -3, -3], [23, 23, 19, 19, 14, 14, 14])

        return

        self.change_indicator('i', 1)
        self.change_indicator('j', 1)
        self.iterate_j(2, 3, -3, -2, -1)

        self.change_indicator('i', 2)
        self.change_indicator('j', 2)
        self.iterate_j(3, -3, -2, -1)

        self.change_indicator('i', 3)
        self.change_indicator('j', 3)
        self.iterate_j(-3, -2, -1)

        self.change_indicator('i', -3)
        self.change_indicator('j', -3)
        self.iterate_j(-2, -1)

        self.change_indicator('i', -2)
        self.change_indicator('j', -2)
        self.iterate_j(-1)

