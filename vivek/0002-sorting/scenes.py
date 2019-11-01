from manimlib.imports import *
import numpy as np

class Scene1(Scene):
    def construct(self):
        text = TextMobject("Computer Science by Pandey")

        subtext = TextMobject("One video: One snack sized topic")
        VGroup(text, subtext).arrange(DOWN)
        self.play(Write(text))
        self.wait(5)
        self.play(Write(subtext))
        self.wait(15)
        self.play(FadeOut(text), FadeOut(subtext))
        
class Scene2(Scene):
    def construct(self):
        text = TextMobject("Sorting $n$ numbers takes at least $\\theta(n\\log{}n)$ time")
        self.play(Write(text))
        self.wait(20)

class Scene3(Scene):
    def construct(self):
        text = TextMobject("Previous video: information theoretic approach")
        self.play(Write(text))
        self.wait(10)
        self.play(FadeOut(text))
        self.wait(10)

class Scene5(Scene):
    def construct(self):
        text = TextMobject("This video: algorithmic approach")
        self.play(Write(text))
        self.wait(20)
        self.play(FadeOut(text))
        self.wait()

class Scene6(Scene):
    def construct(self):
        xnum23 = TextMobject("23")
        xnum28 = TextMobject("28")
        xnum14 = TextMobject("14")
        xnum33 = TextMobject("33")
        xnum18 = TextMobject("18")
        xnum20 = TextMobject("20")
        xnum21 = TextMobject("21")
        xnum25 = TextMobject("25")
        VGroup(xnum23, xnum28, xnum14, xnum33, xnum18, xnum20, xnum21, xnum25).arrange(RIGHT)

        num23 = TextMobject("23")
        num28 = TextMobject("28")
        num14 = TextMobject("14")
        num33 = TextMobject("33")
        num18 = TextMobject("18")
        num20 = TextMobject("20")
        num21 = TextMobject("21")
        num25 = TextMobject("25")
        VGroup(num23, num28, num14, num33, num18, num20, num21, num25).arrange(RIGHT)
        self.play(
                  Write(num23), 
                  Write(num28), 
                  Write(num14), 
                  Write(num33),
                  Write(num18), 
                  Write(num20), 
                  Write(num21), 
                  Write(num25),
                  Write(xnum23), 
                  Write(xnum28), 
                  Write(xnum14), 
                  Write(xnum33),
                  Write(xnum18), 
                  Write(xnum20), 
                  Write(xnum21), 
                  Write(xnum25)
        )
        self.wait(7)

        num14.generate_target()
        num18.generate_target()
        num20.generate_target()
        num21.generate_target()
        num23.generate_target()
        num25.generate_target()
        num28.generate_target()
        num33.generate_target()
        
        num14.target.next_to(num23, DOWN)
        num18.target.next_to(num28, DOWN)
        num20.target.next_to(num14, DOWN)
        num21.target.next_to(num33, DOWN)
        num23.target.next_to(num18, DOWN)
        num25.target.next_to(num20, DOWN)
        num28.target.next_to(num21, DOWN)
        num33.target.next_to(num25, DOWN)
        
        self.play(MoveToTarget(num14), 
                  MoveToTarget(num18),
                  MoveToTarget(num20),
                  MoveToTarget(num21),
                  MoveToTarget(num23),
                  MoveToTarget(num25),
                  MoveToTarget(num28),
                  MoveToTarget(num33)
                 )
        self.wait(2)

        self.play( 
                  FadeOut(num14),
                  FadeOut(num18),
                  FadeOut(num20),
                  FadeOut(num21),
                  FadeOut(num23),
                  FadeOut(num25),
                  FadeOut(num28),
                  FadeOut(num33),
                  FadeOut(xnum14),
                  FadeOut(xnum18),
                  FadeOut(xnum20),
                  FadeOut(xnum21),
                  FadeOut(xnum23),
                  FadeOut(xnum25),
                  FadeOut(xnum28),
                  FadeOut(xnum33)
        )
        self.wait(2)

class Scene8(Scene):
    def construct(self):
        text = TextMobject("What is a decision tree?")
        text.to_corner(UP)
        root = Ellipse()
        root.next_to(text, DOWN)

        child1 = Ellipse()
        child1.next_to(root, 6 * DOWN + LEFT)

        child2 = Ellipse()
        child2.next_to(root, 6 * DOWN + RIGHT)

        child11 = Ellipse()
        child11.next_to(child1, 6 * DOWN + LEFT)
       
        child12 = Ellipse()
        child12.next_to(child1, 6 * DOWN )
       
        child21 = Ellipse()
        child21.next_to(child2, 6 * DOWN)
       
        child22 = Ellipse()
        child22.next_to(child2, 6 * DOWN + RIGHT)

        arrow1 = Arrow(root.get_bottom(), child1.get_top())
        arrow1.scale(0.8)
       
        arrow2 = Arrow(root.get_bottom(), child2.get_top())
        arrow2.scale(0.8)

        arrow11 = Arrow(child1.get_bottom(), child11.get_top())
        arrow11.scale(0.8)

        arrow12 = Arrow(child1.get_bottom(), child12.get_top())
        arrow12.scale(0.8)

        arrow21 = Arrow(child2.get_bottom(), child21.get_top())
        arrow21.scale(0.8)

        arrow22 = Arrow(child2.get_bottom(), child22.get_top())
        arrow22.scale(0.8)

        #self.play(Write(text), Write(root), Write(child1), Write(child2),
        #          Write(child11), Write(child12), Write(child21), Write(child22),
        #          Write(root_text), Write(arrow1), Write(arrow2),
        #          Write(arrow11), Write(arrow12), Write(arrow21), Write(arrow22),
        #          Write(arrow1_text), Write(arrow2_text),
        #          Write(arrow11_text), Write(arrow12_text),
        #          Write(arrow21_text), Write(arrow22_text),
        #          Write(child1_text), Write(child2_text)
        #         )
        self.play(Write(text), Write(root))
        self.wait()

        self.play(Write(arrow1), Write(child1))
        self.wait()

        self.play(Write(arrow11), Write(arrow12),
                  Write(child11), Write(child12)
                 )
        self.wait()

        self.play(Write(arrow2), Write(child2))
        self.wait()

        self.play(Write(arrow21), Write(arrow22),
                  Write(child21), Write(child22)
                 )
        self.wait(20)

class Scene9(Scene):
    def construct(self):
        text = TextMobject("Should I go on a trip?")
        text.to_corner(UP)
        root = Ellipse()
        root.next_to(text, DOWN)
        root_text = TextMobject("Is it a holiday?")
        root_text.scale(0.8)
        root_text.next_to(root, RIGHT)

        child1 = Ellipse()
        child1.next_to(root, 6 * DOWN + LEFT)
        child1_text = TextMobject("Pleasant weather?")
        child1_text.scale(0.8)
        child1_text.next_to(child1, LEFT)

        child2 = Ellipse()
        child2.next_to(root, 6 * DOWN + RIGHT)
        child2_text = TextMobject("Vacations left?")
        child2_text.scale(0.8)
        child2_text.next_to(child2, RIGHT)

        child11 = TextMobject("GO!")
        child11.next_to(child1, 6 * DOWN + LEFT)
       
        child12 = TextMobject("DON'T")
        child12.next_to(child1, 6 * DOWN )
       
        child21 = TextMobject("GO!")
        child21.next_to(child2, 6 * DOWN)
       
        child22 = TextMobject("DON'T")
        child22.next_to(child2, 6 * DOWN + RIGHT)

        arrow1 = Arrow(root.get_bottom(), child1.get_top())
        arrow1.scale(0.8)
        arrow1_text = TextMobject("Yes")
        arrow1_text.next_to(arrow1, LEFT)
        arrow1_text.scale(0.7)
       
        arrow2 = Arrow(root.get_bottom(), child2.get_top())
        arrow2.scale(0.8)
        arrow2_text = TextMobject("No")
        arrow2_text.next_to(arrow2, RIGHT)
        arrow2_text.scale(0.7)

        arrow11 = Arrow(child1.get_bottom(), child11.get_top())
        arrow11.scale(0.8)
        arrow11_text = TextMobject("Yes")
        arrow11_text.next_to(arrow11, LEFT)
        arrow11_text.scale(0.7)

        arrow12 = Arrow(child1.get_bottom(), child12.get_top())
        arrow12.scale(0.8)
        arrow12_text = TextMobject("No")
        arrow12_text.next_to(arrow12, RIGHT)
        arrow12_text.scale(0.7)

        arrow21 = Arrow(child2.get_bottom(), child21.get_top())
        arrow21.scale(0.8)
        arrow21_text = TextMobject("Yes")
        arrow21_text.next_to(arrow21, LEFT)
        arrow21_text.scale(0.7)

        arrow22 = Arrow(child2.get_bottom(), child22.get_top())
        arrow22.scale(0.8)
        arrow22_text = TextMobject("No")
        arrow22_text.next_to(arrow22, RIGHT)
        arrow22_text.scale(0.7)

        #self.play(Write(text), Write(root), Write(child1), Write(child2),
        #          Write(child11), Write(child12), Write(child21), Write(child22),
        #          Write(root_text), Write(arrow1), Write(arrow2),
        #          Write(arrow11), Write(arrow12), Write(arrow21), Write(arrow22),
        #          Write(arrow1_text), Write(arrow2_text),
        #          Write(arrow11_text), Write(arrow12_text),
        #          Write(arrow21_text), Write(arrow22_text),
        #          Write(child1_text), Write(child2_text)
        #         )
        self.play(Write(text))
        self.wait(8)

        self.play(Write(root_text), Write(root))
        self.wait(2)

        self.play(Write(arrow1), Write(child1), Write(arrow1_text))
        self.wait(1)

        self.play(Write(child1_text))
        self.wait(3)

        self.play(Write(arrow11), Write(arrow12),
                  Write(arrow11_text), Write(arrow12_text),
                  Write(child11), Write(child12)
                 )
        self.wait(7)

        self.play(Write(arrow2), Write(child2), Write(child2_text))
        self.wait(14)

        self.play(Write(arrow21), Write(arrow22),
                  Write(arrow21_text), Write(arrow22_text),
                  Write(child21), Write(child22)
                 )
        self.wait(60)

class Scene10(Scene):
    def construct(self):
        text1 = TextMobject("A sorting algorithm")
        text2 = TextMobject("$\equiv$")
        text3 = TextMobject("A decision tree")
        VGroup(text1, text2, text3).arrange(DOWN)
        self.play(Write(text1), Write(text2), Write(text3))
        self.wait(30)

class SortingTree(VGroup):
    def __init__(self, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.text = TextMobject("$a_1$ $a_2$ $a_3$")
        self.text.to_corner(UP)

        self.root = Ellipse()
        self.root.scale(0.8)
        self.root.next_to(self.text, DOWN)
        self.root_text = TextMobject("$a_1$ $<$ $a_2?$")
        self.root_text.scale(0.6)
        self.root_text.next_to(self.text, 2 * DOWN)

        self.child1 = Ellipse()
        self.child1.scale(0.8)
        self.child1.next_to(self.root, 6 * DOWN + LEFT)
        self.child1_text = TextMobject("$a_2$ $<$ $a_3?$")
        self.child1_text.scale(0.6)
        self.child1_text.next_to(self.root, 7 * DOWN + 2 * LEFT)

        self.child2 = Ellipse()
        self.child2.scale(0.8)
        self.child2.next_to(self.root, 6 * DOWN + RIGHT)
        self.child2_text = TextMobject("$a_2$ $<$ $a_3?$")
        self.child2_text.scale(0.6)
        self.child2_text.next_to(self.root, 7 * DOWN + 2 * RIGHT)

        self.child11 = TextMobject("$a_1$, $a_2$, $a_3$")
        self.child11.scale(0.8)
        self.child11.next_to(self.child1, 6 * DOWN + LEFT)
       
        self.child12 = Ellipse()
        self.child12.scale(0.8)
        self.child12.next_to(self.child1, 6 * DOWN )
        self.child12_text = TextMobject("$a_1$ $<$ $a_3?$")
        self.child12_text.scale(0.6)
        self.child12_text.next_to(self.child1, 7 * DOWN)

        self.child21 = Ellipse()
        self.child21.scale(0.8)
        self.child21.next_to(self.child2, 6 * DOWN)
        self.child21_text = TextMobject("$a_1$ $<$ $a_3?$")
        self.child21_text.scale(0.6)
        self.child21_text.next_to(self.child2, 7 * DOWN)

        self.child22 = TextMobject("$a_3$, $a_2$, $a_1$")
        self.child22.scale(0.8)
        self.child22.next_to(self.child2, 6 * DOWN + RIGHT)

        self.child121 = TextMobject("$a_1$, $a_3$, $a_2$")
        self.child121.scale(0.8)
        self.child121.next_to(self.child12, 4 * DOWN + LEFT)

        self.child122 = TextMobject("$a_3$, $a_1$, $a_2$")
        self.child122.scale(0.8)
        self.child122.next_to(self.child12, 4 * DOWN)

        self.child211 = TextMobject("$a_2$, $a_1$, $a_3$")
        self.child211.scale(0.8)
        self.child211.next_to(self.child21, 4 * DOWN)
                
        self.child212 = TextMobject("$a_2$, $a_3$, $a_1$")
        self.child212.scale(0.8)
        self.child212.next_to(self.child21, 4 * DOWN + RIGHT)

        self.arrow1 = Arrow(self.root.get_bottom(), self.child1.get_top())
        self.arrow1.scale(0.8)
        self.arrow1_text = TextMobject("Yes")
        self.arrow1_text.next_to(self.arrow1, LEFT)
        self.arrow1_text.scale(0.7)
       
        self.arrow2 = Arrow(self.root.get_bottom(), self.child2.get_top())
        self.arrow2.scale(0.8)
        self.arrow2_text = TextMobject("No")
        self.arrow2_text.next_to(self.arrow2, RIGHT)
        self.arrow2_text.scale(0.7)

        self.arrow11 = Arrow(self.child1.get_bottom(), self.child11.get_top())
        self.arrow11.scale(0.8)
        self.arrow11_text = TextMobject("Yes")
        self.arrow11_text.next_to(self.arrow11, LEFT)
        self.arrow11_text.scale(0.7)

        self.arrow12 = Arrow(self.child1.get_bottom(), self.child12.get_top())
        self.arrow12.scale(0.8)
        self.arrow12_text = TextMobject("No")
        self.arrow12_text.next_to(self.arrow12, RIGHT)
        self.arrow12_text.scale(0.7)

        self.arrow21 = Arrow(self.child2.get_bottom(), self.child21.get_top())
        self.arrow21.scale(0.8)
        self.arrow21_text = TextMobject("Yes")
        self.arrow21_text.next_to(self.arrow21, LEFT)
        self.arrow21_text.scale(0.7)

        self.arrow22 = Arrow(self.child2.get_bottom(), self.child22.get_top())
        self.arrow22.scale(0.8)
        self.arrow22_text = TextMobject("No")
        self.arrow22_text.next_to(self.arrow22, RIGHT)
        self.arrow22_text.scale(0.7)

        self.arrow121 = Arrow(self.child12.get_bottom(), self.child121.get_top())
        self.arrow121.scale(0.8)
        self.arrow121_text = TextMobject("Yes")
        self.arrow121_text.next_to(self.arrow121, LEFT)
        self.arrow121_text.scale(0.7)

        self.arrow122 = Arrow(self.child12.get_bottom(), self.child122.get_top())
        self.arrow122.scale(0.8)
        self.arrow122_text = TextMobject("No")
        self.arrow122_text.next_to(self.arrow122, RIGHT)
        self.arrow122_text.scale(0.7)

        self.arrow211 = Arrow(self.child21.get_bottom(), self.child211.get_top())
        self.arrow211.scale(0.8)
        self.arrow211_text = TextMobject("Yes")
        self.arrow211_text.next_to(self.arrow211, LEFT)
        self.arrow211_text.scale(0.7)

        self.arrow212 = Arrow(self.child21.get_bottom(), self.child212.get_top())
        self.arrow212.scale(0.8)
        self.arrow212_text = TextMobject("No")
        self.arrow212_text.next_to(self.arrow212, RIGHT)
        self.arrow212_text.scale(0.7)

        self.rect11 = SurroundingRectangle(self.child11)
        self.rect22 = SurroundingRectangle(self.child22)
        self.rect121 = SurroundingRectangle(self.child121)
        self.rect122 = SurroundingRectangle(self.child122)
        self.rect211 = SurroundingRectangle(self.child211)
        self.rect212 = SurroundingRectangle(self.child212)

class SortingTree2(VGroup):
    def __init__(self, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.text = TextMobject("$a_1$ $a_2$ $a_3$")
        self.text.to_corner(UP)

        self.root = Ellipse()
        self.root.scale(0.8)
        self.root.next_to(self.text, DOWN)
        self.root_text = TextMobject("$a_1$ $<$ $a_3?$")
        self.root_text.scale(0.6)
        self.root_text.next_to(self.text, 2 * DOWN)

        self.child1 = Ellipse()
        self.child1.scale(0.8)
        self.child1.next_to(self.root, 6 * DOWN + LEFT)
        self.child1_text = TextMobject("$a_1$ $<$ $a_2?$")
        self.child1_text.scale(0.6)
        self.child1_text.next_to(self.root, 7 * DOWN + 2 * LEFT)

        self.child2 = Ellipse()
        self.child2.scale(0.8)
        self.child2.next_to(self.root, 6 * DOWN + RIGHT)
        self.child2_text = TextMobject("$a_2$ $<$ $a_3?$")
        self.child2_text.scale(0.6)
        self.child2_text.next_to(self.root, 7 * DOWN + 2 * RIGHT)

        self.child11 = Ellipse()
        self.child11.scale(0.8)
        self.child11.next_to(self.child1, 6 * DOWN + LEFT)
        self.child11_text = TextMobject("$a_1$ $<$ $a_3?$")
        self.child11_text.scale(0.6)
        self.child11_text.next_to(self.child1, 7 * DOWN + 2 * LEFT)
       
        self.child111 = TextMobject("$a_1$, $a_2$, $a_3$")
        self.child111.scale(0.8)
        self.child111.next_to(self.child11, 4 * DOWN + LEFT)

        self.child112 = TextMobject("$a_1$, $a_3$, $a_2$")
        self.child112.scale(0.8)
        self.child112.next_to(self.child11, 4 * DOWN + RIGHT)

        self.child12 = TextMobject("$a_2$, $a_1$, $a_3$")
        self.child12.scale(0.8)
        self.child12.next_to(self.child1, 7 * DOWN)

        self.child21 = TextMobject("$a_2$, $a_3$, $a_1$")
        self.child21.scale(0.8)
        self.child21.next_to(self.child2, 7 * DOWN)

        self.child22 = Ellipse()
        self.child22.scale(0.8)
        self.child22.next_to(self.child2, 6 * DOWN + RIGHT)
        self.child22_text = TextMobject("$a_1$ $<$ $a_2?$")
        self.child22_text.scale(0.6)
        self.child22_text.next_to(self.child2, 7 * DOWN + 2 * RIGHT)

        self.child221 = TextMobject("$a_3$, $a_1$, $a_2$")
        self.child221.scale(0.8)
        self.child221.next_to(self.child22, 4 * DOWN + LEFT)

        self.child222 = TextMobject("$a_3$, $a_2$, $a_1$")
        self.child222.scale(0.8)
        self.child222.next_to(self.child22, 4 * DOWN + RIGHT)

        self.arrow1 = Arrow(self.root.get_bottom(), self.child1.get_top())
        self.arrow1.scale(0.8)
        self.arrow1_text = TextMobject("Yes")
        self.arrow1_text.next_to(self.arrow1, LEFT)
        self.arrow1_text.scale(0.7)
       
        self.arrow2 = Arrow(self.root.get_bottom(), self.child2.get_top())
        self.arrow2.scale(0.8)
        self.arrow2_text = TextMobject("No")
        self.arrow2_text.next_to(self.arrow2, RIGHT)
        self.arrow2_text.scale(0.7)

        self.arrow11 = Arrow(self.child1.get_bottom(), self.child11.get_top())
        self.arrow11.scale(0.8)
        self.arrow11_text = TextMobject("Yes")
        self.arrow11_text.next_to(self.arrow11, LEFT)
        self.arrow11_text.scale(0.7)

        self.arrow12 = Arrow(self.child1.get_bottom(), self.child12.get_top())
        self.arrow12.scale(0.8)
        self.arrow12_text = TextMobject("No")
        self.arrow12_text.next_to(self.arrow12, RIGHT)
        self.arrow12_text.scale(0.7)

        self.arrow21 = Arrow(self.child2.get_bottom(), self.child21.get_top())
        self.arrow21.scale(0.8)
        self.arrow21_text = TextMobject("Yes")
        self.arrow21_text.next_to(self.arrow21, LEFT)
        self.arrow21_text.scale(0.7)

        self.arrow22 = Arrow(self.child2.get_bottom(), self.child22.get_top())
        self.arrow22.scale(0.8)
        self.arrow22_text = TextMobject("No")
        self.arrow22_text.next_to(self.arrow22, RIGHT)
        self.arrow22_text.scale(0.7)

        self.arrow111 = Arrow(self.child11.get_bottom(), self.child111.get_top())
        self.arrow111.scale(0.8)
        self.arrow111_text = TextMobject("Yes")
        self.arrow111_text.next_to(self.arrow111, LEFT)
        self.arrow111_text.scale(0.7)

        self.arrow112 = Arrow(self.child11.get_bottom(), self.child112.get_top())
        self.arrow112.scale(0.8)
        self.arrow112_text = TextMobject("No")
        self.arrow112_text.next_to(self.arrow112, RIGHT)
        self.arrow112_text.scale(0.7)

        self.arrow221 = Arrow(self.child22.get_bottom(), self.child221.get_top())
        self.arrow221.scale(0.8)
        self.arrow221_text = TextMobject("Yes")
        self.arrow221_text.next_to(self.arrow221, LEFT)
        self.arrow221_text.scale(0.7)

        self.arrow222 = Arrow(self.child22.get_bottom(), self.child222.get_top())
        self.arrow222.scale(0.8)
        self.arrow222_text = TextMobject("No")
        self.arrow222_text.next_to(self.arrow222, RIGHT)
        self.arrow222_text.scale(0.7)

        self.rect111 = SurroundingRectangle(self.child111)
        self.rect112 = SurroundingRectangle(self.child112)
        self.rect12 = SurroundingRectangle(self.child12)
        self.rect21 = SurroundingRectangle(self.child21)
        self.rect221 = SurroundingRectangle(self.child221)
        self.rect222 = SurroundingRectangle(self.child222)

        self.label111 = TextMobject("leaf\#1")
        self.label111.next_to(self.child111, UP)
        self.label111.scale(0.6)

        self.label112 = TextMobject("leaf\#2")
        self.label112.next_to(self.child112, LEFT)
        self.label112.scale(0.6)

        self.label12 = TextMobject("leaf\#3")
        self.label12.next_to(self.child12, DOWN)
        self.label12.scale(0.6)

        self.label21 = TextMobject("leaf\#4")
        self.label21.next_to(self.child21, DOWN)
        self.label21.scale(0.6)

        self.label221 = TextMobject("leaf\#5")
        self.label221.next_to(self.child221, LEFT)
        self.label221.scale(0.6)

        self.label222 = TextMobject("leaf\#6")
        self.label222.next_to(self.child222, LEFT)
        self.label222.scale(0.6)

        self.final_text1 = TextMobject("Number of leaves")
        self.final_text2 = TextMobject("$= 3!$")
        self.final_text3 = TextMobject("$= 6$")
        VGroup(self.final_text1, self.final_text2, self.final_text3).arrange(DOWN).to_corner(UP + RIGHT)

class TreeScene(Scene):
    def setup(self):
        self.st = SortingTree()
        self.st_more = SortingTree2()
        self.add(self.st)
        self.add(self.st_more)
    
class Scene11(TreeScene):
    def construct(self):
        st = self.st
 
        self.play(Write(st.text))
        self.wait(8)

        self.play(Write(st.root), Write(st.root_text))
        self.wait(8)

        self.play(Write(st.arrow1), Write(st.arrow1_text), 
                  Write(st.child1_text), Write(st.child1))
        self.wait(5)

        self.play(Write(st.child11), Write(st.arrow11), Write(st.arrow11_text), Write(st.rect11))
        self.wait(6)

        self.play(Write(st.child12), Write(st.arrow12), Write(st.arrow12_text), Write(st.child12_text))
        self.wait(5)

        self.play(Write(st.child121), Write(st.rect121), Write(st.child122), Write(st.rect122), Write(st.arrow121), Write(st.arrow122), Write(st.arrow121_text), Write(st.arrow122_text))
        self.wait(11)

        self.play(Write(st.child2), Write(st.child2_text), Write(st.arrow2), Write(st.arrow2_text))
        self.wait(2)

        self.play(Write(st.child21), Write(st.child21_text), Write(st.arrow21), Write(st.arrow21_text))
        self.wait(1)

        self.play(Write(st.child212), Write(st.rect212), Write(st.child211), Write(st.rect211), Write(st.arrow211), Write(st.arrow211_text), Write(st.arrow212), Write(st.arrow212_text))
        self.wait(1)

        self.play(Write(st.arrow22), Write(st.arrow22_text), Write(st.child22), Write(st.rect22))
        self.wait(40)

class Scene12(TreeScene):
    def construct(self):
        st = self.st
        st_more = self.st_more
        st.add(st.text, st.root,
               st.child1, st.child2,
               st.child11, st.child12, st.child21, st.child22,
               st.child12_text, st.child21_text,
               st.root_text, st.arrow1, st.arrow2,
               st.arrow11, st.arrow12, st.arrow21, st.arrow22,
               st.arrow1_text, st.arrow2_text,
               st.arrow11_text, st.arrow12_text,
               st.arrow21_text, st.arrow22_text,
               st.child1_text, st.child2_text,
               st.child121, st.child122,
               st.child211, st.child212,
               st.arrow121, st.arrow122,
               st.arrow121_text, st.arrow122_text,
               st.arrow211, st.arrow212,
               st.arrow211_text, st.arrow212_text,
               st.rect11, st.rect22,
               st.rect121, st.rect122,
               st.rect211, st.rect212
                 )


        VGroup(st, st_more).arrange(LEFT)

        text = TextMobject("Sorting Algorithm 1")
        text.to_edge(UP)
        self.play(st.scale, 0.8, st.to_edge, DOWN,)
        self.play(Write(text))

        self.wait(2)

        self.play(ApplyMethod(VGroup(st, text).shift, FRAME_X_RADIUS * RIGHT * 1.5, rate_func = running_start))

        st_more.add(
                  st_more.text,
                  st_more.root, 
                  st_more.root_text,
                  st_more.arrow1, 
                  st_more.arrow1_text, 
                  st_more.child1,
                  st_more.child1_text, 
                  st_more.child11, 
                  st_more.child11_text, 
                  st_more.arrow11, 
                  st_more.arrow11_text, 
                  st_more.rect12,
                  st_more.child12, 
                  st_more.arrow12, 
                  st_more.arrow12_text, 
                  st_more.child111, 
                  st_more.rect111, 
                  st_more.child112, 
                  st_more.rect112, 
                  st_more.arrow111, 
                  st_more.arrow112, 
                  st_more.arrow111_text, 
                  st_more.arrow112_text,
                  st_more.child2, 
                  st_more.child2_text, 
                  st_more.arrow2, 
                  st_more.arrow2_text,
                  st_more.child21, 
                  st_more.arrow21, 
                  st_more.arrow21_text,
                  st_more.child221, 
                  st_more.rect21, 
                  st_more.child222, 
                  st_more.rect222, 
                  st_more.arrow221, 
                  st_more.arrow221_text, 
                  st_more.arrow222, 
                  st_more.arrow222_text,
                  st_more.arrow22, 
                  st_more.arrow22_text, 
                  st_more.child22, 
                  st_more.child22_text, 
                  st_more.rect221
        )

        self.play(Write(st_more.text),
                  Write(st_more.root), 
                  Write(st_more.root_text),
                  Write(st_more.arrow1), 
                  Write(st_more.arrow1_text), 
                  Write(st_more.child1),
                  Write(st_more.child1_text), 
                  Write(st_more.child11), 
                  Write(st_more.child11_text), 
                  Write(st_more.arrow11), 
                  Write(st_more.arrow11_text), 
                  Write(st_more.rect12),
                  Write(st_more.child12), 
                  Write(st_more.arrow12), 
                  Write(st_more.arrow12_text), 
                  Write(st_more.child111), 
                  Write(st_more.rect111), 
                  Write(st_more.child112), 
                  Write(st_more.rect112), 
                  Write(st_more.arrow111), 
                  Write(st_more.arrow112), 
                  Write(st_more.arrow111_text), 
                  Write(st_more.arrow112_text),
                  Write(st_more.child2), 
                  Write(st_more.child2_text), 
                  Write(st_more.arrow2), 
                  Write(st_more.arrow2_text),
                  Write(st_more.child21), 
                  Write(st_more.arrow21), 
                  Write(st_more.arrow21_text),
                  Write(st_more.child221), 
                  Write(st_more.rect21), 
                  Write(st_more.child222), 
                  Write(st_more.rect222), 
                  Write(st_more.arrow221), 
                  Write(st_more.arrow221_text), 
                  Write(st_more.arrow222), 
                  Write(st_more.arrow222_text),
                  Write(st_more.arrow22), 
                  Write(st_more.arrow22_text), 
                  Write(st_more.child22), 
                  Write(st_more.child22_text), 
                  Write(st_more.rect221)
        )
        self.play(st_more.scale, 0.8, st_more.to_edge, DOWN,)

        text_more = TextMobject("Sorting Algorithm 2")
        text_more.to_edge(UP)
        self.play(Write(text_more))

        self.wait(16)
        st_more.circle1_text = TextMobject("1")
        st_more.circle1_text.next_to(st_more.root, LEFT)
        st_more.circle1_text.scale(0.8)
        st_more.circle1_text.set_color(WHITE)
        self.play(Write(st_more.circle1_text))

        st_more.circle2_text = TextMobject("2")
        st_more.circle2_text.next_to(st_more.child1, LEFT)
        st_more.circle2_text.scale(0.8)
        st_more.circle2_text.set_color(WHITE)
        self.play(Write(st_more.circle2_text))

        st_more.circle3_text = TextMobject("3")
        st_more.circle3_text.next_to(st_more.child11, LEFT)
        st_more.circle3_text.scale(0.8)
        st_more.circle3_text.set_color(WHITE)
        self.play(Write(st_more.circle3_text))
        self.wait(40)

class Scene13(Scene):
    def construct(self):
        root = Ellipse()
        root.scale(0.5)
        root.to_corner(UP)

        child1 = Ellipse()
        child1.scale(0.5)
        child1.next_to(root, 4 * DOWN + LEFT)

        child2 = Ellipse()
        child2.scale(0.5)
        child2.next_to(root, 4 * DOWN + RIGHT)

        child11 = Ellipse()
        child11.scale(0.5)
        child11.next_to(child1, 4 * DOWN + LEFT)

        child12 = Ellipse()
        child12.scale(0.5)
        child12.next_to(child1, 4 * DOWN + RIGHT)

        child22 = Ellipse()
        child22.scale(0.5)
        child22.next_to(child2, 4 * DOWN + RIGHT)

        child121 = Ellipse()
        child121.scale(0.5)
        child121.next_to(child12, 4 * DOWN + LEFT)

        child122 = Ellipse()
        child122.scale(0.5)
        child122.next_to(child12, 4 * DOWN + RIGHT)

        child1211 = Ellipse()
        child1211.scale(0.5)
        child1211.next_to(child121, 4 * DOWN + LEFT)

        child1212 = Ellipse()
        child1212.scale(0.5)
        child1212.next_to(child121, 4 * DOWN + RIGHT)

        arrow1 = Arrow(root.get_bottom(), child1.get_top())
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

        circle1_text = TextMobject("1")
        circle1_text.next_to(root, LEFT)
        circle1_text.scale(0.8)
        circle1_text.set_color(WHITE)

        circle2_text = TextMobject("2")
        circle2_text.next_to(child1, LEFT)
        circle2_text.scale(0.8)
        circle2_text.set_color(WHITE)

        circle3_text = TextMobject("3")
        circle3_text.next_to(child12, LEFT)
        circle3_text.scale(0.8)
        circle3_text.set_color(WHITE)

        circle4_text = TextMobject("4")
        circle4_text.next_to(child121, LEFT)
        circle4_text.scale(0.8)
        circle4_text.set_color(WHITE)

        circle5_text = TextMobject("5")
        circle5_text.next_to(child1211, LEFT)
        circle5_text.scale(0.8)
        circle5_text.set_color(WHITE)

        depth_text = TextMobject("depth = 5")
        depth_text.next_to(child1212, DOWN)

        self.play(Write(root), 
                 Write(child1),
                 Write(child2),
                 Write(child11),
                 Write(child12),
                 Write(child22),
                 Write(child121),
                 Write(child122),
                 Write(child1211),
                 Write(child1212),
                 Write(arrow1),
                 Write(arrow2),
                 Write(arrow11),
                 Write(arrow12),
                 Write(arrow22),
                 Write(arrow121),
                 Write(arrow122),
                 Write(arrow1211),
                 Write(arrow1212),
              )
        self.wait(6)
        self.play(Write(circle1_text))
        self.play(Write(circle2_text))
        self.play(Write(circle3_text))
        self.play(Write(circle4_text))
        self.play(Write(circle5_text))

        self.play(Write(depth_text))
        self.wait(60)

class Scene14(Scene):
    def construct(self):
        text1 = TextMobject("Number of leaf nodes in decision tree for sorting")
        text2 = TextMobject("$\ge$")
        text3 = TextMobject("$n!$")
        text4 = TextMobject("(Since all $n!$ permutations must appear as leaves)")

        VGroup(text1, text2, text3, text4).arrange(DOWN)
        self.play(Write(text1))
        self.play(Write(text2))
        self.play(Write(text3))
        self.wait(1)
        self.play(Write(text4))
        self.wait(60)

class Scene15(TreeScene):
    def construct(self):
        st_more = self.st_more
        st_more.add(
                  st_more.text,
                  st_more.root, 
                  st_more.root_text,
                  st_more.arrow1, 
                  st_more.child1,
                  st_more.child1_text, 
                  st_more.child11, 
                  st_more.child11_text, 
                  st_more.arrow11, 
                  st_more.rect12,
                  st_more.child12, 
                  st_more.arrow12, 
                  st_more.child111, 
                  st_more.rect111, 
                  st_more.child112, 
                  st_more.rect112, 
                  st_more.arrow111, 
                  st_more.arrow112, 
                  st_more.child2, 
                  st_more.child2_text, 
                  st_more.arrow2, 
                  st_more.child21, 
                  st_more.arrow21, 
                  st_more.child221, 
                  st_more.rect21, 
                  st_more.child222, 
                  st_more.rect222, 
                  st_more.arrow221, 
                  st_more.arrow222, 
                  st_more.arrow22, 
                  st_more.child22, 
                  st_more.child22_text, 
                  st_more.rect221,
        )

        self.play(Write(st_more.text),
                  Write(st_more.root), 
                  Write(st_more.root_text),
                  Write(st_more.arrow1), 
                  Write(st_more.child1),
                  Write(st_more.child1_text), 
                  Write(st_more.child11), 
                  Write(st_more.child11_text), 
                  Write(st_more.arrow11), 
                  Write(st_more.rect12),
                  Write(st_more.child12), 
                  Write(st_more.arrow12), 
                  Write(st_more.child111), 
                  Write(st_more.rect111), 
                  Write(st_more.child112), 
                  Write(st_more.rect112), 
                  Write(st_more.arrow111), 
                  Write(st_more.arrow112), 
                  Write(st_more.child2), 
                  Write(st_more.child2_text), 
                  Write(st_more.arrow2), 
                  Write(st_more.child21), 
                  Write(st_more.arrow21), 
                  Write(st_more.child221), 
                  Write(st_more.rect21), 
                  Write(st_more.child222), 
                  Write(st_more.rect222), 
                  Write(st_more.arrow221), 
                  Write(st_more.arrow222), 
                  Write(st_more.arrow22), 
                  Write(st_more.child22), 
                  Write(st_more.child22_text), 
                  Write(st_more.rect221),
        )
        self.wait(2)
        self.play(
                  Write(st_more.label111),
                  Write(st_more.label112),
                  Write(st_more.label12),
                  Write(st_more.label21),
                  Write(st_more.label221),
                  Write(st_more.label222),
        )
        self.wait(2)
        self.play(
                  Write(st_more.final_text1),
                  Write(st_more.final_text2),
                  Write(st_more.final_text3)
        )
        self.wait(60)

class Scene16(Scene):
    def construct(self):
        text1 = TextMobject("Given a tree with $n!$ leaves")
        text2 = TextMobject("What can we say about the depth of the tree?")
        text3 = TextMobject("More the number of leaves, more should be depth")
        VGroup(text1, text2, text3). arrange(DOWN)
        self.play(Write(text1))
        self.play(Write(text2))
        self.wait(4)
        self.play(Write(text3))
        self.wait(61)

class Scene17(Scene):
    def construct(self):
        text1 = TextMobject("A tree with $n!$ leaves will have depth")
        text2 = TextMobject("$\\Omega(n\\log{}n)$")
        text2a = TextMobject("(At least $n\\log{}n$)")
        text3 = TextMobject("Thus")
        text4 = TextMobject("Running time will be at least $\\theta(n\\log{}n)$")
        VGroup(text1, text2, text2a, text3, text4). arrange(DOWN)
        self.play(Write(text1))
        self.play(Write(text2))
        self.play(Write(text2a))
        self.wait(38)
        self.play(Write(text3))
        self.play(Write(text4))
        self.wait(7)

        text5 = TextMobject("Proof link in description")
        text5.to_corner(UP + RIGHT)
        arrow = Arrow(text1.get_top(), text5.get_bottom())
        self.play(Write(text5), Write(arrow))
        self.wait(60)

class Scene18(Scene):
    def construct(self):
        root = Ellipse()
        root.scale(0.5)
        root.to_corner(UP)

        child1 = Ellipse()
        child1.scale(0.5)
        child1.next_to(root, 4 * DOWN + LEFT)

        child2 = Ellipse()
        child2.scale(0.5)
        child2.next_to(root, 4 * DOWN + RIGHT)

        child11 = Ellipse()
        child11.scale(0.5)
        child11.next_to(child1, 4 * DOWN + LEFT)

        child12 = Ellipse()
        child12.scale(0.5)
        child12.next_to(child1, 4 * DOWN + RIGHT)

        child22 = Ellipse()
        child22.scale(0.5)
        child22.next_to(child2, 4 * DOWN + RIGHT)

        child121 = Ellipse()
        child121.scale(0.5)
        child121.next_to(child12, 4 * DOWN + LEFT)

        child122 = Ellipse()
        child122.scale(0.5)
        child122.next_to(child12, 4 * DOWN + RIGHT)

        child1211 = Ellipse()
        child1211.scale(0.5)
        child1211.next_to(child121, 4 * DOWN + LEFT)

        child1212 = Ellipse()
        child1212.scale(0.5)
        child1212.next_to(child121, 4 * DOWN + RIGHT)

        arrow1 = Arrow(root.get_bottom(), child1.get_top())
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

        text1 = TextMobject("A sorting algo")
        text1.next_to(child22, RIGHT)
        text1.scale(0.8)

        text2 = TextMobject("$\equiv$ decision tree")
        text2.next_to(text1, DOWN)
        text2.scale(0.8)

        text3 = TextMobject("Tree must have $n!$ leaves")
        text3.next_to(text2, 2 * DOWN)
        text3.scale(0.8)

        text4 = TextMobject("Its depth is $\\Omega(n\\log{}n)$")
        text4.next_to(text3, 2 * DOWN)
        text4.scale(0.8)

        recap = TextMobject("RECAP")
        recap.to_corner(UP + LEFT)
         
        self.play(Write(root), 
                 Write(child1),
                 Write(child2),
                 Write(child11),
                 Write(child12),
                 Write(child22),
                 Write(child121),
                 Write(child122),
                 Write(child1211),
                 Write(child1212),
                 Write(arrow1),
                 Write(arrow2),
                 Write(arrow11),
                 Write(arrow12),
                 Write(arrow22),
                 Write(arrow121),
                 Write(arrow122),
                 Write(arrow1211),
                 Write(arrow1212), 
                 Write(recap)
              )

        self.wait(8)
        self.play(Write(text1), Write(text2))
        self.wait(8)
        self.play(Write(text3))
        self.wait(8)
        self.play(Write(text4))
        self.wait(60)

class Scene19(Scene):
    def construct(self):
        text1 = TextMobject("Thanks for watching!")
        text2 = TextMobject("Please LIKE and SUBSCRIBE for more videos")
        VGroup(text1, text2).arrange(DOWN)
        self.play(Write(text1), Write(text2))
        self.wait(10)

class Cover(TreeScene):
    def construct(self):
        st = self.st
        st_more = self.st_more
        st.add(st.root,
               st.child1, st.child2,
               st.child12, st.child21,
               st.arrow1, st.arrow2,
               st.arrow11, st.arrow12, st.arrow21, st.arrow22,
               st.arrow121, st.arrow122,
               st.arrow211, st.arrow212,
               st.rect11, st.rect22,
               st.rect121, st.rect122,
               st.rect211, st.rect212
                 )

        VGroup(st, st_more).arrange(LEFT)

        text1 = TextMobject("$\\theta(n\\log{}n)$")
        text1.to_edge(UP + RIGHT)
        text1.scale(2.5)
        self.play(Write(text1))

        text2 = TextMobject("bound")
        text2.next_to(text1, DOWN)
        text2.scale(2.5)
        self.play(Write(text2))

        text3 = TextMobject("for")
        text3.next_to(text2, DOWN)
        text3.scale(2.5)
        self.play(Write(text3))

        text4 = TextMobject("sorting")
        text4.next_to(text3, DOWN)
        text4.scale(2.5)
        self.play(Write(text4))

        text5 = TextMobject("algos")
        text5.next_to(text4, DOWN)
        text5.scale(2.5)
        self.play(Write(text5))


        self.play(ApplyMethod(VGroup(st).shift, FRAME_X_RADIUS * LEFT * 0.5, rate_func = running_start))
        self.play(ApplyMethod(VGroup(text1, text2, text3, text4, text5).shift, FRAME_X_RADIUS * LEFT * 0.25, rate_func = running_start))

        #self.wait(2)

        #self.play(ApplyMethod(VGroup(st, text).shift, FRAME_X_RADIUS * RIGHT * 1.5, rate_func = running_start))

        #st_more.add(
        #          st_more.text,
        #          st_more.root, 
        #          st_more.root_text,
        #          st_more.arrow1, 
        #          st_more.arrow1_text, 
        #          st_more.child1,
        #          st_more.child1_text, 
        #          st_more.child11, 
        #          st_more.child11_text, 
        #          st_more.arrow11, 
        #          st_more.arrow11_text, 
        #          st_more.rect12,
        #          st_more.child12, 
        #          st_more.arrow12, 
        #          st_more.arrow12_text, 
        #          st_more.child111, 
        #          st_more.rect111, 
        #          st_more.child112, 
        #          st_more.rect112, 
        #          st_more.arrow111, 
        #          st_more.arrow112, 
        #          st_more.arrow111_text, 
        #          st_more.arrow112_text,
        #          st_more.child2, 
        #          st_more.child2_text, 
        #          st_more.arrow2, 
        #          st_more.arrow2_text,
        #          st_more.child21, 
        #          st_more.arrow21, 
        #          st_more.arrow21_text,
        #          st_more.child221, 
        #          st_more.rect21, 
        #          st_more.child222, 
        #          st_more.rect222, 
        #          st_more.arrow221, 
        #          st_more.arrow221_text, 
        #          st_more.arrow222, 
        #          st_more.arrow222_text,
        #          st_more.arrow22, 
        #          st_more.arrow22_text, 
        #          st_more.child22, 
        #          st_more.child22_text, 
        #          st_more.rect221
        #)

        #self.play(Write(st_more.text),
        #          Write(st_more.root), 
        #          Write(st_more.root_text),
        #          Write(st_more.arrow1), 
        #          Write(st_more.arrow1_text), 
        #          Write(st_more.child1),
        #          Write(st_more.child1_text), 
        #          Write(st_more.child11), 
        #          Write(st_more.child11_text), 
        #          Write(st_more.arrow11), 
        #          Write(st_more.arrow11_text), 
        #          Write(st_more.rect12),
        #          Write(st_more.child12), 
        #          Write(st_more.arrow12), 
        #          Write(st_more.arrow12_text), 
        #          Write(st_more.child111), 
        #          Write(st_more.rect111), 
        #          Write(st_more.child112), 
        #          Write(st_more.rect112), 
        #          Write(st_more.arrow111), 
        #          Write(st_more.arrow112), 
        #          Write(st_more.arrow111_text), 
        #          Write(st_more.arrow112_text),
        #          Write(st_more.child2), 
        #          Write(st_more.child2_text), 
        #          Write(st_more.arrow2), 
        #          Write(st_more.arrow2_text),
        #          Write(st_more.child21), 
        #          Write(st_more.arrow21), 
        #          Write(st_more.arrow21_text),
        #          Write(st_more.child221), 
        #          Write(st_more.rect21), 
        #          Write(st_more.child222), 
        #          Write(st_more.rect222), 
        #          Write(st_more.arrow221), 
        #          Write(st_more.arrow221_text), 
        #          Write(st_more.arrow222), 
        #          Write(st_more.arrow222_text),
        #          Write(st_more.arrow22), 
        #          Write(st_more.arrow22_text), 
        #          Write(st_more.child22), 
        #          Write(st_more.child22_text), 
        #          Write(st_more.rect221)
        #)
        #self.play(st_more.scale, 0.8, st_more.to_edge, DOWN,)

        #text_more = TextMobject("Sorting Algorithm 2")
        #text_more.to_edge(UP)
        #self.play(Write(text_more))

        #self.wait(16)
        #st_more.circle1_text = TextMobject("1")
        #st_more.circle1_text.next_to(st_more.root, LEFT)
        #st_more.circle1_text.scale(0.8)
        #st_more.circle1_text.set_color(WHITE)
        #self.play(Write(st_more.circle1_text))

        #st_more.circle2_text = TextMobject("2")
        #st_more.circle2_text.next_to(st_more.child1, LEFT)
        #st_more.circle2_text.scale(0.8)
        #st_more.circle2_text.set_color(WHITE)
        #self.play(Write(st_more.circle2_text))

        #st_more.circle3_text = TextMobject("3")
        #st_more.circle3_text.next_to(st_more.child11, LEFT)
        #st_more.circle3_text.scale(0.8)
        #st_more.circle3_text.set_color(WHITE)
        #self.play(Write(st_more.circle3_text))
        #self.wait(40)
