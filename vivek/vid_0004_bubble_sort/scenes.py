from manimlib.imports import *
from manimlib.for_vivek_videos.array import Array
from vivek.vid_0004_bubble_sort.stick_man import StickMan
from vivek.vid_0004_bubble_sort.code import Code
import random

class Opening(Scene):
    def construct(self):
        text = TextMobject("Computer Science by Pandey")

        subtext = TextMobject("One video: One snack sized topic")
        VGroup(text, subtext).arrange(DOWN)
        self.play(FadeIn(text), FadeIn(subtext))
        self.wait(2)

class LastVideo(Scene):
    def move(self, src, dst):
        a = self.boxes.set_color(self.seq[src], RED)
        self.play(*a, run_time=0.5)
        self.play(self.boxes.Move(self.seq[src], UP, 3), run_time=0.5)
        self.play(self.boxes.Move(self.seq[src], LEFT, (self.seq[src] - self.seq[dst]) * 1.8 + 5.0), run_time=0.5)
        self.play(self.boxes.Move(self.seq[src], DOWN, 3), run_time=0.5)
        right_moves = [self.boxes.Move(self.seq[i], RIGHT, 1.8) for i in range(dst, src)]
        self.play(*right_moves, run_time=0.5)

    def construct(self):
        self.platform = Line(LEFT, RIGHT)
        self.platform.set_width(8)
        self.platform.to_edge(DOWN, buff = 2.95 * LARGE_BUFF)

        nums = [23, 25, 33, 28, 14, 17, 20]
        self.seq = [0, 1, 2, 3, 4, 5, 6]
        lengths = [num / 20 for num in nums]
        self.boxes = Array(len(nums), StickMan, lengths,  
                           buff=0.6 * LARGE_BUFF, aligned_edge=DOWN)
        g = VGroup(self.platform, self.boxes)
        g.scale(0.7)

        bar = "\_" * 12
        c = [ 
             TexMobject("n"),
             TexMobject("n-1"),
             TexMobject("\\vdots"),
             TexMobject("2"),
             TexMobject("1"),
             TexMobject(bar),
             TexMobject("n(n+1)/2"),
             TexMobject(bar)
        ]
        c1 = VGroup(*c).arrange(DOWN)
        c1.next_to(self.boxes)

        order = TexMobject("\\Rightarrow O(n^2)")
        g1 = VGroup(g, c1, order).arrange(RIGHT)
        order.next_to(c[-2], RIGHT)

        rect = SurroundingRectangle(g1, buff=LARGE_BUFF)

        name = TextMobject("Last video: Selection Sort")
        name.next_to(rect, DOWN)

        self.play(Write(rect))

        self.play(Write(self.boxes))
        self.play(Write(self.platform))

        self.play(Write(name))

        self.move(4, 0)
        self.seq = [4, 0, 1, 2, 3, 5, 6]
        #self.move(6, 0)
        self.play(Write(c1))
        self.play(Write(order))
        self.wait(1.5)

class IntroduceBubbleSort(Scene):
    def construct(self):
        this = TextMobject("This video")
        char = TextMobject("Humble and maligned")
        char.set_color(GREEN)
        topic = TextMobject("BUBBLE SORT").scale(2)
        topic.set_color(BLUE)
        g = VGroup(this, char, topic).arrange(DOWN)
        self.play(Write(this))
        self.wait(2)
        self.play(Write(char))
        self.wait(1)
        self.play(Write(topic))
        self.wait(6)

class MyCodeBubble(VGroup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        header = TextMobject("BUBBLE SORT", color="YELLOW")
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
        self.b = VGroup(header, *self.codes).arrange(DOWN).to_edge(RIGHT + DOWN)
        for i in range(0, len(self.codes)):
            x_diff = 0.8 + 0.65 * lines[i].count('SPACE')
            self.codes[i].align_to((x_diff, 0, 0), LEFT)
        self.add(header)
        self.add(self.b)

class MyCodeImprovedBubble(VGroup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        header = TextMobject("IMPROVED BUBBLE SORT", color="YELLOW")
        lines = [
            "for (i = 0; i < n; i++) \{",
            "SPACEflag = 0",
            "SPACEfor (j=0; j<n-1; j++) \{",
            "SPACESPACEif (A[j] > A[j+1]) \{",
            "SPACESPACESPACEtemp = A[j]",
            "SPACESPACESPACEA[j] = A[j + 1]",
            "SPACESPACESPACEA[j + 1] = temp",
            "SPACESPACESPACEflag = 1",
            "SPACESPACE\}",
            "SPACE\}",
            "SPACEif (flag == 0) \{",
            "SPACESPACEbreak",
            "SPACE\}",
            "\}"
        ]

        self.codes = [Code(line) for line in lines]
        self.b = VGroup(header, *self.codes).arrange(DOWN, buff=SMALL_BUFF).to_edge(RIGHT + DOWN)
        for i in range(0, len(self.codes)):
            x_diff = 0.8 + 0.65 * lines[i].count('SPACE')
            self.codes[i].align_to((x_diff, 0, 0), LEFT)
        self.add(header)
        self.add(self.b)
class MyCodeSelection(VGroup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        header = TextMobject("SELECTION SORT", color="YELLOW")
        lines = [
            "for (i = 0; i < n; i++) \{",
            "SPACEjmin = i",
            "SPACEfor (j = i; j < n; j++) \{",
            "SPACESPACEif (A[j] < A[jmin]) \{",
            "SPACESPACESPACEjmin = j",
            "SPACESPACE\}",
            "SPACE\}",
            "SPACEtemp = A[i]",
            "SPACEA[i] = A[jmin]",
            "SPACEA[jmin] = temp",
            "\}"
        ]
        self.codes = [Code(line) for line in lines]
        self.b = VGroup(header, *self.codes).arrange(DOWN).to_edge(RIGHT + DOWN)
        for i in range(0, len(self.codes)):
            x_diff = 0.8 + 0.65 * lines[i].count('SPACE')
            self.codes[i].align_to((x_diff, 0, 0), LEFT)
        self.add(header)
        self.add(self.b)

class Knuth(Scene):
    def construct(self):
        slow = TextMobject("Slowest of popular sorting algos", color="YELLOW")
        no_teach = TextMobject("Don't teach it!", color="RED")
        knuth = TextMobject("DONALD KNUTH", color=BLUE).scale(2)
        saying1 = TextMobject("The Bubble Sort seems to have ").scale(1.5)
        saying2 = TextMobject("nothing to recommend it except a ").scale(1.5)
        saying3 = TextMobject("catchy name and that it leads to").scale(1.5)
        saying4 = TextMobject("some intereting theoretical problems").scale(1.5)
        saying = VGroup(slow, no_teach, knuth, saying1, saying2, saying3, saying4).arrange(DOWN)
         
        self.play(Write(slow))
        self.wait(7)
        self.play(Write(no_teach))
        self.wait(2)
        self.play(Write(knuth)) 
        self.play(Write(saying1)) 
        self.play(Write(saying2)) 
        self.play(Write(saying3)) 
        self.play(Write(saying4)) 
        self.wait(4)

class WhySlow(Scene):
    def construct(self):
        why = TextMobject("Why is bubble sort so slow?").scale(1.5)
        why.to_edge(TOP, buff=3*SMALL_BUFF)
        self.play(Write(why)) 

        a1 = TextMobject("Worse complexity than merge, quick and heap sorts", color=BLUE)
        a2 = TextMobject("Those algos are $O(n\\log{}n)$", color=BLUE)
        a = VGroup(a1, a2).arrange(DOWN)
        a.next_to(why, DOWN, buff=5*SMALL_BUFF)
        self.play(Write(a))

        self.wait(4)
        b1 = TextMobject("Question: Why slower than selection/insertion sorts?", color=RED)
        b2 = TextMobject("Answer: Swaps!", color=RED)
        b = VGroup(b1, b2).arrange(DOWN)
        b.next_to(a, DOWN, buff=5*SMALL_BUFF)
        self.play(Write(b1))
        self.wait(4)
        self.play(Write(b2))
        self.wait(4)

        r = VGroup(why, a, b)
        r.generate_target()
        r.target.move_to((0, 5.5, 0))
        self.play(MoveToTarget(r))

        self.my_code_bubble = MyCodeBubble()
        self.my_code_bubble.next_to(b, DOWN)
        self.my_code_bubble.to_edge(LEFT)
        writes = [Write(x) for x in self.my_code_bubble.b]
        self.play(*writes)

        self.my_code_selection = MyCodeSelection()
        self.my_code_selection.next_to(b, DOWN)
        self.my_code_selection.to_edge(RIGHT)
        writes = [Write(x) for x in self.my_code_selection.b]
        self.play(*writes)

        self.play(FadeOut(b))

        g1 = VGroup(self.my_code_bubble.codes[3], self.my_code_bubble.codes[4], self.my_code_bubble.codes[5])
        h1 = SurroundingRectangle(g1, color=GREEN)
        self.play(Write(h1))
        s1 = TextMobject("$O(n^2)$ swaps", color=RED)
        s1.next_to(h1, DOWN)
        self.play(Write(s1))
        self.wait(18)

        g2 = VGroup(self.my_code_selection.codes[7], self.my_code_selection.codes[8], self.my_code_selection.codes[9])
        h2 = SurroundingRectangle(g2, color=GREEN)
        self.play(Write(h2))
        s2 = TextMobject("$O(n)$ swaps", color=RED)
        s2.next_to(h2, UP)
        self.play(Write(s2))
        self.wait(8)

        swap1 = TextMobject("Swaps are heavy:", color=BLUE)
        swap2 = TextMobject("3 instructions", color=BLUE)
        swap = VGroup(swap1, swap2).arrange(DOWN)
        swap.next_to(s1, DOWN, buff=8*SMALL_BUFF)
        rswap = SurroundingRectangle(swap, color=BLUE)
        self.play(Write(rswap))
        self.play(Write(swap1))
        self.play(Write(swap2))
        self.wait(26)

class Nature(Scene):
    def construct(self):
        r1 = ImageMobject('Petals.png').scale(3)
        r1.to_edge(LEFT)
        r2 = ImageMobject('Snail.jpg').scale(2)
        r2.to_edge(RIGHT + TOP)
        self.play(FadeIn(r1))
        self.play(FadeIn(r2))
        
        t1 = TextMobject("Nature is usually optimal", color=BLUE).scale(0.9)
        t2 = TextMobject("Bubble sort is inspired by nature", color=BLUE).scale(0.9)
        t3 = TextMobject("Then why is it slow?", color=BLUE).scale(0.9)
        t = VGroup(t1, t2, t3).arrange(DOWN)
        t.next_to(r2, DOWN)
        self.play(Write(t))
        self.wait(19)

class Improvement(Scene):
    def construct(self):
        self.my_code_bubble = MyCodeBubble()
        self.my_code_bubble.to_edge(LEFT)
        writes = [Write(x) for x in self.my_code_bubble.b]
        self.play(*writes)

        self.my_code_improved_bubble = MyCodeImprovedBubble()
        self.my_code_improved_bubble.to_edge(RIGHT)
        writes = [Write(x) for x in self.my_code_improved_bubble.b]
        self.play(*writes)

        self.wait(2)
        g1 = VGroup(self.my_code_improved_bubble.codes[1])
        r1 = SurroundingRectangle(g1)
        self.play(Write(r1))

        g2 = VGroup(self.my_code_improved_bubble.codes[7])
        r2 = SurroundingRectangle(g2)
        self.play(Write(r2))

        g3 = VGroup(*self.my_code_improved_bubble.codes[10:13])
        r3 = SurroundingRectangle(g3)
        self.play(Write(r3))
        self.wait(24)

class Manindra(Scene):
    def construct(self):
        r1 = ImageMobject('Manindra_Agarwal.jpg').scale(2)
        self.play(FadeIn(r1))
        t1 = TextMobject("Manindra Agarwal should never see", color=YELLOW)
        t2 = TextMobject("a file called BubbleSort.java!", color=YELLOW)
        t1.next_to(r1, DOWN)
        t2.next_to(t1, DOWN)
        self.play(Write(t1))
        self.play(Write(t2))
