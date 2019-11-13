from manimlib.imports import *

class Final(Scene):
    def construct(self):
        text = TextMobject("Concluding notes")
        text.set_color(YELLOW)
        text.to_edge(UP)

        text1 = TextMobject("Time complexity: $O(n^2)$")
        text1.next_to(text, DOWN, buff=4 * SMALL_BUFF)

        line1 = Line(LEFT, RIGHT, stroke_width=1)
        line1.set_length(14)
        line1.next_to(text1, DOWN)

        text2 = TextMobject("$O(n^2)$ holds even for fully or almost sorted array.")
        text2.next_to(line1, DOWN)

        text3 = TextMobject("Some algos run faster for almost sorted input")
        text3.next_to(text2, DOWN)

        line2 = Line(LEFT, RIGHT, stroke_width=1)
        line2.set_length(14)
        line2.next_to(text3, DOWN)

        text4 = TextMobject("Selection sort is stable")
        text4.next_to(line2, DOWN)

        self.play(Write(text), 
                  Write(text1), 
                  Write(line1), 
                  Write(text2), 
                  Write(text3),
                  Write(line2), 
                  Write(text4), 
            )
