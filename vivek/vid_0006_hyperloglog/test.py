from manimlib.imports import *

class Test1(Scene):
    CONFIG = {
        "input_space_rect_config": {
            "stroke_color": WHITE,
            "stroke_width": 1,
            "fill_color": DARKER_GREY,
            "fill_opacity": 1,
            "width": 6,
            "height": 2,
        },
    }
    def construct(self):
        rect = Rectangle(**self.input_space_rect_config)
        rect.to_corner(UL, buff=SMALL_BUFF)
        input_line = UnitInterval()
        input_dot = Dot()
        input_tracker = ValueTracker(0)
        get_input = input_tracker.get_value
        f_always(
            input_dot.move_to,
            lambda: input_line.n2p(get_input())
        )

        self.play(
            FadeInFromLarge(input_dot),
        )
        #kw = {
        #    "run_time": 10,
        #    "rate_func": lambda t: smooth(t, 1),
        #}
        #self.play(
        #    ApplyMethod(input_tracker.set_value, 1, **kw),
        #)
        for value in 1, 0:
            self.play(
                input_tracker.set_value, value,
                run_time=2
            )

    def get_input_line(self, input_rect):
        input_line = UnitInterval()
        input_line.move_to(input_rect)
        input_line.shift(0.25 * UP)
        input_line.set_width(
            input_rect.get_width() - 1
        )
        input_line.add_numbers(0, 0.5, 1)
        return input_line

