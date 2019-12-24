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

class ThreeQuestions(Scene):
    def construct(self):
        s = TextMobject("STABLE SORTING ALGORITHMS", color=YELLOW).scale(1.5)
        s.to_edge(TOP, buff=SMALL_BUFF)
        q0 = TextMobject("Three Questions", color=BLUE).scale(1.3)
        q0.next_to(s, DOWN)
        q1 = TextMobject("1. When do we call a sorting algorithm as stable?", substrings_to_isolate=["1."])
        q2 = TextMobject("2. Why is stability a useful property of sorting algorithms?", substrings_to_isolate=["2."])
        q3 = TextMobject("3. What makes a sorting algo stable?", substrings_to_isolate=["3."])

        q1.sn = q1.get_part_by_tex("1.")
        q1.sn.set_color(GREEN)
        q2.sn = q2.get_part_by_tex("2.")
        q2.sn.set_color(GREEN)
        q3.sn = q3.get_part_by_tex("3.")
        q3.sn.set_color(GREEN)

        self.play(Write(s))
        self.wait(3)
        self.play(Write(q0))
        self.wait(1.5)
        q = VGroup(q1, q2, q3).arrange(DOWN, buff=4*SMALL_BUFF)
        q.next_to(q0, DOWN, buff=LARGE_BUFF)
        q1.shift(1.0 * LEFT)
        q3.shift(2.4 * LEFT)
        self.play(Write(q1))
        self.wait(1.5)
        self.play(Write(q2))
        self.wait(2.7)
        self.play(Write(q3))

        self.wait(4)
        l1 = Line(UP, DOWN, color=GREEN).scale(0.5)
        l1.next_to(q3, DOWN)
        l1.shift(3 * RIGHT)

        l2 = Arrow(LEFT, RIGHT, color=GREEN).scale(0.5)
        l2.next_to(l1, RIGHT, buff=0)
        l2.shift(0.5 * DOWN)
       
        t = TextMobject("Original\\\\Insights!", color=GREEN)
        t.next_to(l2, RIGHT)
        
        triangle = Triangle(color=GREEN).scale(0.7)
        triangle.next_to(t)

        self.play(Write(l1), Write(l2), Write(t), Write(triangle))
        self.wait(9)

class Array(VGroup):
    def __init__(self, nums, side_length, **kwargs):
        super().__init__(**kwargs)
        self.nums = nums
        self.seq = [k for k in range(len(nums))]
        self.array = [Square(side_length=side_length, color=RED) for num in nums]
        self.array_g = VGroup(*self.array).arrange(RIGHT, buff=0)
        self.nums_t = [TexMobject(str(num)) for num in nums]
        self.nums_t_g = VGroup(*self.nums_t).arrange(RIGHT, buff=6.8*SMALL_BUFF)
        self.add(self.array_g)
        self.add(self.nums_t_g)

        self.step_size = self.array[0].side_length

    def move_up(self, i):
        return self.move(i, UP, self.step_size)

    def move_down(self, i):
        return self.move(i, DOWN, self.step_size)

    def move_left(self, i, num_steps):
        return self.move(i, LEFT, self.step_size * num_steps)

    def move_right(self, i, num_steps):
        return self.move(i, RIGHT, self.step_size * num_steps)

    def move(self, i, direction, magnitude):
        item = self.nums_t[i]
        item.generate_target()
        item.target.shift(magnitude * direction)
        return MoveToTarget(item)

    def set_scale(self, scale_factor):
        self.step_size *= scale_factor

    def init_seq(self):
        self.seq = [k for k in range(len(nums))]

class SortingAlgos(Scene):
    def swap(self, a, former, latter):
        diff = latter - former
        l, f = a.seq[latter], a.seq[former]
        yield [a.move_up(l), a.move_down(f)]
        yield [a.move_left(l, diff), a.move_right(f, diff)]
        yield [a.move_down(l), a.move_up(f)]
        a.seq[former], a.seq[latter] = a.seq[latter], a.seq[former]

    def insert(self, a, src, target):
        assert src > target
        s, t = a.seq[src], a.seq[target]
        yield [a.move_up(s)]
        yield [a.move_left(s, src - target)]
        yield [a.move_right(a.seq[i], 1) for i in range(target, src)]
        yield [a.move_down(s)]
        temp = a.seq[src]
        for i in range(src, target, -1):
            a.seq[i] = a.seq[i - 1]
        a.seq[target] = temp

    def selection_sort(self, a):
        for move in self.swap(a, 0, 4):
            yield move
        for move in self.swap(a, 1, 4):
            yield move
        for move in self.swap(a, 2, 4):
            yield move
        for move in self.swap(a, 3, 4):
            yield move
        for move in self.swap(a, 5, 6):
            yield move
        while True:
            yield 'dummy'

    def selection_sort_with_duplicate(self, a):
        for move in self.swap(a, 0, 4):
            yield move
        for move in self.swap(a, 1, 5):
            yield move
        for move in self.swap(a, 2, 4):
            yield move
        for move in self.swap(a, 4, 5):
            yield move
        while True:
            yield 'dummy'
    
    def insertion_sort(self, a):
        for move in self.insert(a, 4, 0):
            yield move
        for move in self.insert(a, 6, 5):
            yield move
        while True:
            yield 'dummy'

    def insertion_sort_with_duplicate(self, a):
        for move in self.insert(a, 3, 2):
            yield move
        for move in self.insert(a, 4, 0):
            yield move
        for move in self.insert(a, 5, 1):
            yield move
        while True:
            yield 'dummy'

    def quick_sort(self, a):
        for move in self.swap(a, 1, 4):
            yield move
        for move in self.swap(a, 0, 1):
            yield move
        for move in self.swap(a, 3, 4):
            yield move
        for move in self.swap(a, 2, 3):
            yield move
        for move in self.swap(a, 5, 6):
            yield move
        while True:
            yield 'dummy'

    def quick_sort_with_duplicate(self, a):
        for move in self.swap(a, 1, 5):
            yield move
        for move in self.swap(a, 2, 4):
            yield move
        for move in self.swap(a, 0, 2):
            yield move
        for move in self.swap(a, 4, 5):
            yield move
        while True:
            yield 'dummy'

    def bubble_sort(self, a):
        for move in self.swap(a, 3, 4):
            yield move
        for move in self.swap(a, 5, 6):
            yield move
        for move in self.swap(a, 2, 3):
            yield move
        for move in self.swap(a, 1, 2):
            yield move
        for move in self.swap(a, 0, 1):
            yield move
        while True:
            yield 'dummy'

    def bubble_sort_with_duplicate(self, a):
        for move in self.swap(a, 2, 3):
            yield move
        for move in self.swap(a, 3, 4):
            yield move
        for move in self.swap(a, 4, 5):
            yield move
        for move in self.swap(a, 2, 3):
            yield move
        for move in self.swap(a, 3, 4):
            yield move
        for move in self.swap(a, 1, 2):
            yield move
        for move in self.swap(a, 2, 3):
            yield move
        for move in self.swap(a, 0, 1):
            yield move
        for move in self.swap(a, 1, 2):
            yield move
        while True:
            yield 'dummy'

    def write_array_init(self, nums, side_length):
        self.a0 = Array(nums, side_length)

        self.play(
               FadeIn(self.a0),
           )
        self.wait(1.5)

    def scale_copy_move(self, rt, rt1):
        scale_factor = 0.6
        self.play(
               ApplyMethod(self.a0.scale, scale_factor), run_time=0.4
             )

        self.a0.set_scale(scale_factor)

        self.a1 = self.a0.deepcopy()
        self.a2 = self.a0.deepcopy()
        self.a3 = self.a0.deepcopy()
        self.a4 = self.a0.deepcopy()

        self.play(
            ApplyMethod(self.a1.set_color, YELLOW),
            ApplyMethod(self.a2.set_color, YELLOW),
            ApplyMethod(self.a3.set_color, YELLOW),
            ApplyMethod(self.a4.set_color, YELLOW),
            run_time=0.1
        )
        self.a0.generate_target()
        self.a0.target.shift(self.dir0)

        self.a1.generate_target()
        self.a1.target.shift(self.dir1)

        self.a2.generate_target()
        self.a2.target.shift(self.dir2)

        self.a3.generate_target()
        self.a3.target.shift(self.dir3)

        self.a4.generate_target()
        self.a4.target.shift(self.dir4)

        self.play(
                   FadeOut(self.header),
                   MoveToTarget(self.a0),
                   MoveToTarget(self.a1),
                   MoveToTarget(self.a2),
                   MoveToTarget(self.a3), 
                   MoveToTarget(self.a4), run_time=rt
                  )
        self.wait(rt1)

        self.text0 = TextMobject("Input Array")
        self.text1 = TextMobject("Selection Sort")
        self.text2 = TextMobject("Quick Sort")
        self.text3 = TextMobject("Insertion Sort")
        self.text4 = TextMobject("Bubble Sort")

        self.text0.next_to(self.a0, buff=5*SMALL_BUFF)
        self.text1.next_to(self.a1, buff=5*SMALL_BUFF)
        self.text2.next_to(self.a2, buff=5*SMALL_BUFF)
        self.text3.next_to(self.a3, buff=5*SMALL_BUFF)
        self.text4.next_to(self.a4, buff=5*SMALL_BUFF)

        self.play(Write(self.text0), run_time=rt)
        self.play(Write(self.text1), run_time=rt) 
        self.play(Write(self.text2), run_time=rt) 
        self.play(Write(self.text3), run_time=rt) 
        self.play(Write(self.text4), run_time=rt)

    def play_sorting(self):
        self.sort1 = self.selection_sort(self.a1)
        self.sort2 = self.quick_sort(self.a2)
        self.sort3 = self.insertion_sort(self.a3)
        self.sort4 = self.bubble_sort(self.a4)

        for m1, m2, m3, m4 in zip(self.sort1, self.sort2, self.sort3, self.sort4):
            if [m1, m2, m3, m4].count('dummy') == 4:
                break
            moves = []
            if m1 != 'dummy':
                moves += m1
            if m2 != 'dummy':
                moves += m2
            if m3 != 'dummy':
                moves += m3
            if m4 != 'dummy':
                moves += m4
            self.play(*moves, run_time=1.3)

    def play_sorting_with_duplicate(self):
        self.sort1 = self.selection_sort_with_duplicate(self.a1)
        self.sort2 = self.quick_sort_with_duplicate(self.a2)
        self.sort3 = self.insertion_sort_with_duplicate(self.a3)
        self.sort4 = self.bubble_sort_with_duplicate(self.a4)

        for m1, m2, m3, m4 in zip(self.sort1, self.sort2, self.sort3, self.sort4):
            if [m1, m2, m3, m4].count('dummy') == 4:
                break
            moves = []
            if m1 != 'dummy':
                moves += m1
            if m2 != 'dummy':
                moves += m2
            if m3 != 'dummy':
                moves += m3
            if m4 != 'dummy':
                moves += m4
            self.play(*moves, run_time=0.2)

    def collapse_sorting(self):
        self.a0.generate_target()
        self.a0.target.shift(-self.dir0)

        self.play(
                   MoveToTarget(self.a0),
                   FadeOut(self.a1),
                   FadeOut(self.a2),
                   FadeOut(self.a3), 
                   FadeOut(self.a4),
                   FadeOut(self.text0),
                   FadeOut(self.text1),
                   FadeOut(self.text2),
                   FadeOut(self.text3),
                   FadeOut(self.text4), run_time=1.0
                  )
        self.wait(1)

        scale_factor = 1.0 / 0.6
        self.play(
               ApplyMethod(self.a0.scale, scale_factor),
        )
        self.a0.set_scale(scale_factor)
        self.wait(6)

    def create_duplicate_numbers(self):
        # 0    1   2   3   4   5   6
        #[15, 18, 21, 23, 14, 28, 24]
        #[15, 18, 21, 18, 14, 14, 20]
        self.c3 = Circle().scale(0.5)
        self.c3.next_to(self.a0.array[2], buff=SMALL_BUFF)

        self.play(
              Write(self.c3), 
           )

        t = TextMobject("18")
        t.move_to((self.a0.nums_t[3].get_x(), self.a0.nums_t[3].get_y(), 0))

        self.play(
             Transform(self.a0.nums_t[3], t),
          )
        self.play(FadeOut(self.c3))
        
        self.enlarge_and_shrink_no_brace(self.a0, [1, 3])

        self.wait(0.5)
        self.d5 = Circle().scale(0.5)
        self.d5.next_to(self.a0.array[4], buff=SMALL_BUFF)

        self.play(
              Write(self.d5), 
           )

        s = TextMobject("14")
        s.move_to((self.a0.nums_t[5].get_x(), self.a0.nums_t[5].get_y(), 0))

        self.play(
             Transform(self.a0.nums_t[5], s),
          )
        self.play(FadeOut(self.d5))

        self.enlarge_and_shrink_no_brace(self.a0, [4, 5])
        self.wait(4.0)

        u1 = TexMobject("18_1")
        u2 = TexMobject("18_2")
        one, three = self.a0.nums_t[1], self.a0.nums_t[3]
        u1.move_to((one.get_x(), one.get_y(), 0))
        u2.move_to((three.get_x(), three.get_y(), 0))
        self.play(
             Transform(one, u1),
             Transform(three, u2),
            )

        self.wait(5.0)
        v1 = TexMobject("14_1")
        v2 = TexMobject("14_2")
        four, five = self.a0.nums_t[4], self.a0.nums_t[5]
        v1.move_to((four.get_x(), four.get_y(), 0))
        v2.move_to((five.get_x(), five.get_y(), 0))
        self.play(
             Transform(four, v1),
             Transform(five, v2),
            )

    def enlarge_and_shrink_no_brace(self, array, elems):
        i1 = array.seq[elems[0]]
        i2 = array.seq[elems[1]]
        scale = 1.2

        writes = [
               ApplyMethod(array.nums_t[i1].scale, scale),
               ApplyMethod(array.nums_t[i2].scale, scale),
            ]
        self.play(
            *writes, run_time=0.5
        )

        writes = [
               ApplyMethod(array.nums_t[i1].scale, 1.0 / scale),
               ApplyMethod(array.nums_t[i2].scale, 1.0 / scale),
            ]
        self.play(
            *writes, run_time=0.5
        )

    def enlarge_and_shrink_item(self, array, elems):
        i1 = array.seq[elems[0]]
        i2 = array.seq[elems[1]]
        scale = 1.5

        self.brace = Brace(VGroup(array.nums_t[i1], array.nums_t[i2]), DOWN)
        writes = [
               ApplyMethod(array.nums_t[i1].scale, scale),
               ApplyMethod(array.nums_t[i2].scale, scale),
               Write(self.brace)
            ]

        self.play(
            *writes, run_time=1.0
        )

        self.play(
            ApplyMethod(array.nums_t[i1].scale, 1.0 / scale),
            ApplyMethod(array.nums_t[i2].scale, 1.0 / scale),
            FadeOut(self.brace, run_time=1.0)
        )
        
    def get_img(self, img, color):
        r = SVGMobject(file_name='icons/' + img + '.svg', color=color)
        r.scale(0.25)
        return r
        
    def get_check(self):
        return self.get_img('checkmark', GREEN)

    def get_cross(self):
        return self.get_img('delete', RED)

    def enlarge_and_shrink_add_symbol(self):
        #Selection sort
        #self.enlarge_and_shrink_item(self.a1, [0, 1])
        self.enlarge_and_shrink_item(self.a1, [3, 4])
        self.r1 = self.get_cross()
        self.r1.next_to(self.text1)
        self.play(Write(self.r1), run_time=1.0)

        #Quick sort
        self.wait(1)
        #self.enlarge_and_shrink_item(self.a2, [0, 1])
        self.enlarge_and_shrink_item(self.a2, [3, 4])
        self.r2 = self.get_cross()
        self.r2.next_to(self.text2)
        self.play(Write(self.r2), run_time=1.0)

        self.shift_left()
        self.do_grouping_1()
        #Insertion sort
        self.wait(2.3)
        self.enlarge_and_shrink_item(self.a3, [3, 4])
        self.enlarge_and_shrink_item(self.a3, [0, 1])
        self.r3 = self.get_check()
        self.r3.next_to(self.text3)
        self.play(Write(self.r3), run_time=1.0)
        self.wait(10)

        #Bubble sort
        #self.enlarge_and_shrink_item(self.a4, [0, 1])
        #self.enlarge_and_shrink_item(self.a4, [3, 4])
        self.r4 = self.get_check()
        self.r4.next_to(self.text4)
        self.play(Write(self.r4), run_time=1.0)
        self.do_grouping_2()

    def shift_left(self):
        v = VGroup(
                self.a0, 
                self.a1,
                self.a2,
                self.a3,
                self.a4,
                self.text0, 
                self.text1,
                self.text2,
                self.text3,
                self.text4,
                self.r1,
                self.r2,
             )
        v.generate_target()
        v.target.shift(2 * LEFT)
        self.play(MoveToTarget(v))

    def do_grouping_1(self):
        brace_1 = Brace(VGroup(self.r1, self.r2), RIGHT)
        brace_text_1 = TextMobject("Unstable Algos")
        brace_text_1.next_to(brace_1, RIGHT)
        self.play(Write(brace_1), Write(brace_text_1))
         
    def do_grouping_2(self):
        brace_2 = Brace(VGroup(self.r3, self.r4), RIGHT)
        brace_text_2 = TextMobject("Stable Algos")
        brace_text_2.next_to(brace_2, RIGHT)
        self.play(Write(brace_2), Write(brace_text_2))

    def show_header(self):
        self.header = TextMobject("What is stability in sorting algorithm?", color=BLUE)
        self.header.to_edge(UP, buff=5*SMALL_BUFF)
        self.play(Write(self.header))

    def construct(self):
        nums = [15, 18, 21, 23, 14, 28, 24]
        side_length = 1.15
        d0 = 3.1
        delta = 1.4

        self.dir0 = d0                 * UP + 2 * LEFT
        self.dir1 = (d0 - 1.3 * delta) * UP + 2 * LEFT
        self.dir2 = (d0 - 2.3 * delta) * UP + 2 * LEFT
        self.dir3 = (d0 - 3.3 * delta) * UP + 2 * LEFT
        self.dir4 = (d0 - 4.3 * delta) * UP + 2 * LEFT

        self.show_header()
        self.wait(2)
        self.write_array_init(nums, side_length)
        self.scale_copy_move(1.0, 0.4)

        self.play_sorting()

        self.collapse_sorting()
        self.create_duplicate_numbers()
        self.wait(1.7)
        self.scale_copy_move(0.8, 0)
        self.play_sorting_with_duplicate()
        self.enlarge_and_shrink_add_symbol()
        self.wait(2)

class Bag(Scene):
    def get_bag(self):
        r = SVGMobject(file_name='icons/bag.svg', color=RED)
        r.scale(0.7)
        return r

    def construct(self):
        nums = [15, 18, 21, 23, 14, 28, 24]
        side_length = 1.15
        self.a0 = Array(nums, side_length)

        self.play(
               Write(self.a0),
           )
         
        self.wait(2)
        bags = [self.get_bag() for _ in range(len(nums))]
        for idx, bag in enumerate(bags):
            bag.next_to(self.a0.nums_t[idx], DOWN, buff=0)

        self.play(*[Write(bag) for bag in bags])
        self.wait(2.2)

class Marks(Scene):
    def get_sorted_scores(self):
        scores = [
            {'name': 'Saurav',  'marks': 29},
            {'name': 'Tanmay', 'marks': 27},
            {'name': 'Rahul',  'marks': 27},
            {'name': 'Mahesh', 'marks': 24}, 
            {'name': 'Sachin', 'marks': 21},
            {'name': 'Pankaj', 'marks': 16},
            {'name': 'Suresh', 'marks': 15}, 
            {'name': 'Arvind', 'marks': 14},
            {'name': 'Neerav', 'marks': 10}, 
            {'name': 'Kushal', 'marks': 10},
            {'name': 'Madhav', 'marks': 9},
            {'name': 'Sooraj',   'marks': 7},
        ]
        for score in scores:
            yield score

    def get_names(self):
        names = ['Mahesh', 'Suresh', 'Neerav', 'Madhav', 'Kushal', 'Saurav', 'Tanmay', 'Pankaj', 'Rahul', 'Sachin', 'Ravi', 'Arvind']
        for name in names:
            yield name

    def get_marks(self):
         marks = [24, 15, 10, 9, 10, 29, 27, 16, 27, 21, 7, 14]
         for mark in marks:
             yield mark

    def get_elems(self):
        names, marks = self.get_names(), self.get_marks()
        for name, mark in zip(names, marks):
            s = Square(side_length=2)
            m = TextMobject(str(mark)).scale(1.4)
            n = TextMobject(name).scale(0.8)
            n.next_to(m, DOWN)
            v = VGroup(s, n, m)
            v.m = m
            v.n = n
            yield v
        
    def write_part(self, group, elems, prev, n, scale):
        for _ in range(n):
            elem = next(elems)
            elem.scale(scale)
            elem.next_to(prev, buff=0)
            prev = elem
            self.play(FadeIn(elem))
            group.add(elem)
            self.group.elems.append(elem)
        return prev
        
    def write_array(self):
        elems = self.get_elems()
        self.group = VGroup()
        self.group.elems = []

        prev = next(elems)
        pivot = prev
        self.group.add(prev)
        self.group.elems.append(prev)
        self.play(FadeIn(prev))

        prev = self.write_part(self.group, elems, prev, 3, 1)
        pt = (pivot.get_x() - 10, pivot.get_y(), 0)
        scale = 0.6
        self.play(
            self.group.scale, scale, {"about_point": pt}
        )
        prev = self.write_part(self.group, elems, prev, 5, scale)

        pt = (pivot.get_x() - 16, pivot.get_y(), 0)
        scale = 0.9
        self.play(
            self.group.scale, scale, {"about_point": pt}
        )
        self.write_part(self.group, elems, prev, 3, scale * 0.6)

    def highlight_individual(self, i, rt=0.5):
        scale = 1.2
        elem_func_m = self.group.elems[i].m.scale
        elem_func_n = self.group.elems[i].n.scale
        self.play(
               ApplyMethod(elem_func_m, scale), 
               ApplyMethod(elem_func_n, scale), 
               run_time=rt
            )
        self.play(
               ApplyMethod(elem_func_m, 1.0 / scale), 
               ApplyMethod(elem_func_n, 1.0 / scale), 
               run_time=rt
            )

    def highlight_individual_in_table(self, i):
        scale = 1.2
        elem_func_sn  = self.row_group.elems[i].sn.scale
        elem_func_mark = self.row_group.elems[i].mark.scale
        elem_func_name = self.row_group.elems[i].name.scale
        self.play(
               ApplyMethod(elem_func_sn, scale), 
               ApplyMethod(elem_func_mark, scale), 
               ApplyMethod(elem_func_name, scale), 
               run_time=0.5
            )
        self.play(
               ApplyMethod(elem_func_sn, 1.0 / scale), 
               ApplyMethod(elem_func_mark, 1.0 / scale), 
               ApplyMethod(elem_func_name, 1.0 / scale), 
               run_time=0.5
            )

    def move_up(self):
        self.group.generate_target()
        self.group.target.shift(3 * UP)
        self.play(MoveToTarget(self.group))

    def get_one_row(self, sno, name, mark):
        outer_rect = Rectangle(width=5, height=1)

        sn_rect = Rectangle(width=1, height=1)
        sn_rect.next_to(outer_rect.get_left(), buff=0)
        sn = TextMobject(str(sno))        
        sn.next_to(sn_rect.get_left())

        name_rect = Rectangle(width=3, height=1)
        name_rect.next_to(sn_rect, buff=0)
        name = TextMobject(name)
        name.next_to(name_rect.get_left())

        mark_rect = Rectangle(width=1, height=1)
        mark_rect.next_to(name_rect, buff=0)
        mark = TextMobject(str(mark))
        mark.next_to(mark_rect.get_left())

        group = VGroup()
        group.add(sn)
        group.add(name)
        group.add(mark)
        group.sn = sn
        group.name = name
        group.mark = mark
        return group

    def write_leaderboard(self):
        self.header = TextMobject("\\normalfont\\calligra Leaderboard")

        self.outer_rect = Rectangle(width=5, height=6)
        self.outer_rect.next_to(self.group, DOWN)

        self.header.next_to(self.outer_rect.get_top(), DOWN)

        h_line = Line(self.outer_rect.get_left(), self.outer_rect.get_right())
        h_line.scale(0.8)
        h_line.set_stroke(width = 2)
        h_line.next_to(self.header, DOWN)

        self.play(Write(self.outer_rect), Write(self.header))

        self.row_group = Group()
        self.row_group.elems = []

        sorted_scores = self.get_sorted_scores()
        score = next(sorted_scores)
        prev_rect = self.get_one_row(1, score['name'], score['marks'])
        prev_rect.next_to(self.header, DOWN)
        self.row_group.elems.append(prev_rect)
        self.play(Write(prev_rect))

        for i in range(2, 11):
            score = next(sorted_scores)
            name, mark = score['name'], score['marks']
            rect = self.get_one_row(i, name, mark)
            rect.next_to(prev_rect, DOWN, buff=SMALL_BUFF)
            self.row_group.elems.append(rect)
            self.play(Write(rect))
            prev_rect = rect

    def explain_leaderboard(self):
        pt1 = [self.group.elems[6].get_x(), self.group.elems[6].get_y(), 0]
        pt3 = [self.row_group.elems[1].get_x(), self.row_group.elems[1].get_y(), 0]
        self.line1 = Arrow(pt1, pt3)
        self.play(ShowCreation(self.line1))

        qt1 = [self.group.elems[8].get_x(), self.group.elems[8].get_y(), 0]
        qt3 = [self.row_group.elems[2].get_x(), self.row_group.elems[2].get_y(), 0]
        self.line2 = Arrow(qt1, qt3)
        self.play(ShowCreation(self.line2))

    def construct(self):
        self.write_array()
        self.move_up()
        self.highlight_individual(0)
        self.wait(4.0)
        self.highlight_individual(1)
        self.wait(1.5)
        self.highlight_individual(2, rt=0.1)
        self.highlight_individual(3, rt=0.1)
        self.highlight_individual(4, rt=0.1)
        self.highlight_individual(5, rt=0.1)
        self.highlight_individual(6, rt=0.1)
        self.highlight_individual(7, rt=0.1)
        self.write_leaderboard()
        self.wait(10.4)
        self.highlight_individual(6, rt=0.4)
        self.highlight_individual(8)
        self.wait(1.9)
        self.highlight_individual_in_table(1)
        self.wait(1)
        self.highlight_individual_in_table(2)
        self.wait(1)
        self.explain_leaderboard()
        self.wait(3.8)

class RadixSort(Scene):
    def show_header(self):
        self.header = TextMobject("Radix Sort", color=BLUE).scale(1.5)
        self.header.to_edge(UP)
        self.play(Write(self.header))

    def show_numbers(self):
        self.arr = ['45635', '23049', '30458', '12303', '04834', '40404']
        
        self.group = VGroup()
        self.group.elems = []
        t_obj = TextMobject(self.arr[0])
        t_obj.next_to(self.header, DOWN, buff=LARGE_BUFF)
        self.group.elems.append(t_obj)
        self.group.add(t_obj)
        prev = t_obj
        self.play(Write(t_obj), run_time=0.6)

        for i in range(1, len(self.arr)):
            t_obj = TextMobject(self.arr[i])
            t_obj.next_to(prev, DOWN, buff=2*SMALL_BUFF)
            self.group.elems.append(t_obj)
            self.group.add(t_obj)
            prev = t_obj
            self.play(Write(t_obj), run_time=0.6)

    def step(self, init_group, shifts, step_size, rt=1.0):
        group1 = init_group.deepcopy()

        moves = []
        for i in range(len(self.arr)):
            elem = group1.elems[self.seq[i]]
            elem.generate_target()
            elem.target.shift((2.4, shifts[i] * step_size, 0))
            moves.append(MoveToTarget(elem))

        self.play(*moves, run_time=rt)

        new_seq = [-1] * 6
        for i in range(len(self.seq)):
            new_seq[i + shifts[i]] = self.seq[i]
        self.seq = new_seq

        return group1

    def add_next_column(self, prev_group, shifts, step_size, rt=1.0):
        new_group = self.step(prev_group, shifts, step_size, rt)
        self.groups.add(new_group)
        self.groups.elems.append(new_group)
        return new_group

    def add_arrow(self, i, text, rt=1.0):
        one = self.groups.elems[i].get_bottom()
        two = self.groups.elems[i + 1].get_bottom()
        arrow = CurvedArrow(one, two)
        text = TextMobject(text).scale(0.6)
        text.next_to(arrow, DOWN)
        self.groups.sorting_texts.append(text)
        self.play(Write(arrow), Write(text), run_time=rt)
        self.groups.add(arrow, text)

    def shift_left(self):
        self.groups.generate_target()
        self.groups.target.shift(6 * LEFT)
        self.play(MoveToTarget(self.groups), run_time=1)

    def add_rect(self, i, rt=1.0):
        rect = Rectangle(width=0.25, height=3.2, color=YELLOW)
        rect.next_to(self.groups.elems[i].get_right(), LEFT, buff=i*0.25)
        self.groups.add(rect)
        self.groups.rects.append(rect)
        self.play(Write(rect), run_time=rt)

    def shrink_and_get_back_group5(self):
        scale = 1.2
        s1 = [self.groups.elems[4].elems[i] for i in range(6)]
        s1 += self.groups.rects[4]
        g = Group(*s1)
        self.play(ApplyMethod(g.scale, scale), run_time=0.5)

        scale = 1.0 / 1.2
        self.play(ApplyMethod(g.scale, scale), run_time=0.5)

    def construct(self):
        self.show_header()
        t1 = TextMobject("Needs a stable sort as subroutine").scale(1.7)
        self.play(Write(t1))
        self.wait(8)
        self.play(FadeOut(t1))
        self.show_numbers()
        self.wait(1.2)

        step_size = self.group.elems[1].get_y() - self.group.elems[0].get_y()

        self.seq = [0, 1, 2, 3, 4, 5]
        self.groups = VGroup()
        self.groups.elems = []
        self.groups.sorting_texts = []
        self.groups.rects = []

        self.groups.add(self.group)
        self.groups.elems.append(self.group)

        shifts = [3, 4, 2, -3, -3, -3]
        self.add_rect(0)
        new_group = self.add_next_column(self.group, shifts, step_size)
        self.add_arrow(0, "Sort by \\\\last digit")
        self.wait(4)
        self.shift_left()
        self.wait(2.8)

        shifts = [0, 1, -1, 0, 1, -1]
        self.add_rect(1)
        new_group = self.add_next_column(new_group, shifts, step_size, rt=0.6)
        self.add_arrow(1, "Sort by second \\\\last digit", rt=0.5)
        
        shifts = [1, 1, 3, 1, -4, -2]
        self.add_rect(2)
        new_group = self.add_next_column(new_group, shifts, step_size, rt=0.5)
        self.add_arrow(2, "Sort by \\\\third digit", rt=0.5)

        shifts = [3, 1, -2, -2, 1, -1]
        self.add_rect(3)
        new_group = self.add_next_column(new_group, shifts, step_size, rt=0.4)
        self.add_arrow(3, "Sort by \\\\second digit", rt=0.3)

        shifts = [4, 2, -1, -1, -4, 0]
        self.add_rect(4)
        new_group = self.add_next_column(new_group, shifts, step_size, rt=0.2)
        self.add_arrow(4, "Sort by \\\\first digit",rt=0.5)
        self.wait(3)

        exclaim = TextMobject("Sorted!", color=GREEN)
        exclaim.next_to(self.groups.elems[5], DOWN, buff=LARGE_BUFF)

        e_a = Arrow(self.groups.elems[5].get_bottom(), exclaim.get_top(), buff=0, color=GREEN)

        r = SVGMobject(file_name='icons/checkmark.svg', color=GREEN)
        r.scale(0.25)
        r.next_to(exclaim, DOWN)
        self.play(Write(e_a), Write(exclaim), Write(r))

        self.wait(6)

        text = TextMobject("Use a stable sort for these \\\\typically, counting sort").scale(0.7)
        text.to_edge(DOWN, buff=0)
        self.play(Write(text))

        a_s = []
        for t in self.groups.sorting_texts:
            a_s.append(Write(Arrow(t.get_bottom(), text.get_top())))
        self.play(*a_s)

        self.wait(7)
        self.shrink_and_get_back_group5()
        self.wait(2)
        text = TextMobject("40404 is before 45635\\\\because 0404 $<$ 5635")
        text.scale(0.8)
        text.next_to(self.groups.elems[4], UP, buff=5*SMALL_BUFF)
        self.play(Write(text))

        self.wait(12)
        a1 = Arrow(self.groups.elems[4].elems[5], self.groups.elems[5].elems[5], buff=0)
        self.play(Write(a1))
        a2 = Arrow(self.groups.elems[4].elems[0], self.groups.elems[5].elems[0], buff=0)
        self.play(Write(a2))
        self.wait(8)

class StableAlgos(Scene):
    def write_header(self):
        self.header = TextMobject("Which sorting algos are stable?", color=BLUE)
        self.header.to_edge(TOP, buff=SMALL_BUFF)
        self.play(Write(self.header))

    def any_algo(self):
        self.any_algo = TextMobject("Any sorting algo has stable version\\\\but there can be additional time/space complexities")
        self.any_algo.next_to(self.header, DOWN, buff=LARGE_BUFF)
        self.play(Write(self.any_algo))

    def write_reason(self):
        #s1 = "Merge, Insertion, Counting sorts"
        #t1 = TextMobject("Merge, Insertion, Counting sorts:\\\\ No swaps $\\Rightarrow$ Stable", substrings_to_isolate=[s1])
        #t1.algo_part = t1.get_part_by_tex(s1)
        #t1.algo_part.set_color(GREEN)

        s1 = "Swaps"
        s2 = "non adjacent"
        self.reason = TextMobject("Swaps of non adjacent elements \\\\are the root cause of instability \\\\of sorting algorithms", substrings_to_isolate=[s1, s2]).scale(1.2)
        self.reason.s1 = self.reason.get_part_by_tex(s1)
        self.reason.s1.set_color(GREEN)
        self.reason.s2 = self.reason.get_part_by_tex(s2)
        self.reason.s2.set_color(GREEN)

        self.reason.next_to(self.any_algo, DOWN, buff=LARGE_BUFF)
        self.play(Write(self.reason))

    def write_array(self):
        nums = ["-", "-", "18_1", "-", "18_2", "-", "-", "14"]
        side_length = 1.15
        self.a0 = Array(nums, side_length)
        self.a0.next_to(self.reason, DOWN, buff=10*SMALL_BUFF)
        self.play(Write(self.a0))

    def write_second_array(self):
        nums = ["-", "-", "18_1", "18_2", "-", "-", "14"]
        side_length = 1.15
        self.a1 = Array(nums, side_length)
        self.a1.next_to(self.a0, DOWN)
        self.play(Write(self.a1))

        self.brace =  Brace(VGroup(self.a1.nums_t[2], self.a1.nums_t[3]), DOWN)
        self.play(Write(self.brace))

    def play_array(self):
        l, f = 7, 2
        diff = l - f
        self.play(self.a0.move_up(l), self.a0.move_down(f))
        self.play(self.a0.move_left(l, diff), self.a0.move_right(f, diff))
        self.play(self.a0.move_down(l), self.a0.move_up(f))

    def enlarge_and_shrink_18s(self):
        scale = 1.2
        self.play(
             ApplyMethod(self.a0.nums_t[2].scale, scale),
             ApplyMethod(self.a0.nums_t[4].scale, scale), 
             run_time=0.5
        )
        self.play(
             ApplyMethod(self.a0.nums_t[2].scale, 1.0 / scale),
             ApplyMethod(self.a0.nums_t[4].scale, 1.0 / scale), 
             run_time=0.5
        )

    def emphasize_18s(self):
        scale = 1.2
        self.play(ApplyMethod(self.a0.nums_t[2].scale, scale), run_time=0.5)
        self.play(ApplyMethod(self.a0.nums_t[2].scale, 1.0 / scale), run_time=0.5)
        self.wait(0.7)
        self.play(ApplyMethod(self.a0.nums_t[4].scale, scale), run_time=0.5)
        self.play(ApplyMethod(self.a0.nums_t[4].scale, 1.0 / scale), run_time=0.5)
        
    def shift_up(self):
        g = Group(self.header, self.reason, self.any_algo)
        g.generate_target()
        g.target.shift(3 * UP)
        self.play(MoveToTarget(g))

    def move_all_up(self):
        g = Group(self.a0, self.header, self.reason, self.a1, self.brace)
        g.generate_target()
        g.target.shift(5 * UP)
        self.play(MoveToTarget(g))

    def get_img(self, img, color):
        r = SVGMobject(file_name='icons/' + img + '.svg', color=color)
        r.scale(0.25)
        return r
        
    def get_check(self):
        return self.get_img('checkmark', GREEN)

    def get_cross(self):
        return self.get_img('delete', RED)

    def describe_algos(self):
        s1 = "Merge, Insertion, Counting sorts"
        t1 = TextMobject("Merge, Insertion, Counting sorts:\\\\ No swaps $\\Rightarrow$ Stable", substrings_to_isolate=[s1])
        t1.algo_part = t1.get_part_by_tex(s1)
        t1.algo_part.set_color(GREEN)

        l1 = Line(LEFT, RIGHT, color=BLUE).scale(5)

        s2 = "Bubble sort"
        t2 = TextMobject("Bubble sort: \\\Swaps only adjacent elements $\\Rightarrow$ Stable", substrings_to_isolate=[s2])
        t2.algo_part = t2.get_part_by_tex(s2)
        t2.algo_part.set_color(GREEN)

        l2 = Line(LEFT, RIGHT, color=BLUE).scale(5)

        s3 = "Quick, Heap, Selection sorts"
        t3 = TextMobject("Quick, Heap, Selection sorts: \\\\Swap non adjacent elements $\\Rightarrow$ Not Stable", substrings_to_isolate=[s3])
        t3.algo_part = t3.get_part_by_tex(s3)
        t3.algo_part.set_color(GREEN)

        t = VGroup(t1, l1, t2, l2, t3).arrange(DOWN)
        t.next_to(self.brace, DOWN)

        check1 = self.get_check()
        check1.next_to(t1)
        
        check2 = self.get_check()
        check2.next_to(t2)

        cross = self.get_cross()
        cross.next_to(t3)

        self.play(Write(t1))
        self.play(Write(check1))
        self.wait(2)
        self.play(Write(l1))
        self.play(Write(t2))
        self.play(Write(check2))
        self.wait(0.5)
        self.play(Write(l2))
        self.play(Write(t3))
        self.play(Write(cross))
        self.wait(11)
        
    def construct(self):
        self.write_header()
        self.wait(8)
        self.any_algo()
        self.wait(14)
        self.write_reason()
        self.shift_up()
        self.wait(12)
        self.write_array()
        self.enlarge_and_shrink_18s()
        self.wait(7)
        self.play_array()
        self.wait(1)
        self.emphasize_18s()
        self.wait(20.5)
        self.write_second_array()
        self.wait(8)
        self.move_all_up()
        self.describe_algos()

class AnotherWay(Scene):
    def write_header(self):
        self.header = TextMobject("Impossibility trinity for comparison sorts", color=BLUE)
        self.header.to_edge(TOP, buff=SMALL_BUFF)
        self.play(Write(self.header))

    def enlarge_and_shrink(self, elem):
        scale = 1.2
        self.play(ApplyMethod(elem.scale, scale),  run_time=0.5)
        self.play(ApplyMethod(elem.scale, 1.0 / scale),  run_time=0.5)

    def draw_triangle(self):
        self.triangle = Triangle().scale(3)
        self.triangle.next_to(self.header, DOWN, buff=LARGE_BUFF)
        self.play(Write(self.triangle))

        self.wait(0.5)
        self.t1 = TextMobject("$O(n\\log{}n)$ time", color=YELLOW)
        self.t1.next_to(self.triangle.get_vertices()[0], UP)
        self.play(Write(self.t1))

        self.wait(0.5)
        self.t2 = TextMobject("$O(1)$ extra space", color=YELLOW)
        self.t2.next_to(self.triangle.get_vertices()[1], DOWN)
        self.play(Write(self.t2))

        self.wait(0.5)
        self.t3 = TextMobject("Stability", color=YELLOW)
        self.t3.next_to(self.triangle.get_vertices()[2], DOWN)
        self.play(Write(self.t3))

        self.wait(5.5)
        self.enlarge_and_shrink(self.t1)
        self.wait(5.5)
        self.enlarge_and_shrink(self.t2)
        self.wait(1)
        self.enlarge_and_shrink(self.t3)
        self.wait(2)
        self.t0 = TextMobject("Choose \\\\any two", color=PINK)
        self.t0.next_to(self.triangle.get_vertices()[0], DOWN, buff=2*LARGE_BUFF)
        self.play(Write(self.t0))

        self.wait(4)
        self.t12 = TextMobject("Quick Sort\\\\Heap Sort").scale(0.8)
        self.t12.next_to(self.t0, LEFT)

        self.dot0 = Dot(color=GREEN, radius=0.3)
        self.dot0.move_to(self.triangle.get_vertices()[0])
        self.dot1 = Dot(color=GREEN, radius=0.3)
        self.dot1.move_to(self.triangle.get_vertices()[1])
        self.dot2 = Dot(color=GREEN, radius=0.3)
        self.dot2.move_to(self.triangle.get_vertices()[2])
        self.play(FadeIn(self.dot0), FadeIn(self.dot1), Write(self.t12))

        self.wait(13)
        self.t23 = TextMobject("Merge Sort").scale(0.8)
        self.t23.next_to(self.t0, RIGHT)
        self.play(Write(self.t23), FadeOut(self.dot1), FadeIn(self.dot2))

        self.wait(9)
        self.t13 = TextMobject("Insertion Sort\\\\Bubble Sort").scale(0.8)
        self.t13.next_to(self.t0, DOWN, buff=LARGE_BUFF)
        self.play(Write(self.t13), FadeIn(self.dot1), FadeOut(self.dot0))
        self.wait(10)
        self.play(FadeOut(self.dot1), FadeOut(self.dot2))

    def shift_left(self):
        g = Group(
            self.triangle, self.t1, self.t2, self.t3, self.t0,
            self.t12, self.t23, self.t13)
        g.generate_target()
        g.target.shift(2*LEFT)
        self.play(MoveToTarget(g), run_time=2)

    def selection_sort(self):
        self.s = TextMobject("Selection Sort: \\\\Why unstable despite \\\\$O(n^2)$ time?")
        self.s.to_edge(RIGHT)
        self.play(Write(self.s))

        self.wait(14)
        ans = TextMobject("Answer: $n$ shifts are \\\\replaced by 1 swap \\\\as an optimisation", substrings_to_isolate=['Answer'])
        ans.answer_part = ans.get_part_by_tex('Answer')
        ans.answer_part.set_color(GREEN)
        ans.next_to(self.s, DOWN)
        self.play(Write(ans))

    def construct(self):
        self.write_header()
        self.wait(9)
        self.draw_triangle()
        self.shift_left()
        self.selection_sort()
        self.wait(23)

class BigDeal(Scene):
    def construct(self):
        deal = TextMobject("What's the big deal?", color=BLUE).scale(2)
        deal.rotate(PI/12)
        self.play(Write(deal))
        self.wait(9)
        self.play(FadeOut(deal))

class GoodBye(Scene):
    def construct(self):
        bye = TextMobject("\\normalfont\\calligra Goodbye!", color=BLUE).scale(3)
        self.play(Write(bye))
        self.wait(3)

class Cover(Scene):
    def write_header(self):
        self.header = TextMobject("Impossibility trinity for comparison sorts", color=BLUE)
        self.header.to_edge(TOP, buff=SMALL_BUFF)
        self.play(Write(self.header))

    def enlarge_and_shrink(self, elem):
        scale = 1.2
        self.play(ApplyMethod(elem.scale, scale),  run_time=0.5)
        self.play(ApplyMethod(elem.scale, 1.0 / scale),  run_time=0.5)

    def draw_triangle(self):
        self.triangle = Triangle().scale(3)
        self.triangle.to_edge(TOP, buff=4*SMALL_BUFF)
        self.play(Write(self.triangle))

        self.t1 = TextMobject("$O(n\\log{}n)$ time", color=YELLOW).scale(1.3)
        self.t1.next_to(self.triangle.get_vertices()[0], UP)
        self.play(Write(self.t1))

        self.t2 = TextMobject("$O(1)$ space", color=YELLOW).scale(1.3)
        self.t2.next_to(self.triangle.get_vertices()[1], DOWN)
        self.play(Write(self.t2))

        self.t3 = TextMobject("Stability", color=YELLOW).scale(1.3)
        self.t3.next_to(self.triangle.get_vertices()[2], DOWN)
        self.play(Write(self.t3))

    def shift_left(self):
        g = Group(self.triangle, self.t1, self.t2, self.t3)
        g.generate_target()
        g.target.shift(2.7*LEFT)
        self.play(MoveToTarget(g), run_time=1)

    def message(self):
        self.s = TextMobject("Stable Sorting \\\\Algorithms").scale(2.7)
        self.s.to_edge(RIGHT + TOP)
        self.play(Write(self.s))

    def construct(self):
        self.draw_triangle()
        self.shift_left()
        self.message()
